# Lead Capture to CRM Workflow

**Price:** $39

Capture and qualify leads from any web form directly into your CRM system. This workflow accepts lead submissions via webhook, validates that all required fields (name, email, phone, message) are present, posts valid leads to your CRM API, and returns appropriate success or failure responses. Send only quality, complete leads into your pipeline — no more wasted time on partial form submissions.

**Key Features:**
- Webhook trigger — embed in landing pages, contact forms, or lead magnets
- Built-in field validation — requires name, email, phone, and message with AND logic
- CRM API integration — POST valid leads to any REST API endpoint
- API key authentication — secure header-based auth for your CRM
- Smart response routing — success response for valid leads, detailed validation error for incomplete submissions
- Source tagging — each lead is tagged with `n8n-webhook` source identifier
- 10-second timeout with SSL verification

**Setup Requirements:**
- n8n self-hosted instance (any deployment: Docker, n8n.cloud, or local)
- A CRM system with a REST API endpoint for creating contacts/leads
- API key or header-based auth credentials for your CRM
- Basic ability to point a form's submission URL to the n8n webhook endpoint

**What the Buyer Gets:**
- Ready-to-import n8n workflow JSON file (`lead-capture-to-crm.json`)
- Webhook endpoint at `/webhook/lead-capture`
- Input validation logic (name, email, phone, message — all required)
- CRM POST integration with API key authentication
- Success and error response templates
- Easy setup: import → configure CRM endpoint + API key → activate
