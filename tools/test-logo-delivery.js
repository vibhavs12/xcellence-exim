#!/usr/bin/env node

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');

const root = path.resolve(__dirname, '..');
const parts = fs.readFileSync(path.join(root, 'build/parts.py'), 'utf8');
const logoPath = 'assets/img/brand/logo.png';
const logoUrl = 'https://xcellenceexim.com/' + logoPath;

assert.match(parts, /"logo":\s*SITE \+ "\/assets\/img\/brand\/logo\.png"/,
  'shared header/footer logo must use the versioned local asset route');
assert.ok(fs.existsSync(path.join(root, logoPath)),
  'the local logo asset must be included in the deployed site');

execFileSync('python3', ['build/build.py'], { cwd: root, stdio: 'inherit' });

for (const page of ['index.html', 'spices/index.html', 'contact-us/index.html']) {
  const html = fs.readFileSync(path.join(root, page), 'utf8');
  const logoSources = [...html.matchAll(/<img[^>]+src="([^"]*logo\.png)"[^>]*alt="Xcellence Exim(?: — Indian Agro Exporter)?"/g)];
  assert.equal(logoSources.length, 2,
    `${page} must render the local logo once in the header and once in the footer`);
  for (const [, src] of logoSources) {
    assert.equal(src, logoUrl, `${page} must not use the legacy wp-content logo route`);
  }
}

console.log('Logo delivery tests passed.');
