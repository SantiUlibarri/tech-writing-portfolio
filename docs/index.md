---
hide:
  - navigation
  - toc
---

# Santiago Fernández Ulibarri

**Technical Writer: API, integration, and platform documentation**<br>
Madrid, Spain · English & Spanish (C2) · [LinkedIn](https://www.linkedin.com/in/santiulibarri) · [GitHub](https://github.com/SantiUlibarri)

I turn complex engineering and product systems into clear, testable, self-service documentation. I've led documentation used by 35,000+ internal users at Oracle and built a documentation function from scratch at Proscai, a retail ERP and integration platform.

This site is itself a sample of how I work: written in Markdown, version-controlled in Git, reviewed through pull requests, and published automatically with MkDocs and GitHub Actions.

## Documentation samples

<div class="grid cards" markdown>

-   **Payments API (Paylark)**

    ---

    A complete payment API sample: OpenAPI 3.1 spec, interactive reference, Postman collection tested against a mock server, quickstart, and payment-status guide.

    [Explore the Payments API →](paylark/index.md)
    
-   **API documentation**

    ---

    Concepts and endpoint reference for a subset of the GitHub REST API: authentication, errors, pagination, and rate limits.

    [Read the API docs →](api/github-api/README.md)

-   **Integration guides**

    ---

    End-to-end documentation for an ERP ↔ Clover POS integration: overview, customer journey, implementation steps, and troubleshooting.

    [Read the integration guides →](implementation/README.md)

-   **Release notes**

    ---

    Release notes single-sourced as structured JSON for machines and Markdown for people.

    [Read the release notes →](release-notes/README.md)

-   **Security procedures**

    ---

    A customer-facing security update, a request guide, and an internal SOP for root key rotation, each written for a different audience.

    [Read the security docs →](security/README.md)

-   **Platform & operations**

    ---

    Ubuntu command-line workflows, managing systemd services, and troubleshooting common Linux errors.

    [Read the platform docs →](linux/README.md)

</div>

## How this site is built

| Layer | Tooling |
|---|---|
| Authoring | Markdown |
| Version control and review | Git, GitHub branches and pull requests |
| Site generator | MkDocs with the Material theme |
| Publishing | GitHub Actions → GitHub Pages, on every merge to `main` |