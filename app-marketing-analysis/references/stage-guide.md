# Stage guide

Detailed instructions per stage. Benchmarks cited here were current as of mid-2026 — treat them as starting points and re-verify with a quick search; the sources publish annual updates.

## Stage 1 — Intake & framing

Confirm the app in 1–2 sentences (forces shared understanding before any numbers). Then lock:

- **Target geography** — global / specific country / specific App Store markets. US-first is the common default: cleanest data, highest ARPU.
- **Monetization model & price** — paid, subscription, freemium+IAP, ads, hybrid. If the user hasn't decided, offer to recommend one after competitor research (Stage 3) rather than guessing.
- **Goals & constraints** — budget ceiling, revenue target, launch date.

Ask via multiple-choice options where possible, with a recommended default marked. Don't proceed until all three are explicit.

## Stage 2 — Market size

**Top-down:** start from a sourced population figure and narrow. For US iOS: ~150–160M US iPhone users (Demandsage, BankMyCell — re-verify), ~57% of US smartphones. Then apply behavior filters (what % of those people exhibit the behavior the app serves — find survey data) and an adoption filter for SAM (what % would adopt a dedicated tool — usually a first-principles assumption; label it).

**Bottom-up sanity check:** budget ÷ realistic CPI → installs; installs × category conversion → payers; payers × price → revenue. If top-down and bottom-up tell wildly different stories, say which constraint binds (usually budget, not market).

**Output table:** TAM / SAM / SOM, each with estimate range + method + which parts are sourced vs. assumed. State the binding constraint explicitly.

## Stage 3 — Competitors

Search the App Store for the obvious queries a user would type. Fetch competitor App Store pages directly — the page contains pricing (In-App Purchases section in Information), last-update date (Version History — a 2-year-old "What's New" means abandoned), and whether the app has enough ratings to display a score (no score = no traction; this is a strong signal in shovelware categories).

Always include **indirect competitors**: general LLMs (ChatGPT/Claude/Gemini free tiers absorb many "generate text" use cases), free web tools, and the status quo of doing nothing. In many categories the indirect competitor is the real one — say so when true.

Watch for the **empty-category signal**: if no direct competitor has traction, that's either an open gap or evidence of weak willingness to pay. Present both readings and carry the second into Stage 4 as a risk.

**Output:** comparison table (competitor / strengths / pricing / weaknesses) + one-line positioning opportunity + a pricing read (where the user's price sits vs. the field).

## Stage 4 — Risks

Cover six categories: market, product, competitive, go-to-market, monetization, platform/App Store/regulatory. For each risk: severity (High/Med/Low) + a concrete mitigation, ordered by severity. Look for a shared root cause across the top risks — naming it usually points to the single cheapest validation experiment (e.g., a fake-door willingness-to-pay test: a landing page with real pricing and a "start trial" button that collects emails, run on a few hundred dollars of ads — behavior beats survey answers).

## Stage 5 — Feature review

Review the brief's feature list strictly through a market/competitive lens:

- **Cut** — features that don't drive adoption or differentiation (cost without market payoff).
- **Add** — table stakes competitors already ship (launching behind the only competitor on a key feature is a named risk), conversion mechanics (e.g., trial-first paywall — trials substantially outconvert pure freemium per RevenueCat), and retention mechanisms if the usage frequency is low.
- **Keep for MVP** — the smallest most *marketable* version. Distinguish features that drive installs (visible in an ad/screenshot) from features that drive completion/retention (invisible until use) — a differentiator users can't perceive before install shouldn't lead marketing.

Every recommendation needs a market reason attached. "Nice UX" is not a market reason.

## Stage 6 — Go-to-market

Assess channels honestly against budget: ASO, Apple Search Ads, paid social, short-form video (organic + paid), influencers, content/SEO, communities/referrals. Small budgets (<$25k) almost always force organic-first with paid amplification of proven creative.

Name **one** most promising source and defend it (format fit, persona fit, budget fit). Outline the campaign: a core hook in the user's voice (the pain, not the technology) and pre-launch / launch / growth phases with concrete actions. Define metrics with target numbers, not just metric names: CPI, install→trial, trial→paid, CAC per payer, D30 retention, plus a product-specific leading indicator.

## Stage 7 — Budget

Channel × phase table summing exactly to the ceiling, including a **reserve line** (~15%) to reallocate to winners. Recommend a small **starting spend** gated on a validation result, not the full budget on day one. State the scaling rule numerically: CAC per paying subscriber ≤ ⅓ of first-year LTV is a sane default; compute what that means in dollars for this app, and check whether cold paid installs can ever clear the bar at category CPI/conversion rates (often they can't — which justifies the organic-first structure).

## Stage 8 — Revenue projection

12-month bottom-up, cash basis: installs → install→paying % → payers → blended revenue/payer → minus store commission (15% under Apple's small-business program, 30% above $1M).

Benchmark starting points (re-verify; RevenueCat publishes annually):
- Freemium download→paid median ≈ 2% by day 35; hard paywall ≈ 10%+; trial-based much higher per-trial.
- CPI: Apple Search Ads ≈ $1.4, TikTok ≈ $2.9, Instagram ≈ $3.5, Facebook ≈ $3.8 (Business of Apps / Mapendo).

Present conservative / base / optimistic with the assumption table shown. Identify the widest-variance assumption by name. Sanity-check three ways: vs. SAM (% captured should be tiny), vs. competitors (does the base case imply implausible category leadership?), vs. budget (does revenue cover spend? If year 1 is really a validation year, say so and define the actual win condition).

## Stage 9 — Final report

Consolidate per `references/report-template.md`, then build both files as described in SKILL.md. The summary paragraph should contain: the opportunity in one clause, the headline numbers, and the single recommended next move with its gate condition.
