# Vendor and Third-Party Risk Policy

<!-- TEMPLATE NOTE: Keep the process proportionate. Most SMB vendors will be tier 3 or 4 and need little more than an inventory entry. Spend your effort on the few vendors in tier 1. Remove this comment before publishing. -->

| Field | Value |
| --- | --- |
| Policy owner | {{POLICY_OWNER}} |
| Approved by | {{EXECUTIVE_SPONSOR}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Classification | Internal |
| Review cadence | Annually |

## 1. Purpose

{{COMPANY_NAME}} relies on vendors for software, cloud hosting, IT support, payroll and much more. Their security problems can quickly become ours. This policy sets out a proportionate way to choose, contract with, monitor and exit vendors, based on how much risk each one carries.

## 2. Scope

This policy applies to any third party that:

- Stores, processes or can access {{COMPANY_NAME}} data (including SaaS and cloud providers).
- Has access to our systems, networks or offices (including managed service providers and contractors).
- Provides a service we depend on to operate.

It covers new vendors, renewals, and material changes to existing vendor relationships. It applies to free services and trials as well as paid ones.

## 3. Roles and responsibilities

| Role | Responsibilities |
| --- | --- |
| Business owner (requester) | Explains the need, provides information for tiering, owns the relationship, and requests reviews at renewal. |
| {{SECURITY_LEAD}} | Assigns the tier, reviews security evidence, records risk decisions, and owns this policy. |
| {{IT_PROVIDER}} | Assesses technical integration (SSO, MFA, data flows) and sets up and removes access. |
| Finance / procurement | Makes sure no purchase order or card payment is made for an unassessed vendor. |
| {{LEGAL_COUNSEL}} / {{PRIVACY_CONTACT}} | Reviews contracts, data processing terms, and cross-border data transfers. |
| {{EXECUTIVE_SPONSOR}} | Accepts high residual risk for tier 1 vendors. |

## 4. Policy statements

### 4.1 Inventory

1. {{COMPANY_NAME}} must keep a vendor inventory listing each vendor, business owner, service, data types involved, tier, contract end date, and date of last review.
2. The inventory must be reviewed at least annually and reconciled against finance records to catch vendors that were bought without review.

### 4.2 Tiering

1. Every vendor must be assigned a risk tier before contract signature, using the criteria in section 5.
2. The tier determines the due diligence, contract terms and review frequency required.

### 4.3 Due diligence

1. Due diligence must be completed and recorded before a vendor receives company data or access, according to the table in section 5.
2. Existing independent assurance (for example, a current SOC 2 Type II report, ISO/IEC 27001 certificate with a relevant scope, or equivalent) should be accepted in place of a questionnaire where it covers the services being used.
3. When reviewing a SOC 2 report, the reviewer should check its period and scope, note any exceptions, and confirm which "complementary user entity controls" {{COMPANY_NAME}} must operate.
4. Findings must be recorded along with a decision: approve, approve with conditions, or reject. Tier 1 vendors with significant unresolved gaps must be approved by {{EXECUTIVE_SPONSOR}}.

### 4.4 Contracts

Contracts for tier 1 and tier 2 vendors must, where applicable, include:

1. Confidentiality and data protection obligations, including a data processing agreement where personal data is processed.
2. A requirement to notify {{COMPANY_NAME}} of security incidents affecting our data without undue delay (target: within 72 hours or less).
3. Security requirements proportionate to the service (for example, MFA, encryption, vulnerability management).
4. Rules on the use of subcontractors (sub-processors), and notice of changes.
5. Data location and cross-border transfer terms.
6. Right to receive audit reports or other assurance evidence.
7. Return and deletion of data at the end of the contract.
8. Service levels, including availability and support response times, for services we depend on.

### 4.5 Access by vendors

1. Vendor staff must use individual, named accounts; shared vendor logins must not be used.
2. Vendor access must follow least privilege, be time-limited where possible, and be covered by MFA.
3. Remote access by vendors (including managed service providers' remote management tools) must be logged and reviewed.
4. Vendor access must be included in access reviews (see [Access Control and Onboarding/Offboarding Policy](03-access-control-and-onboarding-offboarding.md)).

### 4.6 Ongoing monitoring

1. Vendors must be reassessed on the schedule in section 5, and when there is a significant change in the service, data shared, or the vendor's ownership.
2. The business owner must report known vendor security incidents to {{SECURITY_LEAD}}, who will decide whether to invoke the [Incident Response Plan](04-incident-response-plan.md).
3. {{SECURITY_LEAD}} should subscribe to status and security notifications for tier 1 vendors.

### 4.7 Offboarding vendors

1. When a vendor relationship ends, the business owner must make sure that:
   1. All vendor accounts and integrations (API keys, OAuth apps, VPN access) are removed.
   2. Company data is returned or exported as needed.
   3. The vendor confirms deletion of company data in writing, where the contract requires it.
   4. The inventory is updated.

## 5. Vendor tiers

Assign the highest tier for which **any** criterion applies.

| Tier | Criteria | Due diligence before approval | Contract | Reassessment |
| --- | --- | --- | --- | --- |
| **1: Critical** | Processes Restricted data or large volumes of personal data; has administrative access to our environment (for example, an MSP); or the business cannot operate without it for more than a day. | Full questionnaire (section 6) **or** independent assurance report plus follow-up questions; SSO/MFA check; review of breach history. | All clauses in 4.4. | Annually |
| **2: High** | Processes Confidential data or limited personal data; integrates with core systems; or an outage would cause significant disruption. | Short questionnaire (questions marked **\*** in section 6) or independent assurance report. | All clauses in 4.4 that apply. | Every 2 years, or at renewal |
| **3: Moderate** | Handles Internal data only; limited integration; easily replaced. | Check public security page / trust centre; confirm MFA is available and enabled. | Standard terms reviewed for confidentiality and data deletion. | At renewal |
| **4: Low** | No company data beyond basic contact details; no system access. | Inventory entry only. | Standard terms. | None, unless use changes |

## 6. Security questionnaire

Send to tier 1 vendors (all questions) and tier 2 vendors (questions marked **\***). Accept existing documentation where it answers the question.

### 6.1 Governance and assurance

1. **\*** Do you hold a current independent security attestation or certification (for example, SOC 2 Type II, ISO/IEC 27001)? Please share the report or certificate and its scope.
2. **\*** Who is responsible for information security in your organisation?
3. Do you have written information security policies that are reviewed at least annually?
4. Do your staff complete security awareness training at least annually, and are background checks performed where lawful?

### 6.2 Data protection

1. **\*** What types of our data will you store or process, and in which countries?
2. **\*** Is our data encrypted in transit and at rest? Who manages the keys?
3. Is our data logically separated from other customers' data?
4. **\*** Which subcontractors or sub-processors will have access to our data?
5. How long do you keep our data, and how is it deleted at the end of the contract?

### 6.3 Access and identity

1. **\*** Does your service support SSO (SAML or OpenID Connect) and MFA for our users?
2. **\*** Is MFA required for all of your staff who can access customer data or production systems?
3. How is privileged access in your environment granted, reviewed and removed?

### 6.4 Operations

1. How do you find and fix vulnerabilities? What are your patching timelines for critical issues?
2. Do you perform independent penetration tests at least annually? Can you share a summary?
3. What security logs do you keep, for how long, and can we access logs relating to our account?
4. **\*** How do you back up our data, and how often do you test restores?
5. What are your RPO and RTO for the service we use?

### 6.5 Incident response

1. **\*** Do you have a documented incident response process?
2. **\*** How quickly will you notify us of a security incident affecting our data, and how?
3. Have you had a security incident affecting customer data in the last 3 years? If so, what changed afterwards?

### 6.6 Assessment record

```text
Vendor:                         Tier:
Business owner:                 Reviewer:
Service / data involved:
Evidence received:              (report, certificate, questionnaire, trust centre)
Evidence date/period:
Key findings and gaps:
Complementary controls we must operate:
Decision:                       Approve / Approve with conditions / Reject
Conditions and owners:
Risk accepted by (tier 1 only):
Next review date:
```

## 7. Exceptions

Urgent purchases without completed due diligence may be approved by {{SECURITY_LEAD}} for up to 30 days, provided no Restricted data is shared during that period. All other exceptions must be documented with the risk, compensating controls and an end date, and approved by {{SECURITY_LEAD}} (tiers 2 to 4) or {{EXECUTIVE_SPONSOR}} (tier 1).

## 8. Enforcement

Buying or using services that handle company data without following this policy may lead to the service being blocked and to disciplinary action. Finance will not pay invoices for tier 1 or tier 2 vendors that are not in the inventory.

## 9. Review cadence

{{POLICY_OWNER}} reviews this policy at least annually and after any significant vendor-related incident.

## 10. Related documents

- [Access Control and Onboarding/Offboarding Policy](03-access-control-and-onboarding-offboarding.md)
- [Incident Response Plan](04-incident-response-plan.md)
- [Data Classification and Handling Policy](07-data-classification-and-handling.md)
- [Backup and Disaster Recovery Policy](05-backup-and-disaster-recovery.md)

## Version history

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 1.0 | {{EFFECTIVE_DATE}} | {{POLICY_OWNER}} | Initial version, adapted from the CalliArc SMB Security Policies template v0.1.0 |
