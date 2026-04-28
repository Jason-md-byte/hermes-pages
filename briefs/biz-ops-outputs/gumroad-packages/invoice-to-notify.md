# Invoice-to-Notify Email Workflow

**Price:** $39

Automatically send professional invoice notifications to your clients the moment an invoice is generated. This workflow accepts invoice data via webhook, formats a clean email with invoice details (number, amount, due date, line items), sends it through your SMTP server, and logs every notification for your records. No more copy-pasting invoice emails.

**Key Features:**
- Webhook trigger — send invoice data from your billing system, backend, or manual tool
- Rich email formatting — invoice number, client info, amount, currency, due date, status, line-by-line item breakdown
- SMTP email delivery — works with any SMTP provider (SendGrid, Mailgun, Gmail SMTP, etc.)
- Automated audit logging — every sent invoice is timestamped and logged to a local file
- Configurable sender email and SMTP credentials via n8n variables
- Plain-text email format for maximum inbox compatibility

**Setup Requirements:**
- n8n self-hosted instance (any deployment: Docker, n8n.cloud, or local)
- SMTP server credentials (from your email provider)
- Invoice data sent as JSON POST to the webhook endpoint

**What the Buyer Gets:**
- Ready-to-import n8n workflow JSON file (`invoice-to-notify.json`)
- Webhook endpoint at `/webhook/invoice-notify`
- Pre-formatted email template with invoice details and line items
- File-based audit log of all sent invoices
- Easy setup: import → configure SMTP → activate
