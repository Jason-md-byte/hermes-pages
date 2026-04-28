# 3 Workflow Bundle — Business Automation Starter Pack

**Price:** $79 (Save $38 vs. buying individually)

Get all three production-ready n8n workflows at a bundle discount. The Business Automation Starter Pack covers your essential communication and lead management needs: capture leads from any form into your CRM, notify your team instantly via Slack when someone reaches out, and send professional invoice notifications automatically. These three workflows replace the need for Zapier, Mailchimp transactional emails, and partial form-to-Slack integrations — all running on your own self-hosted n8n instance.

**What's Included:**

| Workflow | Purpose | Price |
|---|---|---|
| Lead Capture to CRM | Form submissions → validation → CRM API | $39 |
| Form-to-Slack Notification | Form submissions → rich Slack alerts | $39 |
| Invoice-to-Notify Email | Invoice data → formatted email → audit log | $39 |
| **Bundle Total** | | **$79** |

**Key Features:**
- All three workflows import-ready with zero modification needed
- Webhook-driven architecture — works with any form, frontend, or backend
- Configurable via n8n variables (no hardcoded credentials)
- Validation and error handling built into every workflow
- Audit logging included in the invoice workflow
- Clean separation of concerns — use individually or chain together

**Setup Requirements:**
- n8n self-hosted instance (any deployment: Docker, n8n.cloud, or local)
- Slack webhook URL (for Form-to-Slack workflow)
- SMTP server credentials (for Invoice-to-Notify workflow)
- CRM REST API endpoint + API key (for Lead Capture workflow)
- n8n variables configured: `slackWebhookUrl`, `smtpFromEmail`, `smtpCredentialId`, `crmEndpoint`, `crmCredentialId`

**What the Buyer Gets:**
- Three ready-to-import n8n workflow JSON files:
  - `lead-capture-to-crm.json`
  - `form-to-slack.json`
  - `invoice-to-notify.json`
- All webhook endpoints and connection wiring pre-configured
- Email and Slack message templates pre-built
- Audit log infrastructure included
- 34% savings vs. buying each workflow individually
