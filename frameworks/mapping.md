# Framework Mapping Notes

This page maps each section of the policy templates to three commonly requested frameworks:

- **SOC 2**: AICPA 2017 Trust Services Criteria (with revised points of focus, 2022). Mostly Common Criteria (CC-series), plus Availability (A-series) and Confidentiality (C-series) where relevant.
- **ISO/IEC 27001:2022**: Annex A control IDs (these correspond to the controls described in ISO/IEC 27002:2022).
- **CIS Controls v8**: Safeguard IDs (for example, 6.3). Where only a Control as a whole applies, the Control number is given (for example, "Control 3").

## How to read and use this mapping

- The mapping shows where a policy section **supports** a control. It does not mean the control is fully met. Most controls also need evidence that you are operating the policy: tickets, logs, review records, training completions and so on.
- Where no specific ID is a good fit, the cell says "—" rather than forcing a match. Where only a broad relationship exists, the mapping is given at Control or category level.
- The frameworks are revised from time to time (for example, CIS Controls v8.1 refined some Safeguard wording). Check the current official documents before relying on this for an audit, and involve your auditor or assessor early.
- Section numbers refer to the templates in [`policies/`](../policies/). If you renumber sections, update this file.

## 1. Acceptable Use Policy

[01-acceptable-use.md](../policies/01-acceptable-use.md)

| Section | SOC 2 TSC | ISO 27001:2022 Annex A | CIS Controls v8 |
| --- | --- | --- | --- |
| 4.1 General principles, acknowledgement | CC1.1, CC2.2, CC5.3 | 5.1, 5.10, 6.2 | 14.1 |
| 4.2 Accounts and credentials | CC6.1 | 5.17 | 5.2, 14.3 |
| 4.3 Devices | CC6.1, CC6.8 | 7.7, 7.9, 8.1 | 4.3, 7.3, 10.1 |
| 4.4 Software and cloud services | CC6.8 | 5.23, 8.19 | 2.1, 2.3 |
| 4.5 Generative AI tools | CC2.2, CC6.7 | 5.10, 5.14 | Control 3 |
| 4.6 Email, messaging and the web | CC2.2, CC6.8 | 5.14, 6.3, 8.23 | Control 9, 14.2 |
| 4.7 Data handling | CC6.7, C1.1 | 5.10, 7.10 | 3.9, 14.4 |
| 4.8 Networks | CC6.6 | 6.7, 8.20 | 12.7 |
| 4.9 Prohibited activities | CC1.1, CC6.1 | 5.10, 5.32 | — |
| 4.10 Reporting | CC2.2, CC7.3 | 6.8 | 14.6, 17.3 |
| 4.11 Leaving the company | CC6.2, CC6.5 | 5.11, 6.5 | 6.2 |
| 6 Enforcement | CC1.5 | 6.4 | — |

## 2. Password and MFA Policy

[02-password-and-mfa.md](../policies/02-password-and-mfa.md)

| Section | SOC 2 TSC | ISO 27001:2022 Annex A | CIS Controls v8 |
| --- | --- | --- | --- |
| 4.1 Single sign-on first | CC6.1 | 5.16, 8.5 | 5.6, 6.7 |
| 4.2 Password requirements | CC6.1 | 5.17, 8.5 | 5.2 |
| 4.3 Using and protecting passwords | CC6.1 | 5.17 | 5.2, 14.3 |
| 4.4 Multi-factor authentication | CC6.1, CC6.6 | 8.5 | 6.3, 6.4, 6.5 |
| 4.5 Privileged, service and break-glass accounts | CC6.1, CC6.3 | 5.17, 8.2 | 4.7, 5.4, 5.5 |
| 4.6 Resets and recovery | CC6.1, CC6.2 | 5.17 | — |
| 4.7 Suspected compromise | CC7.2, CC7.4 | 5.17, 5.26 | — |

## 3. Access Control and Onboarding/Offboarding Policy

[03-access-control-and-onboarding-offboarding.md](../policies/03-access-control-and-onboarding-offboarding.md)

