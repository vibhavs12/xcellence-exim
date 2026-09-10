# Google Workspace enquiry endpoint

This endpoint sends website enquiries through the Workspace account that
deploys it. Deploy it while signed in as `info@xcellenceexim.com` (or as a
Workspace user whose mailbox should appear in the email's From field).

## Deploy

1. Open <https://script.google.com> while signed in to the sending Workspace
   mailbox and create a **New project** named `Xcellence Exim Enquiries`.
2. Replace `Code.gs` with the contents of this folder's `Code.gs`.
3. In **Project Settings**, enable **Show "appsscript.json" manifest file in
   editor**, then replace the manifest with this folder's `appsscript.json`.
4. Select **Deploy → New deployment → Web app**.
5. Set **Execute as** to **Me** and **Who has access** to **Anyone**.
6. Authorize the requested send-mail permission and copy the production URL
   ending in `/exec`.

Never put a Workspace password, OAuth token, SMTP credential, or Turnstile
secret in the website or Git repository. The endpoint has a fixed recipient,
input validation, a honeypot, server-verified Turnstile protection, and a
basic hourly limit to reduce abuse.

## Turnstile configuration (required before deployment)

1. In the Cloudflare dashboard, create a **Turnstile** widget named `Xcellence
   Exim RFQ` in **Managed** mode. Restrict it to `xcellenceexim.com` and
   `www.xcellenceexim.com`.
2. Keep the secret key private. In the Apps Script editor, open **Project
   Settings → Script properties** and add `TURNSTILE_SECRET` with that secret
   as its value.
3. The public site key is not a secret. Rebuild the static site using it:

   ```bash
   TURNSTILE_SITE_KEY='public-site-key-from-cloudflare' python3 build/build.py
   ```

4. Replace `Code.gs` and `appsscript.json` in the Apps Script project, then
   deploy a **new version** of the existing web app. The added external-request
   scope is needed to validate tokens with Cloudflare.
5. Deploy the rebuilt static site immediately after the Apps Script version.
   During that short interval, the endpoint safely rejects unverified form
   posts rather than sending spam.

Apps Script rejects missing, expired, replayed, wrong-action, and
wrong-hostname tokens before it counts or emails an enquiry.

Send the `/exec` URL to the site maintainer. It must be placed in the contact
form's `data-endpoint` attribute before the site can use this endpoint.
