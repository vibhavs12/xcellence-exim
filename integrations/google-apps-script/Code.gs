/**
 * Xcellence Exim website enquiry endpoint.
 *
 * Deploy this Apps Script as a web app from the Workspace mailbox that should
 * appear as the sender (recommended: info@xcellenceexim.com). The destination
 * is deliberately fixed so public callers cannot turn the endpoint into an
 * open email relay.
 */

var CONFIG = Object.freeze({
  recipient: 'sales@xcellenceexim.com',
  cc: 'ashwani@xcellenceexim.com',
  senderName: 'Xcellence Exim Website',
  allowedProducts: [
    'Rice — Basmati',
    'Rice — Non-Basmati',
    'Coffee — Green beans',
    'Coffee — Roasted beans',
    'Coffee — Instant',
    'Spices — Sannam S4 red chilli',
    'Spices — Other',
    'Sugar ICUMSA 45',
    'Sugar — Other grade',
    'Other agro commodity'
  ],
  maxPerHour: 30
});

function doGet() {
  return json_({ ok: true, service: 'Xcellence Exim enquiry endpoint' });
}

function doPost(e) {
  try {
    var input = (e && e.parameter) || {};

    // Honeypot submissions are acknowledged but never mailed.
    if (text_(input.company_website, 200)) {
      return json_({ ok: true });
    }

    enforceRateLimit_();

    var enquiry = {
      name: required_(input.name || input['Full name'], 'Full name', 120),
      company: text_(input.company || input.Company, 160),
      email: required_(input.email || input.Email, 'Email', 254).toLowerCase(),
      phone: text_(input.phone || input['Phone / WhatsApp'], 80),
      country: required_(input.country || input['Destination country'], 'Destination country', 100),
      port: text_(input.port || input['Destination port'], 120),
      product: required_(input.product || input.Product, 'Product', 100),
      quantity: text_(input.quantity || input['Quantity required'], 100),
      incoterm: text_(input.incoterm || input['Preferred Incoterm'], 40),
      packing: text_(input.packing || input['Packing preference'], 180),
      message: required_(input.message || input.Message, 'Message', 4000),
      source: text_(input.source || input._url, 300)
    };

    if (text_(input.privacy_acknowledged, 10).toLowerCase() !== 'yes') {
      throw new Error('Privacy acknowledgement is required.');
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(enquiry.email)) {
      throw new Error('Please enter a valid email address.');
    }
    if (CONFIG.allowedProducts.indexOf(enquiry.product) === -1) {
      throw new Error('Please select a valid product.');
    }

    var subject = [
      'Export enquiry', enquiry.product, enquiry.country, enquiry.name
    ].join(' — ');

    var rows = [
      ['Full name', enquiry.name],
      ['Company', enquiry.company],
      ['Email', enquiry.email],
      ['Phone / WhatsApp', enquiry.phone],
      ['Destination country', enquiry.country],
      ['Destination port', enquiry.port],
      ['Product', enquiry.product],
      ['Quantity required', enquiry.quantity],
      ['Preferred Incoterm', enquiry.incoterm],
      ['Packing preference', enquiry.packing],
      ['Message', enquiry.message],
      ['Privacy notice acknowledged', 'Yes'],
      ['Submitted from', enquiry.source],
      ['Received', new Date().toISOString()]
    ];

    MailApp.sendEmail({
      to: CONFIG.recipient,
      cc: CONFIG.cc,
      subject: subject,
      body: plainBody_(rows),
      htmlBody: htmlBody_(rows),
      name: CONFIG.senderName,
      replyTo: enquiry.email
    });

    return json_({ ok: true });
  } catch (error) {
    console.error(error);
    return json_({ ok: false, message: String(error && error.message || error) });
  }
}

function required_(value, label, maxLength) {
  var result = text_(value, maxLength);
  if (!result) throw new Error(label + ' is required.');
  return result;
}

function text_(value, maxLength) {
  return String(value == null ? '' : value).trim().slice(0, maxLength || 500);
}

function enforceRateLimit_() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(1500)) throw new Error('The enquiry service is busy. Please retry.');
  try {
    var cache = CacheService.getScriptCache();
    var bucket = Utilities.formatDate(new Date(), 'UTC', 'yyyyMMddHH');
    var key = 'enquiries-' + bucket;
    var count = Number(cache.get(key) || 0);
    if (count >= CONFIG.maxPerHour) {
      throw new Error('The enquiry limit has been reached. Please retry later.');
    }
    cache.put(key, String(count + 1), 3600);
  } finally {
    lock.releaseLock();
  }
}

function plainBody_(rows) {
  return rows
    .filter(function (row) { return row[1]; })
    .map(function (row) { return row[0] + ': ' + row[1]; })
    .join('\n');
}

function htmlBody_(rows) {
  var bodyRows = rows
    .filter(function (row) { return row[1]; })
    .map(function (row) {
      return '<tr><th style="text-align:left;padding:10px 14px;border-bottom:1px solid #d9e2dd;color:#0f3d2e;vertical-align:top">' +
        escapeHtml_(row[0]) +
        '</th><td style="padding:10px 14px;border-bottom:1px solid #d9e2dd;white-space:pre-wrap">' +
        escapeHtml_(row[1]) + '</td></tr>';
    })
    .join('');

  return '<div style="font-family:Arial,sans-serif;color:#24312b;max-width:720px">' +
    '<h2 style="color:#0f3d2e">New website export enquiry</h2>' +
    '<p>Replying to this message will address the buyer directly.</p>' +
    '<table style="border-collapse:collapse;width:100%;border:1px solid #d9e2dd">' +
    bodyRows + '</table></div>';
}

function escapeHtml_(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function json_(value) {
  return ContentService
    .createTextOutput(JSON.stringify(value))
    .setMimeType(ContentService.MimeType.JSON);
}
