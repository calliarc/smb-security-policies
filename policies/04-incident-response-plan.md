# Incident Response Plan

<!-- TEMPLATE NOTE: Print a copy of the contact tree (section 6) and keep it somewhere you can reach if email and chat are down. Fill in real names and phone numbers, not only roles. Remove this comment before publishing. -->

| Field | Value |
| --- | --- |
| Policy owner | {{POLICY_OWNER}} |
| Approved by | {{EXECUTIVE_SPONSOR}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Classification | Internal |
| Review cadence | Annually, plus after every Severity 1 or 2 incident |

## 1. Purpose

This plan describes how {{COMPANY_NAME}} detects, responds to and recovers from security incidents. Its goal is to limit damage, restore normal operations quickly, meet legal and contractual obligations, and learn from what happened. It is written so that someone under pressure can follow it without having read it the day before.

## 2. Scope

This plan covers any event that threatens the confidentiality, integrity or availability of {{COMPANY_NAME}} information or systems, including those operated by suppliers on our behalf. Examples:

- Phishing that leads to a compromised account
- Ransomware or other malware
- Business email compromise and payment fraud
- Lost or stolen devices holding company data
- Data sent to the wrong person, or exposed publicly by mistake
- Unauthorised access by an insider or former employee
- A security incident at a vendor that affects our data
- Denial-of-service or outage caused by an attack

Non-security IT outages are handled through normal IT support and the [Backup and Disaster Recovery Policy](05-backup-and-disaster-recovery.md), but should be escalated under this plan if an attack is suspected.

## 3. Definitions

| Term | Meaning |
| --- | --- |
| Security event | Something observable that might indicate a security problem, such as an alert, a suspicious email, or an odd login. Most events are not incidents. |
| Security incident | An event that has been assessed and is confirmed or strongly suspected to harm, or threaten to harm, our information or systems. |
| Personal data breach | An incident that leads to accidental or unlawful destruction, loss, alteration, disclosure of, or access to personal data. May trigger legal notification duties. |
| Incident Lead | The person who coordinates the response for a specific incident. |

## 4. Roles and responsibilities

For a small company one person may hold several roles. Name a primary and a backup for each.

| Role | Primary | Backup | Responsibilities |
| --- | --- | --- | --- |
| Incident Lead | {{SECURITY_LEAD}} | {{IR_BACKUP_LEAD}} | Declares the incident and severity, coordinates the response, keeps the incident log, decides when to escalate and when to close. |
| Technical Lead | {{IT_PROVIDER}} | {{IT_BACKUP_CONTACT}} | Investigates, contains, eradicates and recovers; preserves evidence. |
| Executive Sponsor | {{EXECUTIVE_SPONSOR}} | {{EXECUTIVE_BACKUP}} | Makes business decisions (for example, shutting systems down, paying for outside help), approves external communications. |
| Communications Lead | {{COMMS_LEAD}} | {{EXECUTIVE_SPONSOR}} | Drafts internal, customer and public messages; single point of contact for media. |
| Legal and Privacy | {{LEGAL_COUNSEL}} | {{PRIVACY_CONTACT}} | Advises on notification duties, privilege, law enforcement and contracts. |
| HR | {{HR_LEAD}} | Manager of the person involved | Handles incidents involving employees, and staff communications. |
| Scribe | Assigned by the Incident Lead | | Records a timestamped log of actions, decisions and evidence. |

All staff must report suspected incidents immediately to {{SECURITY_EMAIL}} or {{IT_HELPDESK}}, and must not try to investigate or "clean up" on their own.

## 5. Severity levels

The Incident Lead assigns a severity at triage and reviews it as facts emerge. If unsure, choose the higher level.

| Severity | Description | Examples | Response target | Who is notified |
| --- | --- | --- | --- | --- |
| **SEV 1: Critical** | Major business disruption, or confirmed exposure of Restricted data or large amounts of personal data. | Ransomware across multiple systems; confirmed breach of customer database; fraudulent payment sent. | Incident Lead engaged within 30 minutes, 24/7. | Full response team, Executive Sponsor, legal, cyber insurer. |
| **SEV 2: High** | Confirmed compromise with limited spread, or probable exposure of Confidential or personal data. | One compromised mailbox used to send phishing; malware on a single server; lost unencrypted laptop. | Engaged within 2 hours, 24/7. | Incident Lead, Technical Lead, Executive Sponsor; legal as needed. |
| **SEV 3: Medium** | Suspicious activity or a contained compromise with no evidence of data exposure. | User entered password on a phishing site but MFA blocked sign-in; malware quarantined by endpoint protection. | Engaged within 1 business day. | Incident Lead, Technical Lead. |
| **SEV 4: Low** | Minor policy violation or blocked attack with no impact. | Reported phishing email that nobody clicked; lost encrypted, managed phone wiped remotely. | Handled within normal IT support timelines. | Recorded in the incident log. |

## 6. Contact tree

Keep this section current. Store a printed or offline copy with the Incident Lead and Executive Sponsor.

```text
Anyone who spots something
        |
        v
{{SECURITY_EMAIL}} / {{IT_HELPDESK}}
        |
        v
Incident Lead: {{SECURITY_LEAD}}  (backup: {{IR_BACKUP_LEAD}})
        |
        +--> Technical Lead: {{IT_PROVIDER}}
        |
        +--> SEV 1 or 2 --> Executive Sponsor: {{EXECUTIVE_SPONSOR}}
                               |
                               +--> Legal counsel: {{LEGAL_COUNSEL}}
                               +--> Cyber insurer: {{CYBER_INSURER}} ({{INSURER_HOTLINE}})
                               +--> Communications Lead: {{COMMS_LEAD}}
                               +--> HR: {{HR_LEAD}} (if staff involved)
```

| Contact | Name | Phone | Email | Notes |
| --- | --- | --- | --- | --- |
| Incident Lead | {{SECURITY_LEAD}} | | | |
| Backup Incident Lead | {{IR_BACKUP_LEAD}} | | | |
| IT / MSP | {{IT_PROVIDER}} | | | Contract number / support portal: |
| Executive Sponsor | {{EXECUTIVE_SPONSOR}} | | | |
| Legal counsel | {{LEGAL_COUNSEL}} | | | |
| Cyber insurer | {{CYBER_INSURER}} | {{INSURER_HOTLINE}} | | Policy number: |
| Incident response retainer (if any) | {{IR_RETAINER}} | | | |
| Bank fraud line | | | | For payment fraud, call immediately. |
| Law enforcement | | | | Local police cyber unit or national reporting service. |
| Data protection regulator | | | | Only after consulting legal counsel. |

> Check your cyber insurance policy before an incident. Many policies require you to call the insurer's hotline first and use their approved responders, or they may not cover the costs.

## 7. Response phases

### Phase 1: Prepare

Before anything happens:

1. {{COMPANY_NAME}} must keep this plan, the contact tree and key system documentation where they can be reached without company systems (for example, a printed copy and a copy in a personal password manager of the Incident Lead).
2. Logging must be enabled on the identity provider, email, endpoint protection, firewall and critical applications, with retention of at least {{LOG_RETENTION_PERIOD}}.
3. Backups must be in place and tested, as described in the [Backup and Disaster Recovery Policy](05-backup-and-disaster-recovery.md).
4. Staff must be trained to recognise and report incidents.
5. A tabletop exercise must be run at least once a year (see section 10).
6. An out-of-band communication channel (for example, a group on a separate messaging app or a phone bridge) should be agreed in advance in case email or chat is compromised.

### Phase 2: Detect and triage

1. Record the report in the incident log: who reported, when, what they saw.
2. The Incident Lead (or Technical Lead) makes an initial assessment within the response target for a provisional severity.
3. Decide: is this an incident? If yes, declare it, assign a severity and an Incident Lead, and open an incident record using the template in section 9.1.
4. Notify people according to the severity table and contact tree.
5. Contact the cyber insurer early for SEV 1 and SEV 2 incidents.

### Phase 3: Contain

The goal is to stop things getting worse while preserving evidence.

1. Short-term containment examples: disconnect affected devices from the network (do not power them off unless instructed), disable compromised accounts and revoke sessions, block malicious senders or domains, isolate affected cloud workloads.
2. Preserve evidence before making changes where possible: export relevant logs, take screenshots, note times (with time zone), and record what was done and by whom.
3. For payment fraud, contact the bank immediately; recall requests are time-sensitive.
4. Do not contact or negotiate with attackers, and do not pay any ransom, without Executive Sponsor, legal counsel and insurer involvement.

### Phase 4: Eradicate

1. Identify the root cause and how the attacker got in.
2. Remove malware, malicious mailbox rules, rogue accounts, OAuth app grants and persistence mechanisms.
3. Reset credentials that may be exposed, including service accounts and API keys.
4. Patch the vulnerability or fix the configuration that was exploited.

### Phase 5: Recover

1. Restore systems from known-good backups or rebuild them, as described in the [Backup and Disaster Recovery Policy](05-backup-and-disaster-recovery.md).
2. Verify systems are clean and working before returning them to users.
3. Monitor closely for signs that the attacker has returned, for at least {{POST_INCIDENT_MONITORING_DAYS}} days.
4. The Incident Lead confirms with the Executive Sponsor when normal operations have resumed.

### Phase 6: Notify

Run in parallel with the phases above for any incident involving personal data or customer data.

1. Legal counsel must assess notification obligations under applicable law (for example, data protection laws, sector regulations and state breach notification laws) and under customer contracts. Some deadlines are short: under the EU and UK GDPR, notifiable personal data breaches must be reported to the regulator within 72 hours of becoming aware.
2. External notifications (regulators, customers, affected individuals, partners) must be approved by the Executive Sponsor and legal counsel.
3. Keep a record of all notifications sent, to whom and when.

### Phase 7: Learn

1. For SEV 1 and SEV 2 incidents, hold a blameless post-incident review within 10 business days of closure. For SEV 3, a short written summary is enough.
2. Use the template in section 9.4.
3. Track follow-up actions to completion with owners and dates.
4. Update this plan, related policies and training based on what was learned.

## 8. Evidence and records

1. Incident records, logs and evidence must be kept for at least {{INCIDENT_RECORD_RETENTION}} or longer if required by law, contract or an ongoing legal matter.
2. Evidence that may be used in legal proceedings should be handled with a documented chain of custody. If this is likely, engage a qualified forensic provider through legal counsel or the insurer.

## 9. Templates

### 9.1 Incident record

```text
Incident ID:            IR-YYYY-NNN
Date/time detected:     (include time zone)
Reported by:
Incident Lead:
Severity:               SEV 1 / 2 / 3 / 4   (update history below)
Status:                 Open / Contained / Recovered / Closed
Summary:                What happened, in two or three sentences.
Systems affected:
Data affected:          Type, classification, approx. number of records/people
Personal data involved: Yes / No / Unknown
Insurer notified:       Yes / No   Claim ref:
Timeline:
  YYYY-MM-DD HH:MM  Event / action / decision  (who)
Actions outstanding:
Notifications sent:
Closed by / date:
```

### 9.2 Internal staff notice

```text
Subject: Action needed: security issue affecting [system]

We are dealing with a security issue affecting [system/service].
Our team is working on it now.

What you need to do:
- [For example: do not open emails from X / sign out and back in / change
  your password when prompted]
- Report anything unusual to {{SECURITY_EMAIL}} or {{IT_HELPDESK}}.

What you should not do:
- Do not discuss this outside the company or on social media.
- Direct any questions from customers or media to {{COMMS_LEAD}}.

We will send an update by [time].

[Name], Incident Lead
```

### 9.3 Customer notification (initial)

Adapt with legal counsel before sending. Keep to facts; do not speculate.

```text
Subject: Security incident notice from {{COMPANY_NAME}}

Dear [customer name],

On [date], {{COMPANY_NAME}} identified a security incident affecting
[system/service]. We are writing to let you know what happened, what it
means for you, and what we are doing about it.

What happened: [Brief factual description.]

What information was involved: [Types of data, or "We are still
investigating and will update you by [date]."]

What we are doing: [Containment and recovery steps; outside experts
engaged; law enforcement or regulators informed if applicable.]

What you can do: [Specific, practical steps, for example watching for
phishing that references this incident, or resetting shared credentials.]

For more information: Contact [name] at [email/phone].

We are sorry for the concern this may cause and will keep you updated.

[Name, title]
{{COMPANY_NAME}}
```

### 9.4 Post-incident review

```text
Incident ID:
Review date / attendees:
Summary:
Timeline of key events:
Root cause (technical and process):
What went well:
What could be improved:
Was the severity right? Were response targets met?
Actions:
  | # | Action | Owner | Due date | Status |
Policy/plan updates required:
```

## 10. Tabletop exercise

{{COMPANY_NAME}} must run at least one tabletop exercise a year, involving the Incident Lead, Technical Lead, Executive Sponsor and Communications Lead. A tabletop is a discussion, not a live test: a facilitator walks the group through a scenario and the group talks through what they would do.

### 10.1 How to run it (60 to 90 minutes)

1. Pick a scenario relevant to the business (see below) and brief a facilitator who is not a player.
2. Share the plan and contact tree with players beforehand.
3. The facilitator presents the scenario in stages ("injects"), pausing after each for the group to decide what to do, who does it, and who needs to know.
4. The scribe records decisions, gaps and questions.
5. Finish with a 15-minute debrief and turn the gaps into tracked actions.

### 10.2 Sample scenario: business email compromise

| Inject | Situation | Discussion questions |
| --- | --- | --- |
| 1 | Monday, 09:10. A customer calls: they paid last month's invoice to "our new bank account" from an email that came from your finance manager's real mailbox. | Who takes the call? Who do you tell? What severity is this? |
| 2 | {{IT_PROVIDER}} finds a mailbox rule forwarding all emails containing "invoice" to an external address, created 12 days ago from an overseas IP. | What do you do with the account right now? What evidence do you keep? |
| 3 | Sign-in logs show the attacker also opened the shared finance folder, which holds customer bank details. | Is personal data involved? Who decides on notification? Is there a deadline? |
| 4 | A second customer emails asking whether they should also use the new bank details. | What do you tell customers, and who approves the message? Who calls the bank? |
| 5 | A journalist emails asking about "a data breach at {{COMPANY_NAME}}". | Who responds? What is said? |
| 6 | Wrap-up. | How did the attacker get in? Which controls would have stopped it? What are our top three actions? |

Other useful scenarios: ransomware encrypts the file server on a Friday evening; a laptop with customer data is stolen from a car; a key SaaS vendor announces a breach; a departing employee downloads the customer list.

### 10.3 Exercise record

| Date | Scenario | Participants | Key findings | Actions raised |
| --- | --- | --- | --- | --- |
| | | | | |

## 11. Exceptions

Deviations from this plan during a live incident may be made by the Incident Lead where following the plan would cause greater harm. Deviations must be recorded in the incident log and discussed in the post-incident review.

## 12. Enforcement

All staff are required to report suspected incidents promptly. Failing to report a known incident, deliberately destroying evidence, or discussing an active incident externally without authorisation may lead to disciplinary action.

## 13. Review cadence

{{POLICY_OWNER}} reviews this plan at least annually, after every SEV 1 or SEV 2 incident, after each tabletop exercise, and whenever key contacts change. The contact tree should be checked quarterly.

## 14. Related documents

- [Backup and Disaster Recovery Policy](05-backup-and-disaster-recovery.md)
- [Vendor and Third-Party Risk Policy](06-vendor-and-third-party-risk.md)
- [Data Classification and Handling Policy](07-data-classification-and-handling.md)
- [Acceptable Use Policy](01-acceptable-use.md)

## Version history

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 1.0 | {{EFFECTIVE_DATE}} | {{POLICY_OWNER}} | Initial version, adapted from the CalliArc SMB Security Policies template v0.1.0 |
