# Access Control and Onboarding/Offboarding Policy

<!-- TEMPLATE NOTE: Adjust the timeframes (for example, "within 4 hours") to what your team can reliably achieve, then keep to them. Remove this comment before publishing. -->

| Field | Value |
| --- | --- |
| Policy owner | {{POLICY_OWNER}} |
| Approved by | {{EXECUTIVE_SPONSOR}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Classification | Internal |
| Review cadence | Annually |

## 1. Purpose

This policy makes sure that the right people have the right access to {{COMPANY_NAME}} systems and data, for the right amount of time, and no longer. It covers how access is requested, granted, reviewed and removed, including when people join, move roles or leave.

## 2. Scope

This policy applies to:

- All employees, contractors, interns and third parties who need access to company systems.
- All systems that hold or process company data, including the identity provider ({{IDENTITY_PROVIDER}}), SaaS applications, cloud infrastructure, servers, network devices, and physical offices.
- User, administrator, service and shared accounts.

## 3. Roles and responsibilities

| Role | Responsibilities |
| --- | --- |
| Hiring manager / line manager | Requests access for new starters and movers based on role, notifies HR and IT of leavers, and reviews their team's access. |
| {{HR_LEAD}} | Triggers onboarding and offboarding by notifying {{IT_PROVIDER}} of start dates, role changes and end dates. |
| {{IT_PROVIDER}} | Creates, changes and removes accounts; keeps records of requests and approvals; runs access reports. |
| System owners | Define roles for their system, approve access requests, and complete access reviews. |
| {{SECURITY_LEAD}} | Owns this policy, approves privileged access and exceptions, and oversees access reviews. |

## 4. Policy statements

### 4.1 Principles

1. Access must be granted on a **least privilege** and **need-to-know** basis: people get the minimum access needed to do their job.
2. Access should be granted through predefined roles or groups (role-based access) rather than to individuals one at a time.
3. Every account must be traceable to a single named person, except approved service and break-glass accounts, which must each have a named owner.
4. Duties that could allow fraud or a serious error if done by one person (for example, creating a supplier and approving payment to it) should be split between different people, or covered by a review control where the team is too small to split them.

### 4.2 Requesting and approving access

1. Access must be requested through {{ACCESS_REQUEST_METHOD}} so that there is a record.
2. Access requests must be approved by the person's manager and, for sensitive systems, by the system owner.
3. Privileged or administrator access must also be approved by {{SECURITY_LEAD}}.
4. {{IT_PROVIDER}} must keep a record of who requested, approved and granted access, and when.

### 4.3 Privileged access

1. Administrator rights must be limited to people who need them for their role and kept to the smallest practical number.
2. Administrators must use separate, dedicated admin accounts protected by phishing-resistant MFA, as set out in the [Password and MFA Policy](02-password-and-mfa.md).
3. Standard users must not have local administrator rights on their devices. Where software installation is needed, it should be handled through device management or an approved elevation tool.
4. Time-limited ("just-in-time") elevation should be used where the platform supports it.
5. Administrator activity on critical systems should be logged, and logs retained for at least {{LOG_RETENTION_PERIOD}}.

### 4.4 Onboarding (joiners)

1. {{HR_LEAD}} must notify {{IT_PROVIDER}} of new starters at least {{ONBOARDING_NOTICE_DAYS}} business days before their start date, including role, manager and start date.
2. Accounts must not be activated before background checks (where required by role or law) and contract signature are complete.
3. New starters must complete security awareness training and acknowledge the [Acceptable Use Policy](01-acceptable-use.md) within their first {{TRAINING_DEADLINE_DAYS}} days.
4. Initial credentials must be delivered securely (for example, a one-time link or in person) and never in the same message as the username.

### 4.5 Role changes (movers)

1. Managers must request access changes when someone changes role.
2. Access that is no longer needed for the new role must be removed within 5 business days of the change. Temporary overlap should be time-limited and approved.

### 4.6 Offboarding (leavers)

1. {{HR_LEAD}} or the manager must notify {{IT_PROVIDER}} of every departure as soon as it is known.
2. For planned departures, access must be disabled by the end of the person's last working day.
3. For involuntary or high-risk departures, access must be disabled before or at the time the person is notified.
4. All access must be disabled within 24 hours of departure at the latest, including SaaS accounts that are not connected to SSO.
5. Company devices and assets must be recovered, and data on them preserved or wiped as appropriate.
6. Mailboxes and files must be handed over to the manager or archived according to the retention schedule, not simply deleted.

### 4.7 Access reviews

1. System owners must review user access to critical systems at least **quarterly** and all other systems at least **every six months**.
2. Privileged accounts must be reviewed at least **quarterly**.
3. Reviews must confirm that each account still belongs to a current person with a business need, and that access levels are correct. Inappropriate access must be removed within 5 business days of the review.
4. Review evidence (who reviewed, when, what changed) must be retained for at least 12 months.

### 4.8 Dormant accounts

1. Accounts that have not been used for 45 days should be disabled automatically or flagged for review.
2. Disabled accounts should be deleted after {{ACCOUNT_DELETION_PERIOD}} unless there is a documented reason to keep them.

### 4.9 Third-party and contractor access

1. Contractors and vendors must have individual accounts with an expiry date matching their contract or engagement.
2. Remote support access for vendors must be enabled only when needed, logged, and removed or disabled afterwards.

### 4.10 Physical access

1. Access to offices, server rooms and network cabinets must be restricted to authorised people and removed at offboarding.
2. Visitors must be signed in and accompanied in non-public areas.

## 5. Checklists

### 5.1 Onboarding checklist

Complete for every new starter. Keep a copy with the access request record.

#### Before day one

- [ ] Signed contract and confidentiality agreement received ({{HR_LEAD}})
- [ ] Background check complete where required ({{HR_LEAD}})
- [ ] Role, manager and start date sent to {{IT_PROVIDER}}
- [ ] Access request approved by manager (and system owner where needed)
- [ ] Account created in {{IDENTITY_PROVIDER}} and added to role-based groups
- [ ] Device prepared: enrolled in device management, disk encryption on, endpoint protection installed, updates applied
- [ ] Account created in {{PASSWORD_MANAGER}}

#### Day one

- [ ] Credentials delivered securely; user sets their own passphrase
- [ ] MFA enrolled (security key or authenticator app); backup method registered
- [ ] Acceptable Use Policy acknowledged
- [ ] Physical access badge or keys issued and logged
- [ ] Shown how to report phishing and incidents ({{SECURITY_EMAIL}}, {{PHISHING_REPORT_METHOD}})

#### First {{TRAINING_DEADLINE_DAYS}} days

- [ ] Security awareness training completed
- [ ] Role-specific training completed (for example, payments verification for finance)
- [ ] Manager confirms access is correct, nothing missing, nothing extra

### 5.2 Role change checklist

- [ ] New role and effective date confirmed by {{HR_LEAD}}
- [ ] Access for new role requested and approved
- [ ] Access from old role identified and removed (within 5 business days)
- [ ] Shared vaults, distribution lists and on-call rotas updated
- [ ] Any privileged access re-approved by {{SECURITY_LEAD}}

### 5.3 Offboarding checklist

#### Before or on the last day

For involuntary departures, complete these at the time the person is notified.

- [ ] Departure date and type (voluntary/involuntary) sent to {{IT_PROVIDER}}
- [ ] {{IDENTITY_PROVIDER}} account disabled and all sessions/tokens revoked
- [ ] MFA methods and registered devices removed
- [ ] Access removed from applications not connected to SSO (check the application inventory)
- [ ] {{PASSWORD_MANAGER}} access removed; shared vault passwords the person knew are rotated
- [ ] VPN, remote access and cloud console access removed
- [ ] Email forwarding rules and mailbox delegations reviewed and removed
- [ ] Mailbox converted/archived and delegated to manager if needed; auto-reply set
- [ ] Ownership of files, shared drives and SaaS resources transferred
- [ ] Company devices, security keys, badges and keys returned and logged
- [ ] Personal devices: company apps and data removed (see [Remote Work and BYOD Policy](08-remote-work-byod.md))
- [ ] Physical access revoked; alarm codes changed if the person knew them

#### Within 24 hours

- [ ] All remaining access confirmed removed
- [ ] Vendor portals, banking and payment platforms, domain registrar and social media accounts checked
- [ ] Offboarding record signed off by {{IT_PROVIDER}} and manager

#### Later

- [ ] Returned devices wiped or reimaged (after any legal hold is cleared)
- [ ] Licences reclaimed
- [ ] Account deleted after {{ACCOUNT_DELETION_PERIOD}}

## 6. Exceptions

Exceptions (for example, a shared account on a system that does not support individual users) must be approved by {{SECURITY_LEAD}}, documented with compensating controls and an end date, and reviewed at least every 12 months.

## 7. Enforcement

Granting access without approval, sharing accounts, or failing to remove leavers' access may lead to disciplinary action. Missed offboarding steps found during access reviews must be treated as security events and investigated.

## 8. Review cadence

{{POLICY_OWNER}} reviews this policy and its checklists at least annually, and after any access-related incident or significant change to the identity provider or HR systems.

## 9. Related documents

- [Password and MFA Policy](02-password-and-mfa.md)
- [Acceptable Use Policy](01-acceptable-use.md)
- [Vendor and Third-Party Risk Policy](06-vendor-and-third-party-risk.md)
- [Data Classification and Handling Policy](07-data-classification-and-handling.md)

## Version history

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 1.0 | {{EFFECTIVE_DATE}} | {{POLICY_OWNER}} | Initial version, adapted from the CalliArc SMB Security Policies template v0.1.0 |
