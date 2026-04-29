# Public APIs Curated for Jason's n8n Biz Ops Streams

> Curated from [public-apis](https://github.com/public-apis/public-apis) (195KB README, 50+ categories, 1000+ APIs)
> Target: n8n workflows running on localhost:5678

---

## 1. Cryptocurrency APIs → Crypto Bot Data Feeds

**Biz Ops Stream:** Crypto Bot — real-time price feeds, trading signals, portfolio tracking

| # | API | URL | Description | Auth |
|---|-----|-----|-------------|------|
| 1 | **CoinGecko** | https://www.coingecko.com/api | Cryptocurrency Price, Market, and Developer/Social Data | No |
| 2 | **CoinMarketCap** | https://coinmarketcap.com/api/ | Cryptocurrencies Prices | apiKey |
| 3 | **Binance** | https://github.com/binance/binance-spot-api-docs | Exchange for Trading Cryptocurrencies | apiKey |
| 4 | **CoinCap** | https://docs.coincap.io/ | Real time Cryptocurrency prices through a RESTful API | No |
| 5 | **CryptoCompare** | https://www.cryptocompare.com/api# | Cryptocurrencies Comparison | No |

**n8n Usage:**
- **CoinGecko** (no auth!) → HTTP Request node → Poll every 5 min → Compare prices → Telegram alert on breakouts
- **Binance** → WebSocket/HTTP node → Real-time ticker data → Feed into Crypto Bot decision logic
- **CoinMarketCap** → HTTP Request node → Daily market cap rankings → Google Sheets write for portfolio tracking
- **CoinCap** (no auth!) → Simple REST poll → Dashboard widget in n8n
- **Template product:** "Crypto Price Alert Bot" — CoinGecko + Telegram + Google Sheets

---

## 2. Finance APIs → Crypto Bot & General Templates

**Biz Ops Stream:** Crypto Bot data feeds, template products

| # | API | URL | Description | Auth |
|---|-----|-----|-------------|------|
| 1 | **Alpha Vantage** | https://www.alphavantage.co/ | Realtime and historical stock data | apiKey |
| 2 | **Finnhub** | https://finnhub.io/docs/api | Real-Time RESTful APIs and Websocket for Stocks, Currencies, and Crypto | apiKey |
| 3 | **Yahoo Finance** | https://www.yahoofinanceapi.com/ | Real time low latency Yahoo Finance API for stock market, crypto, forex | apiKey |
| 4 | **IEX Cloud** | https://iexcloud.io/docs/api/ | Realtime & Historical Stock and Market Data | apiKey |
| 5 | **Twelve Data** | https://twelvedata.com/ | Stock market data (real-time & historical) | apiKey |

**n8n Usage:**
- **Alpha Vantage** → HTTP Request node → Poll stock prices → Condition node for threshold → Email/Slack alert
- **Finnhub** → News + price combined → Sentiment analysis pipeline
- **Template product:** "Multi-Asset Price Dashboard" — poll Alpha Vantage + CoinGecko → n8n dashboard

---

## 3. News APIs → YouTube Channel 5 Content

**Biz Ops Stream:** YouTube Channel 5 — content research, trending topics, auto-summarization

| # | API | URL | Description | Auth |
|---|-----|-----|-------------|------|
| 1 | **NewsAPI** | https://newsapi.org/ | Headlines from a range of news sources and blogs | apiKey |
| 2 | **GNews** | https://gnews.io/ | Search for news from various sources | apiKey |
| 3 | **Mediastack** | https://mediastack.com/ | Free, Simple REST API for Live News & Blog Articles | apiKey |
| 4 | **New York Times** | https://developer.nytimes.com/ | The New York Times Developer Network | apiKey |
| 5 | **The Guardian** | http://open-platform.theguardian.com/ | Access all content the Guardian creates | apiKey |

**n8n Usage:**
- **NewsAPI** → HTTP Request node (keyword search) → Filter node → Compose script (summarize top 5) → YouTube script output
- **GNews** → Scheduled trigger (daily) → Search "AI" / "business" → Write to Google Doc → YouTube script draft
- **The Guardian** → Topic-based query → HTML to Markdown → OpenAI node for summary → Script outline
- **Template product:** "Daily News Digester for YouTubers" — NewsAPI → GPT summary → Google Doc → Telegram notification

---

## 4. Business & Marketing APIs → Appointment Setting Lead Gen

**Biz Ops Stream:** Appointment Setting — lead enrichment, email validation, company research

| # | API | URL | Description | Auth |
|---|-----|-----|-------------|------|
| 1 | **Clearbit Logo** | https://clearbit.com/docs#logo-api | Search for company logos | apiKey |
| 2 | **Mailchimp** | https://mailchimp.com/developer/ | Send marketing campaigns and transactional mails | apiKey |
| 3 | **Tomba Email Finder** | https://tomba.io/api | Email Finder for B2B sales and email marketing | apiKey |
| 4 | **ORB Intelligence** | https://api.orb-intelligence.com/docs/ | Company lookup | apiKey |
| 5 | **Trello** | https://developers.trello.com/ | Boards, lists and cards to organize projects | OAuth |

**n8n Usage:**
- **Tomba** → HTTP Request node → Input: company URL → Output: decision maker email → Add to CRM list
- **ORB Intelligence** → Company lookup → Enrich lead record → Store in Airtable/Google Sheets
- **Clearbit Logo** → Enrich CRM with company logos for outreach personalization
- **Trello** → Lead moved to "Contacted" → Trello card auto-update → Slack notification to sales team
- **Template product:** "B2B Lead Enrichment Pipeline" — Tomba + ORB Intelligence + Google Sheets + Gmail

---

## 5. AI/ML APIs → Template Product Ideas

**Biz Ops Stream:** Template product ideas for the n8n marketplace

| # | API | URL | Description | Auth |
|---|-----|-----|-------------|------|
| 1 | **NLP Cloud** | https://nlpcloud.io | NLP API using spaCy and transformers for NER, sentiments, classification, summarization | apiKey |
| 2 | **Clarifai** | https://docs.clarifai.com/api-guide/api-overview | Computer Vision | OAuth |
| 3 | **WolframAlpha** | https://products.wolframalpha.com/api/ | Provides specific answers using data and algorithms | apiKey |
| 4 | **Perspective** | https://perspectiveapi.com | NLP API to detect toxic/obscene/insulting text | apiKey |
| 5 | **Roboflow Universe** | https://universe.roboflow.com | Pre-trained computer vision models | apiKey |

**n8n Usage:**
- **NLP Cloud** → HTTP Request → Summarize articles/news → YouTube script creator template
- **Clarifai** → Image upload → Auto-tag → Google Sheets catalog → CMS product feed
- **Perspective** → Comment moderation workflow → Auto-filter toxic comments → Slack alert
- **Template product ideas:**
  - "AI Content Moderator" — Perspective API + n8n + Slack
  - "Smart Document Classifier" — NLP Cloud + Google Drive + Airtable
  - "Automated Meeting Notes" — Transcriber + NLP Cloud summary + Notion

---

## 6. Weather & Geolocation APIs → General n8n Templates

**Biz Ops Stream:** General templates, local business automation, logistics

| # | API | URL | Description | Auth |
|---|-----|-----|-------------|------|
| 1 | **OpenWeatherMap** | https://openweathermap.org/api | Weather data for any location | apiKey |
| 2 | **Open-Meteo** | https://open-meteo.com/ | Global weather forecast API (no auth!) | No |
| 3 | **ipapi.co** | https://ipapi.co/api/#introduction | Find IP address location information | No |
| 4 | **OpenCage** | https://opencagedata.com | Forward and reverse geocoding using open data | apiKey |
| 5 | **Nominatim** | https://nominatim.org/release-docs/latest/api/Overview/ | Worldwide forward/reverse geocoding (no auth!) | No |

**n8n Usage:**
- **Open-Meteo** (no auth!) → HTTP Request → Get weather for any city → Condition (rain?) → SMS/Telegram alert
- **OpenWeatherMap** → Scheduled trigger (7 AM daily) → Weather + forecast → Email digest to field team
- **ipapi.co** → Webhook trigger → Get visitor IP → Geolocate → Route to appropriate regional sales team
- **Nominatim** (no auth!) → Geocode addresses from Google Sheets → Mapbox visualization
- **Template product:** "Weather-Aware Local Business Automation" — OpenWeatherMap + Telegram + Google Calendar

---

## 7. Email APIs → Appointment Setting & Marketing

**Biz Ops Stream:** Appointment Setting — email verification, deliverability

| # | API | URL | Description | Auth |
|---|-----|-----|-------------|------|
| 1 | **SendGrid** | https://docs.sendgrid.com/api-reference/ | Cloud-based SMTP provider for sending emails | apiKey |
| 2 | **Sendinblue** | https://developers.sendinblue.com/docs | Marketing and transactional email/SMS | apiKey |
| 3 | **MailboxValidator** | https://www.mailboxvalidator.com/api-email-free | Validate email to improve deliverability | apiKey |
| 4 | **Abstract Email Validation** | https://www.abstractapi.com/email-verification-validation-api | Validate emails for deliverability and spam | apiKey |
| 5 | **ImprovMX** | https://improvmx.com/api | API for free email forwarding service | apiKey |

**n8n Usage:**
- **SendGrid** → n8n Email node alternative → Bulk campaign → Track opens/clicks → Update lead scoring
- **Abstract Email Validation** → Webhook (new lead form) → Validate email → If valid, add to Mailchimp list
- **Sendinblue** → Transactional emails triggered by lead stage changes

---

## 8. Bonus: Best n8n Template Product Candidates

APIs that combine well into sellable n8n workflow templates:

| Template Product | APIs Needed | Biz Ops Stream |
|---|---|---|
| **Crypto Price Alert Bot** | CoinGecko + Telegram + Google Sheets | Crypto Bot |
| **Daily News Digester** | NewsAPI/GNews + OpenAI + Google Docs | YouTube Channel 5 |
| **B2B Lead Enrichment Pipeline** | Tomba + ORB Intelligence + Google Sheets + Gmail | Appointment Setting |
| **Weather-Aware Scheduler** | Open-Meteo + Telegram + Google Calendar | General |
| **Content Moderator** | Perspective API + Slack + Gmail | AI/ML Templates |
| **AI Summarizer** | NLP Cloud + HTTP Webhook + Notion | AI/ML Templates |
| **IP to Lead Router** | ipapi.co + Airtable + Slack | Appointment Setting |
| **Market Snapshot** | Alpha Vantage + CoinGecko + Twelve Data + Sheets | Crypto Bot |

---

## Category Breakdown Summary

| Category | Total APIs | Top Pick | Best For |
|---|---|---|---|
| Cryptocurrency | 67 APIs | CoinGecko (free, no auth) | Crypto Bot data feeds |
| Finance | 47 APIs | Alpha Vantage (free tier) | Market data, trading signals |
| News | 19 APIs | NewsAPI (developer tier free) | YouTube content research |
| Business | 24 APIs | Tomba Email Finder | Lead enrichment |
| Machine Learning | 22 APIs | NLP Cloud (free trial) | AI template products |
| Weather | 35 APIs | Open-Meteo (no auth, free) | General automation |
| Geocoding | 70+ APIs | ipapi.co (free, no auth) | IP routing, logistics |
| Email | 18 APIs | SendGrid (free tier) | Marketing automation |

---

*Curated from public-apis repository. All APIs listed have free tiers or free access. Test on n8n localhost:5678 before deploying.*
