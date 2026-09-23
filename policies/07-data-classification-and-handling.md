# Data Classification and Handling Policy

<!-- TEMPLATE NOTE: Four levels work for most SMBs. If you want fewer, merge Confidential and Restricted, but keep the handling rules for the most sensitive data. Remove this comment before publishing. -->

| Field | Value |
| --- | --- |
| Policy owner | {{POLICY_OWNER}} |
| Approved by | {{EXECUTIVE_SPONSOR}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Classification | Internal |
| Review cadence | Annually |

## 1. Purpose

Not all information needs the same protection. This policy gives everyone at {{COMPANY_NAME}} a simple way to decide how sensitive information is, and clear rules for storing, sharing and disposing of it. Protecting the right things well is better than protecting everything poorly.

## 2. Scope

This policy applies to all information created, received or held by {{COMPANY_NAME}}, in any form (digital files, databases, email, chat, paper, recordings), and to everyone who handles it, including contractors and vendors.

## 3. Roles and responsibilities

| Role | Responsibilities |
| --- | --- |
| Data owner (usually a department head) | Decides the classification of data sets in their area, approves access, and sets retention. |
| All users | Classify information they create, handle it according to this policy, and ask when unsure. |
| {{IT_PROVIDER}} | Provides tools that support the handling rules (encryption, sharing controls, labels, secure deletion). |
| {{SECURITY_LEAD}} | Owns this policy and advises on classification questions. |
| {{PRIVACY_CONTACT}} | Advises on personal data and privacy law requirements. |

## 4. Classification levels

| Level | Definition | Impact if disclosed | Examples |
| --- | --- | --- | --- |
| **Public** | Approved for anyone to see. | None. | Published website content, marketing brochures, job adverts, press releases. |
| **Internal** | For use inside {{COMPANY_NAME}}. The default for anything not otherwise classified. | Minor embarrassment or inconvenience. | Internal announcements, org charts, most policies, meeting notes without sensitive content. |
| **Confidential** | Sensitive business or personal information limited to people who need it. | Real harm to the company, customers or staff; possible contract breach. | Customer lists, contracts, pricing, financial reports, employee records, most personal data, non-public product plans, source code. |
| **Restricted** | The most sensitive information, limited to named individuals. | Serious harm; likely legal or regulatory consequences; direct financial loss. | Payment card data, bank account credentials, government ID numbers, health information, passwords and encryption keys, M&A plans, security vulnerability details. |

## 5. Policy statements

### 5.1 Classifying information

1. Information must be treated as **Internal** unless it has been classified otherwise.
2. The creator or data owner must assign a higher classification when the content warrants it.
3. When information from different levels is combined, the combined result must be treated at the highest level.
4. Classifications should be reviewed when information changes or is published (for example, a product plan becomes Public at launch).
5. Confidential and Restricted documents should be labelled, using a document label, header/footer, or the labelling feature of {{FILE_STORAGE}} where available.

### 5.2 Handling rules

| Activity | Public | Internal | Confidential | Restricted |
| --- | --- | --- | --- | --- |
| **Storage** | Anywhere approved | Approved company storage | Approved company storage with access limited to groups that need it | Approved storage designated for Restricted data, access limited to named people; encrypted at rest |
| **Company devices** | Allowed | Allowed | Allowed on encrypted, managed devices | Only if necessary; encrypted, managed devices; avoid local copies |
| **Personal devices** | Allowed | Through approved apps only | Through approved apps only; no download | Not allowed unless an exception is approved |
| **Sharing internally** | No restriction | No restriction | Need-to-know; share links to named people or groups, not "anyone with the link" | Named individuals only, approved by the data owner |
| **Sharing externally** | No restriction | With a business need | Business need, confidentiality agreement or contract in place, and sent securely | Data owner approval; encrypted; contract in place; logged |
| **Email** | Allowed | Allowed | Allowed to approved recipients; check addresses carefully; use encryption for external recipients where available | Do not send in the body of email; use an encrypted sharing method |
| **Removable media** | Allowed | Avoid | Encrypted, approved media only | Not allowed unless an exception is approved |
| **AI tools** | Allowed | Approved tools only | Tools approved for Confidential data only | Tools approved for Restricted data only (usually none) |
| **Printing** | Allowed | Collect promptly | Collect immediately; do not leave on desks | Avoid; if necessary, secure print and lock away |
| **Disposal** | Normal | Normal deletion; recycle paper | Secure deletion; cross-cut shred or secure bin | Secure deletion with verification; cross-cut shred; media destroyed with certificate |

### 5.3 Personal data

1. Personal data must be handled as at least **Confidential**. Special categories (such as health, biometric, or government ID data) and financial account data must be handled as **Restricted**.
2. Personal data must only be collected and used for a defined purpose, limited to what is needed, and kept no longer than necessary.
3. Requests from individuals about their personal data (for example, access or deletion requests) must be passed to {{PRIVACY_CONTACT}} promptly.

### 5.4 Encryption

1. Laptops, desktops and mobile devices that access Internal or higher data must use full-disk encryption.
2. Confidential and Restricted data must be encrypted in transit (for example, TLS 1.2 or higher) whenever it leaves a company system.
3. Restricted data must be encrypted at rest.
4. Encryption keys and secrets must be stored in an approved secrets manager or password manager, never in code, tickets, chat or documents.

### 5.5 Clear desk and clear screen

1. Confidential and Restricted paper documents must be locked away when not in use.
2. Screens must be locked when unattended, and users should take care that Confidential information is not visible to others, for example in public places or on video calls.

### 5.6 Retention and disposal

1. Information must be kept according to {{COMPANY_NAME}}'s retention schedule, legal requirements, and contracts, and securely disposed of when no longer needed.
2. Deletion must be suspended for information subject to a legal hold, when instructed by {{LEGAL_COUNSEL}}.
3. Devices and storage media must be wiped using a method appropriate to the media, or physically destroyed, before disposal, reuse or return to a leasing company. Records of disposal must be kept for Restricted data.

### 5.7 Mistakes and data loss

1. If Confidential or Restricted information is sent to the wrong person, shared publicly, or lost, users must report it immediately to {{SECURITY_EMAIL}}. It will be handled under the [Incident Response Plan](04-incident-response-plan.md).

## 6. Exceptions

Exceptions must be requested from {{SECURITY_LEAD}} with the data owner's support, and must describe the information, the reason, compensating controls and an end date. Exceptions are reviewed at least every 12 months.

## 7. Enforcement

Mishandling Confidential or Restricted information may lead to removal of access and disciplinary action. Where possible, handling rules are supported by technical controls such as sharing restrictions, data loss prevention and device encryption.

## 8. Review cadence

{{POLICY_OWNER}} reviews this policy at least annually, and after any significant data-related incident or change in privacy law affecting {{COMPANY_NAME}}.

## 9. Related documents

- [Acceptable Use Policy](01-acceptable-use.md)
- [Remote Work and BYOD Policy](08-remote-work-byod.md)
- [Backup and Disaster Recovery Policy](05-backup-and-disaster-recovery.md)
- [Vendor and Third-Party Risk Policy](06-vendor-and-third-party-risk.md)

## Version history

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 1.0 | {{EFFECTIVE_DATE}} | {{POLICY_OWNER}} | Initial version, adapted from the CalliArc SMB Security Policies template v0.1.0 |
