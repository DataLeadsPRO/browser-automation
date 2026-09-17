# Browser Automation API (Headless Sessions)

> Programmatic headless browser sessions: create, interact, browse, and extract - rendered in a real browser.

Part of the **DataLeads** API suite (Tools category). Requests render in a real browser with anti-bot handling and protected-page support built in - no proxies to manage, no infrastructure to run.

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/session/create` | V1 Session Create |
| POST | `/interact` | V1 Interact |
| POST | `/session/list` | V1 Session List |
| POST | `/session/delete` | V1 Session Delete |
| POST | `/browse` | V1 Browse |

## Quick start

```bash
curl -X POST https://data.dataleads.pro/v1/session/create \
  -H 'Content-Type: application/json' \
  -d '{"clientKey": "YOUR_CLIENT_KEY", "url": "https://example.com", "extract": ["title", "markdown"]}'
```

Replace `YOUR_CLIENT_KEY` with your key. Get one at [https://data.dataleads.pro](https://data.dataleads.pro) - free tier included.

## MCP server

- **Remote (Streamable HTTP):** `https://data.dataleads.pro/mcp/browser-automation`
- **Stdio (Docker):** `docker run -e DATALEADS_API_KEY=yourkey ghcr.io/dataleads/browser-automation-mcp:latest`

## Pricing

| Tier | Price | Requests |
|---|---|---|
| Free | $0 | 500/mo |
| Starter | $9/mo | 5,000 |
| Pro | $29/mo | 25,000 |
| Business | $99/mo | 100,000 |
| Enterprise | custom | custom |

Full plan details at [https://data.dataleads.pro](https://data.dataleads.pro).

## License

MIT - see [LICENSE](LICENSE).