| Section | SOC 2 TSC | ISO 27001:2022 Annex A | CIS Controls v8 |
| --- | --- | --- | --- |
| 4.1 Principles (least privilege, RBAC, segregation) | CC6.1, CC6.3 | 5.3, 5.15, 8.3 | 3.3, 6.8 |
| 4.2 Requesting and approving access | CC6.2, CC6.3 | 5.18 | 6.1 |
| 4.3 Privileged access | CC6.1, CC6.3 | 8.2, 8.15 | 5.4, 6.5, 8.2 |
| 4.4 Onboarding | CC1.4, CC6.2 | 5.16, 6.1, 6.2, 6.3 | 5.1, 6.1, 14.1 |
| 4.5 Role changes | CC6.2, CC6.3 | 5.18 | 6.1, 6.2 |
| 4.6 Offboarding | CC6.2, CC6.3, CC6.5 | 5.11, 5.18, 6.5 | 6.2 |
| 4.7 Access reviews | CC6.2, CC6.3 | 5.18 | 5.1 |
| 4.8 Dormant accounts | CC6.2 | 5.18 | 5.3 |
| 4.9 Third-party and contractor access | CC6.2, CC9.2 | 5.18, 5.19 | 6.1, 6.2 |
| 4.10 Physical access | CC6.4 | 7.1, 7.2 | — (CIS v8 does not cover physical security) |
| 5 Checklists | As for 4.4 to 4.6 | As for 4.4 to 4.6 | As for 4.4 to 4.6 |

## 4. Incident Response Plan

[04-incident-response-plan.md](../policies/04-incident-response-plan.md)

| Section | SOC 2 TSC | ISO 27001:2022 Annex A | CIS Controls v8 |
| --- | --- | --- | --- |
| 4 Roles and responsibilities | CC7.4 | 5.2, 5.24 | 17.1, 17.5 |
| 5 Severity levels | CC7.3 | 5.25 | 17.9 |
| 6 Contact tree | CC2.3, CC7.4 | 5.5, 5.24 | 17.2, 17.6 |
| 7 Phase 1: Prepare | CC7.2, CC7.4 | 5.24, 8.15 | 8.2, 17.4 |
| 7 Phase 2: Detect and triage | CC7.2, CC7.3 | 5.25, 6.8 | 17.3 |
| 7 Phases 3 and 4: Contain, eradicate | CC7.4 | 5.26 | 17.4 |
| 7 Phase 5: Recover | CC7.5 | 5.26, 5.29 | 17.4 |
| 7 Phase 6: Notify | CC2.3, CC7.4 | 5.5, 5.26, 5.31, 5.34 | 17.2 |
| 7 Phase 7: Learn | CC7.5 | 5.27 | 17.8 |
| 8 Evidence and records | CC7.4 | 5.28 | — |
| 9 Templates | CC7.4 | 5.24 | 17.4 |
| 10 Tabletop exercise | CC7.4 | 5.24 | 17.7 |

## 5. Backup and Disaster Recovery Policy

[05-backup-and-disaster-recovery.md](../policies/05-backup-and-disaster-recovery.md)

| Section | SOC 2 TSC | ISO 27001:2022 Annex A | CIS Controls v8 |
| --- | --- | --- | --- |
| 4.1 Backup coverage and inventory | A1.2, CC9.1 | 5.9, 8.13 | 11.1, 11.2 |
| 4.2 The 3-2-1 rule | A1.2 | 8.13 | 11.2, 11.4 |
| 4.3 Protecting backups | A1.2, CC6.1 | 8.13, 8.24 | 11.3 |
| 4.4 Frequency and retention | A1.2 | 5.33, 8.13 | 3.4, 11.2 |
| 4.5 Monitoring | A1.2 | 8.13 | 11.2 |
| 4.6 Testing | A1.3 | 5.30, 8.13 | 11.5 |
| 4.7 Disaster recovery | A1.2, A1.3, CC7.5, CC9.1 | 5.29, 5.30 | 11.1 |
| 5 Recovery objectives (RPO/RTO) | A1.2, CC9.1 | 5.30 | 11.1 |

## 6. Vendor and Third-Party Risk Policy

[06-vendor-and-third-party-risk.md](../policies/06-vendor-and-third-party-risk.md)

| Section | SOC 2 TSC | ISO 27001:2022 Annex A | CIS Controls v8 |
| --- | --- | --- | --- |
| Policy as a whole | CC9.2 | 5.19 | 15.2 |
| 4.1 Inventory | CC9.2 | 5.19 | 15.1 |
| 4.2 Tiering and 5 Vendor tiers | CC9.2 | 5.19, 5.21 | 15.3 |
| 4.3 Due diligence and 6 Questionnaire | CC9.2 | 5.19, 5.21, 5.23 | 15.5 |
| 4.4 Contracts | CC9.2 | 5.20 | 15.4 |
| 4.5 Access by vendors | CC6.1, CC6.2, CC9.2 | 5.18, 5.19 | 6.1, 6.2 |
| 4.6 Ongoing monitoring | CC9.2 | 5.22 | 15.6 |
| 4.7 Offboarding vendors | CC6.2, CC9.2 | 5.20, 5.22 | 15.7 |

