# llm-skills

A collection of custom skills for Claude agents, ready to install at [claude.ai](https://claude.ai) via Cowork Settings.

## Skills

### [app-marketing-analysis](app-marketing-analysis/)

Run a full market & marketing analysis for an iOS app idea and deliver a decision-ready report as both a Markdown file and a styled PDF.

**Covers:** market size (TAM/SAM/SOM) · competitor research · risk assessment · feature review · go-to-market strategy · budget planning · 3-scenario revenue projection

**Use when:** a user shares an app idea or concept brief and asks for any of — market research, marketing analysis, competitor research, a go-to-market plan, a marketing budget, or revenue projections.

---

## Packaging a skill

Each skill lives in its own folder and must contain a `SKILL.md` at the root. To turn a skill folder into an installable `.skill` file, zip the folder from **inside** the repo root:

```bash
zip -r app-marketing-analysis.skill app-marketing-analysis/
```

The resulting `.skill` file bundles all references, scripts, and assets alongside the `SKILL.md` manifest. Keep the folder name and the `.skill` filename identical — Claude uses the folder structure at install time.

> **Tip:** exclude macOS metadata so the archive stays clean:
> ```bash
> zip -r app-marketing-analysis.skill app-marketing-analysis/ -x "*.DS_Store" -x "__MACOSX/*"
> ```

---

## Installing a skill at Claude.ai

1. Go to **claude.ai → Settings → Cowork** (or open **claude.ai/cowork**).
2. Click **Add skill** (or the `+` button in the Skills panel).
3. Upload the `.skill` file you packaged above.
4. The skill is now available in any Cowork session — invoke it by name or trigger phrase.

---

## Skill folder structure

```
<skill-name>/
├── SKILL.md          # Required. Name, description, and full agent instructions.
├── references/       # Optional. Markdown guides the agent can read at runtime.
├── scripts/          # Optional. Helper scripts the agent can execute.
└── assets/           # Optional. Images, templates, or other static files.
```

The only required file is `SKILL.md`. Its front matter must include at minimum:

```markdown
---
name: your-skill-name
description: One-sentence summary shown in the Skills panel and used for trigger matching.
---

# Skill title
...instructions...
```
