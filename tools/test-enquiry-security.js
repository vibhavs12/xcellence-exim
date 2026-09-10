#!/usr/bin/env node

const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const REQUIRED_INPUT = {
  name: 'Buyer Example',
  email: 'buyer@example.com',
  country: 'United Kingdom',
  product: 'Rice — Basmati',
  message: 'Please quote one 20 ft container.',
  privacy_acknowledged: 'yes'
};

function loadScript(turnstileResult) {
  const calls = { mail: [], verify: [] };
  const output = (value) => ({
    setMimeType() { return this; },
    getContent() { return value; }
  });
  const context = {
    console: { error: () => {}, log: () => {} },
    JSON,
    Date,
    String,
    Number,
    Object,
    Array,
    RegExp,
    Utilities: { formatDate: () => '2026091014' },
    ContentService: { MimeType: { JSON: 'application/json' }, createTextOutput: output },
    PropertiesService: {
      getScriptProperties: () => ({ getProperty: (name) => name === 'TURNSTILE_SECRET' ? 'test-secret' : null })
    },
    UrlFetchApp: {
      fetch: (url, options) => {
        calls.verify.push({ url, options });
        return { getContentText: () => JSON.stringify(turnstileResult) };
      }
    },
    CacheService: { getScriptCache: () => ({ get: () => '0', put: () => {} }) },
    LockService: { getScriptLock: () => ({ tryLock: () => true, releaseLock: () => {} }) },
    MailApp: { sendEmail: (message) => calls.mail.push(message) }
  };
  vm.createContext(context);
  vm.runInContext(fs.readFileSync('integrations/google-apps-script/Code.gs', 'utf8'), context);
  return { context, calls };
}

function submit(context, extra = {}) {
  const output = context.doPost({ parameter: { ...REQUIRED_INPUT, ...extra } });
  return JSON.parse(output.getContent());
}

{
  const { context, calls } = loadScript({ success: false, 'error-codes': ['invalid-input-response'] });
  const result = submit(context, { 'cf-turnstile-response': 'bad-token' });
  assert.equal(result.ok, false, 'invalid Turnstile must be rejected');
  assert.equal(calls.mail.length, 0, 'invalid Turnstile must not send mail');
  assert.equal(calls.verify.length, 1, 'server must validate every token');
}

{
  const { context, calls } = loadScript({
    success: true,
    action: 'rfq_form',
    hostname: 'xcellenceexim.com'
  });
  const result = submit(context, { 'cf-turnstile-response': 'valid-token' });
  assert.equal(result.ok, true, 'valid Turnstile should permit a genuine enquiry');
  assert.equal(calls.mail.length, 1, 'valid Turnstile should permit mail delivery');
  assert.equal(calls.verify.length, 1, 'server must verify before delivery');
  assert.equal(calls.verify[0].url, 'https://challenges.cloudflare.com/turnstile/v0/siteverify');
}

{
  const { context, calls } = loadScript({
    success: true,
    action: 'wrong_action',
    hostname: 'xcellenceexim.com'
  });
  const result = submit(context, { 'cf-turnstile-response': 'wrong-action-token' });
  assert.equal(result.ok, false, 'a token for another action must be rejected');
  assert.equal(calls.mail.length, 0, 'wrong-action token must not send mail');
}

{
  const { context, calls } = loadScript({
    success: true,
    action: 'rfq_form',
    hostname: 'attacker.example'
  });
  const result = submit(context, { 'cf-turnstile-response': 'wrong-host-token' });
  assert.equal(result.ok, false, 'a token from another hostname must be rejected');
  assert.equal(calls.mail.length, 0, 'wrong-hostname token must not send mail');
}

{
  const contactPage = fs.readFileSync('contact-us/index.html', 'utf8');
  assert.match(contactPage, /challenges\.cloudflare\.com\/turnstile\/v0\/api\.js/,
    'contact page must load Turnstile');
  assert.match(contactPage, /class="cf-turnstile"[^>]+data-sitekey="test-site-key"/,
    'contact page must render the configured public site key');
  assert.match(contactPage, /class="cf-turnstile"[^>]+data-action="rfq_form"/,
    'widget must issue a token for the RFQ action');
  const formScript = fs.readFileSync('assets/js/main.js', 'utf8');
  assert.match(formScript, /payload\['cf-turnstile-response'\] = turnstileToken\(\)/,
    'browser must include the verification token in the RFQ request');
}

console.log('RFQ enquiry security tests passed.');
