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

Never put a Workspace password, OAuth token, or SMTP credential in the website.
The endpoint has a fixed recipient, input validation, a honeypot, and a basic
hourly limit to reduce abuse.

Send the `/exec` URL to the site maintainer. It must be placed in the contact
form's `data-endpoint` attribute before the site can use this endpoint.
