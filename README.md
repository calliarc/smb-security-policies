# SMB Security Policies

Ready-to-use security policy templates for small and mid-size businesses.

[![CI](https://github.com/calliarc/smb-security-policies/actions/workflows/ci.yml/badge.svg)](https://github.com/calliarc/smb-security-policies/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/calliarc/smb-security-policies?include_prereleases&sort=semver)](https://github.com/calliarc/smb-security-policies/releases)
[![Built by CalliArc](https://img.shields.io/badge/built%20by-CalliArc-0a66c2)](https://www.calliarc.com/)

> **Status:** v0.1.0, first release. Feedback and pull requests are welcome.

Plain-English templates written for organisations of roughly 10 to 250 people. Each policy has a purpose, scope, roles, numbered "must/should" policy statements, exceptions, enforcement, review cadence and a version table, plus practical extras such as checklists, a contact tree and forms. Company-specific details are `{{PLACEHOLDERS}}` that a small script fills in for you.

## Features

- Acceptable use policy
- Password and MFA policy
- Access control and onboarding/offboarding policy
- Incident response plan
- Backup and disaster recovery policy
- Vendor and third-party risk policy
- Mapping notes for common frameworks (SOC 2, ISO 27001, CIS Controls)

## Policies

| # | Policy | Highlights |
| --- | --- | --- |
| 01 | [Acceptable Use Policy](policies/01-acceptable-use.md) | Devices, software and SaaS, generative AI tools, email and payment-fraud checks, acknowledgement form |
| 02 | [Password and MFA Policy](policies/02-password-and-mfa.md) | Aligned with NIST SP 800-63B Rev. 4: length over complexity, no forced rotation, blocklists, phishing-resistant MFA for admins |
| 03 | [Access Control and Onboarding/Offboarding Policy](policies/03-access-control-and-onboarding-offboarding.md) | Least privilege, access reviews, joiner/mover/leaver checklists |
| 04 | [Incident Response Plan](policies/04-incident-response-plan.md) | Roles, four severity levels, contact tree, seven phases, communication templates, tabletop exercise |
| 05 | [Backup and Disaster Recovery Policy](policies/05-backup-and-disaster-recovery.md) | 3-2-1 with an immutable copy, RPO/RTO tier table, restore testing record |
| 06 | [Vendor and Third-Party Risk Policy](policies/06-vendor-and-third-party-risk.md) | Four-tier model, contract clauses, security questionnaire, assessment record |
| 07 | [Data Classification and Handling Policy](policies/07-data-classification-and-handling.md) | Four classification levels and a handling matrix |
| 08 | [Remote Work and BYOD Policy](policies/08-remote-work-byod.md) | Home and travel working, BYOD minimum requirements, privacy commitments, BYOD agreement |

Framework mapping: [frameworks/mapping.md](frameworks/mapping.md) maps each policy section to SOC 2 Trust Services Criteria, ISO/IEC 27001:2022 Annex A controls and CIS Controls v8 Safeguards, and lists what the templates do not cover.

## Tech stack

- Markdown
- Word/PDF export via Pandoc (optional)

## Getting started

### Requirements

- Python 3.9 or later
- [PyYAML](https://pypi.org/project/PyYAML/) (optional; a simple built-in parser is used if it is missing)
- [Pandoc](https://pandoc.org/installing.html) (optional) for Word export, plus a PDF engine such as a LaTeX distribution (`xelatex`/`pdflatex`), `wkhtmltopdf`, `weasyprint` or `typst` for PDF export

### 1. Get the templates

```sh
git clone https://github.com/calliarc/smb-security-policies.git
cd smb-security-policies
pip install -r requirements.txt   # optional
```

### 2. Add your company details

```sh
cp company.example.yml company.yml
```

Edit `company.yml`. Each key fills the matching placeholder in the templates, so `COMPANY_NAME: "Acme Ltd"` replaces every `{{COMPANY_NAME}}`. Use role titles rather than personal names where you can. To see every placeholder in use:

```sh
python3 scripts/build.py --list-placeholders
```

`company.yml` is listed in `.gitignore` so that internal contact details are not committed by accident. Remove that line if you want to keep it in your own private fork.

### 3. Build

```sh
python3 scripts/build.py --config company.yml --combined
# or: make build
```

Output goes to `dist/` (the folder is replaced on each run):

| Folder | Contents |
| --- | --- |
| `dist/md/` | Filled-in Markdown for each policy, plus `security-policy-handbook.md` when `--combined` is used |
| `dist/docx/` | Word documents (only if Pandoc is installed) |
| `dist/pdf/` | PDFs (only if Pandoc and a PDF engine are installed) |

Useful options:

| Option | Effect |
| --- | --- |
| `--formats md` | Markdown only (also `md,docx` or `md,docx,pdf`, the default) |
| `--strict` | Fail if any placeholder is missing or empty in your config |
| `--combined` | Also build a single handbook with every policy |
| `--out PATH` | Write somewhere other than `dist/` |

Without `--strict`, missing values are left as `{{PLACEHOLDER}}` and listed as a warning so you can find them. `TEMPLATE NOTE` comments at the top of each template are removed from the output.

### 4. Customise, approve and roll out

1. **Read every policy end to end.** Delete statements you will not actually follow; an unenforced policy is worse than none in an audit.
2. **Tune the numbers.** Timeframes (for example, "disable access within 24 hours"), review frequencies, retention periods and the RPO/RTO table are sensible defaults, not requirements.
3. **Fill in the tables** that need real data: the incident response contact tree (names and phone numbers), the backup system inventory, and the vendor inventory.
4. **Get approval** from leadership, and review with your legal, HR and compliance advisors (see the Disclaimer below).
5. **Publish and collect acknowledgements**, for example of the Acceptable Use Policy and BYOD agreement.
6. **Operate and evidence.** Keep records of access reviews, restore tests, tabletop exercises and vendor assessments. Auditors look for evidence, not just documents.
7. **Review at least annually** and update each policy's version history.

Tip: edit the templates in `policies/` in your own fork (keeping the placeholders), and rebuild whenever you change them. That keeps your policies in version control with a clear history.

## Development

```sh
make test   # unit tests for the build script
make lint   # markdownlint (needs Node.js)
make clean  # remove dist/
```

CI (GitHub Actions) runs markdownlint, a link check with [lychee](https://github.com/lycheeverse/lychee), the unit tests and a strict example build on every push and pull request. Lint rules are in `.markdownlint-cli2.jsonc` and link-check settings in `.lychee.toml`.

## Roadmap

- [x] Initial release
- [x] Documentation and examples
- [x] CI and automated tests

Have an idea? [Open an issue](https://github.com/calliarc/smb-security-policies/issues).

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

These templates are a starting point, not legal or compliance advice. Review and adapt them with your legal, HR and compliance advisors before adopting them.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

[MIT](LICENSE) © 2026 CalliArc

---

Built and maintained by [CalliArc](https://www.calliarc.com/). Need help with managed cybersecurity? [Talk to our team](https://www.calliarc.com/services/managed-cyber-security/).
