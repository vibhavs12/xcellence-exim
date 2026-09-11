#!/usr/bin/env node

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');

const root = path.resolve(__dirname, '..');
const parts = fs.readFileSync(path.join(root, 'build/parts.py'), 'utf8');
const logoPath = 'assets/img/brand/logo.png';
const logoUrl = 'https://xcellenceexim.com/' + logoPath;
const faviconPath = 'assets/img/brand/favicon.png';
const faviconUrl = 'https://xcellenceexim.com/' + faviconPath;

assert.match(parts, /"logo":\s*SITE \+ "\/assets\/img\/brand\/logo\.png"/,
  'shared header/footer logo must use the versioned local asset route');
assert.ok(fs.existsSync(path.join(root, logoPath)),
  'the local logo asset must be included in the deployed site');
assert.match(parts, /"favicon":\s*SITE \+ "\/assets\/img\/brand\/favicon\.png"/,
  'shared page chrome must expose the square favicon asset');
assert.ok(fs.existsSync(path.join(root, faviconPath)),
  'the square favicon asset must be included in the deployed site');

const favicon = fs.readFileSync(path.join(root, faviconPath));
assert.equal(favicon.readUInt32BE(16), 512, 'favicon must be 512 pixels wide');
assert.equal(favicon.readUInt32BE(20), 512, 'favicon must be 512 pixels high');

execFileSync('python3', ['build/build.py'], { cwd: root, stdio: 'inherit' });

for (const page of ['index.html', 'spices/index.html', 'contact-us/index.html']) {
  const html = fs.readFileSync(path.join(root, page), 'utf8');
  const logoSources = [...html.matchAll(/<img[^>]+src="([^"]*logo\.png)"[^>]*alt="Xcellence Exim(?: — Indian Agro Exporter)?"/g)];
  assert.equal(logoSources.length, 2,
    `${page} must render the local logo once in the header and once in the footer`);
  for (const [, src] of logoSources) {
    assert.equal(src, logoUrl, `${page} must not use the legacy wp-content logo route`);
  }
  assert.match(html, new RegExp(`<link rel="icon" href="${faviconUrl}" sizes="any">`),
    `${page} must use the square favicon in its rel="icon" link`);
  assert.match(html, new RegExp(`<link rel="apple-touch-icon" href="${faviconUrl}">`),
    `${page} must use the square favicon in its apple-touch-icon link`);
  assert.match(html, new RegExp(`"logo": "${faviconUrl}"`),
    `${page} must use the square favicon as its Organization JSON-LD logo`);
}

console.log('Logo delivery tests passed.');
