# Report template (Markdown deliverable)

Use this exact structure. The file doubles as LLM-prompt input later, so keep it self-contained: every number carries its basis inline, tables are plain Markdown, no HTML or images.

```markdown
# Market & Marketing Analysis: [App Name]

**Summary:** [3–4 sentences: the opportunity, the headline numbers, the recommended move + its gate condition]

**Framing:** [geography] · [monetization + price] · [budget ceiling / key constraint]

## 1. Market size

- **TAM:** [range] — [method, sources, flagged assumptions]
- **SAM:** [range] — [filter logic, flagged assumptions]
- **SOM (yr 1):** [range] — [bottom-up math]
- [Proxy markets if used, labeled as proxies. Binding constraint stated.]

## 2. Competitors

- **[Competitor]** — [strengths] / [pricing] / [weaknesses]
- [...one line each, direct then indirect]
- **Positioning opportunity:** [one line]
- [Pricing read: where the user's price sits]

## 3. Risks

1. **[Risk]** — [High/Med/Low] — [mitigation]
2. [...ordered by severity; shared root cause + cheapest validation experiment named]

## 4. Feature review

- **Cut/defer:** [...with market reasons]
- **Add:** [...with market reasons]
- **MVP focus:** [the smallest marketable version, one sentence]

## 5. Go-to-market

- **Channels:** [assessment, one line each]
- **Most promising source:** [channel] — [why]
- **Campaign:** [hook] + [pre-launch / launch / growth phases]
- **Metrics:** [each with a target number]

## 6. Marketing budget (USD)

| Channel | [Phase 1] | [Phase 2] | [Phase 3] | Total |
|---|---|---|---|---|
| [...rows including a reserve line; columns sum to the ceiling] |

- **Recommended starting spend:** [figure + gate condition]
- **Scaling rule:** [numeric rule]

## 7. Revenue projection (12 months, USD)

| | Conservative | Base | Optimistic |
|---|---|---|---|
| Installs | | | |
| Install→paying | | | |
| Paying users | | | |
| Gross revenue | | | |
| **Net after store commission** | | | |

- Key assumptions: [each labeled sourced vs. assumed; widest-variance assumption named]
- Sanity checks: [vs. SAM, vs. competitors, vs. budget]

## Assumptions & things to validate

- [bullet list of every unsourced assumption and how to validate it]

---

*Sources: [compact list of every source used].*

*These are planning estimates, not guarantees — validate with real-world tests before committing the full budget.*
```
