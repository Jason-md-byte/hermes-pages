# Form-to-Slack Notification Workflow

**Price:** $39

Turn any web form into an instant Slack notification. When a user submits a form — contact form, lead gen form, survey, or support ticket — this workflow catches it via webhook, packages it into a rich Slack message with header, fields, and context, and posts it to your team channel. The submitter gets a clean confirmation response while your team acts immediately.

**Key Features:**
- Webhook trigger — embed in any HTML form, Typeform, or custom frontend
- Rich Slack message formatting — header, divider, fields (name, email, subject, message), and timestamp
- Real-time team notifications — no polling, no delays
- Auto-confirmation response to the form submitter
- Configurable Slack webhook URL via n8n variables
- 10-second timeout with error handling

**Setup Requirements:**
- n8n self-hosted instance (any deployment: Docker, n8n.cloud, or local)
- Slack webhook URL (create via Slack Apps > Incoming Webhooks)
- Basic ability to point a form's `action` attribute to the n8n webhook URL

**What the Buyer Gets:**
- Ready-to-import n8n workflow JSON file (`form-to-slack.json`)
- Webhook endpoint at `/webhook/form-submit`
- Slack message template with header, divider, fields, and context blocks
- Confirmation response payload
- Easy setup: import → set Slack webhook URL → activate