## 7. Data Classification and Handling Policy

[07-data-classification-and-handling.md](../policies/07-data-classification-and-handling.md)

| Section | SOC 2 TSC | ISO 27001:2022 Annex A | CIS Controls v8 |
| --- | --- | --- | --- |
| 4 Classification levels | C1.1 | 5.12 | 3.7 |
| 5.1 Classifying and labelling | C1.1 | 5.12, 5.13 | 3.7 |
| 5.2 Handling rules | C1.1, CC6.1, CC6.7 | 5.10, 5.14, 7.10 | 3.3, 3.9, 14.4 |
| 5.3 Personal data | C1.1 (and the Privacy criteria, P-series, if in scope) | 5.34 | 3.1 |
| 5.4 Encryption | CC6.1, CC6.7 | 8.24 | 3.6, 3.10, 3.11 |
| 5.5 Clear desk and clear screen | — | 7.7 | 4.3 |
| 5.6 Retention and disposal | C1.2, CC6.5 | 5.33, 7.14, 8.10 | 3.4, 3.5 |
| 5.7 Mistakes and data loss | CC7.3 | 6.8 | 17.3 |

## 8. Remote Work and BYOD Policy

[08-remote-work-byod.md](../policies/08-remote-work-byod.md)

| Section | SOC 2 TSC | ISO 27001:2022 Annex A | CIS Controls v8 |
| --- | --- | --- | --- |
| 4.1 Working remotely | CC6.6, CC6.7 | 6.7, 7.9 | 12.7 |
| 4.2 Travel | CC6.7 | 6.7, 7.9 | — |
| 4.3 BYOD eligibility | CC6.1, CC6.8 | 6.7, 8.1 | — |
| 4.4 BYOD minimum requirements | CC6.1, CC6.8 | 8.1 | 3.6, 4.3, 4.10, 4.12 |
| 4.5 What the company can and cannot do | CC6.1 | 5.34, 8.1 | 4.11, 4.12 |
| 4.6 Separation of data | CC6.7 | 8.1 | 4.12 |
| 4.7 Loss, theft and leaving | CC6.5, CC7.3 | 5.11, 6.8, 8.1 | 4.11 |
| 5 BYOD agreement | CC2.2 | 6.2, 8.1 | — |

## 9. Common sections in every policy

| Section | SOC 2 TSC | ISO 27001:2022 Annex A | CIS Controls v8 |
| --- | --- | --- | --- |
| Policy document, approval and communication | CC2.2, CC5.3 | 5.1 | — |
| Roles and responsibilities | CC1.3, CC1.5 | 5.2, 5.4 | — |
| Exceptions | CC5.3 | 5.36 | — |
| Enforcement | CC1.5 | 5.36, 6.4 | — |
| Review cadence and version history | CC5.3 | 5.1 | — |

## 10. What these templates do not cover

These templates are a foundation, not a complete security programme. Areas you will likely need to address separately include:

| Area | SOC 2 TSC | ISO 27001:2022 | CIS Controls v8 |
| --- | --- | --- | --- |
| Risk assessment and risk treatment | CC3.1 to CC3.4, CC9.1 | Clauses 6.1, 8.2, 8.3 | — |
| ISMS management system requirements (scope, internal audit, management review) | CC4.1, CC4.2 | Clauses 4 to 10 | — |
| Asset and software inventory | CC6.1 | 5.9 | Controls 1 and 2 |
| Secure configuration and hardening | CC7.1 | 8.9 | Control 4 |
| Vulnerability and patch management | CC7.1 | 8.8 | Control 7 |
| Logging and monitoring | CC7.2 | 8.15, 8.16, 8.17 | Controls 8 and 13 |
| Network security | CC6.6 | 8.20 to 8.22 | Controls 12 and 13 |
| Change management | CC8.1 | 8.32 | — |
| Secure software development | CC8.1 | 8.25 to 8.31 | Control 16 |
| Penetration testing | CC4.1 | 8.8 | Control 18 |
| Physical and environmental security (beyond access) | CC6.4, A1.2 | 7.1 to 7.14 | — |
| Security awareness programme (content and schedule) | CC1.4, CC2.2 | 6.3 | Control 14 |
| Business continuity (beyond IT recovery) | CC9.1, A1.2 | 5.29, 5.30 | — |

Contributions that extend the templates into these areas are welcome. See [CONTRIBUTING.md](../CONTRIBUTING.md).
