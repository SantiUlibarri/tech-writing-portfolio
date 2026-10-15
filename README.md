# Technical Writing Portfolio: Santiago Fernández Ulibarri

[![Build and deploy docs](https://github.com/SantiUlibarri/tech-writing-portfolio/actions/workflows/docs.yml/badge.svg)](https://github.com/SantiUlibarri/tech-writing-portfolio/actions/workflows/docs.yml)

**📖 Live site: https://santiulibarri.github.io/tech-writing-portfolio/**

Bilingual (English/Spanish, C2) technical writer specializing in API, integration, and platform documentation. I've led documentation used by 35,000+ internal users at Oracle and built a documentation function from scratch at Proscai, a retail ERP and integration platform.

This repository is the source for my portfolio site. The site itself is a working example of a docs-as-code workflow: Markdown in Git, pull-request review, automated builds, and continuous deployment.

## What's inside

| Section | Source | Contents |
|---|---|---|
| API documentation | [`docs/api/`](docs/api/github-api/) | GitHub REST API concepts and endpoint reference |
| Integration guides | [`docs/implementation/`](docs/implementation/) | ERP ↔ Clover POS implementation and troubleshooting |
| Release notes | [`docs/release-notes/`](docs/release-notes/) | Single-sourced JSON and Markdown release notes |
| Security | [`docs/security/`](docs/security/) | Customer-facing update, request guide, internal SOP |
| Platform & operations | [`docs/linux/`](docs/linux/) | Ubuntu CLI, systemd, troubleshooting |

## Build the site locally

Requires Python 3.

```bash
git clone https://github.com/SantiUlibarri/tech-writing-portfolio.git
cd tech-writing-portfolio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000/tech-writing-portfolio/.

## How changes are published

1. Changes are made on a branch and opened as a pull request.
2. GitHub Actions builds the site with `mkdocs build --strict`. Any warning, such as a broken link, fails the check.
3. Merging to `main` builds the site again and deploys it to GitHub Pages.

Workflow file: [`.github/workflows/docs.yml`](.github/workflows/docs.yml)

## Tools and skills demonstrated

- **Docs-as-code:** Markdown, Git, GitHub pull requests, GitHub Actions, MkDocs Material
- **API documentation:** REST concepts, authentication, error handling, pagination, rate limits
- **Content types:** concepts, task guides, reference, troubleshooting, release notes, SOPs
- **Collaboration:** Jira, Confluence, Agile/Scrum

## Contact

[LinkedIn](https://www.linkedin.com/in/santiulibarri) · Madrid, Spain