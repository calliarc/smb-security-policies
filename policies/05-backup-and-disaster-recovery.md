# Backup and Disaster Recovery Policy

<!-- TEMPLATE NOTE: The RPO/RTO table in section 5 contains example values. Agree real values with business owners; they drive backup frequency and cost. Remove this comment before publishing. -->

| Field | Value |
| --- | --- |
| Policy owner | {{POLICY_OWNER}} |
| Approved by | {{EXECUTIVE_SPONSOR}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Classification | Internal |
| Review cadence | Annually |

## 1. Purpose

This policy makes sure {{COMPANY_NAME}} can recover its data and keep essential services running after hardware failure, human error, ransomware, a supplier outage or a site disaster. It sets out what must be backed up, how, how often, how backups are protected, and how recovery is tested.

## 2. Scope

This policy covers:

- Servers, virtual machines and cloud infrastructure operated by or for {{COMPANY_NAME}}.
- SaaS applications that hold company data (for example, email, file storage, CRM, accounting). A SaaS provider keeping its service running is **not** the same as {{COMPANY_NAME}} having a backup of its data.
- Configuration of critical systems: firewalls, identity provider, domain and DNS settings, device management profiles.
- Laptops and desktops, to the extent that company data is kept on them.

## 3. Roles and responsibilities

| Role | Responsibilities |
| --- | --- |
| {{EXECUTIVE_SPONSOR}} | Approves RPO/RTO targets and the budget to meet them; declares a disaster. |
| System owners | Define how critical their system is and agree RPO/RTO; take part in restore tests. |
| {{IT_PROVIDER}} | Configures and monitors backups, fixes failures, runs restore tests, maintains recovery runbooks. |
| {{SECURITY_LEAD}} | Owns this policy, checks that backups are protected from tampering, reviews test results. |

## 4. Policy statements

### 4.1 Backup coverage

1. {{IT_PROVIDER}} must keep an inventory of systems and data sets in scope, with each one's owner, criticality tier, backup method and RPO/RTO.
2. All systems in tier 1 to 3 (see section 5) must be backed up. Tier 4 data must be backed up if it is not easily re-created.
3. SaaS data for email, file storage and other critical applications must be backed up using a dedicated third-party backup service or export process, not only the provider's recycle bin or version history.
4. Users must store work files in approved company storage ({{FILE_STORAGE}}), which is backed up, rather than only on local devices.

### 4.2 The 3-2-1 rule

{{COMPANY_NAME}} follows the **3-2-1** rule, strengthened for ransomware:

1. Keep at least **3** copies of important data (the live data plus two backups).
2. Store them on at least **2** different types of storage or platforms (for example, a local backup appliance and a cloud backup service).
3. Keep at least **1** copy off-site, in a different location or cloud region from the primary data.
4. In addition, at least **1** copy must be **immutable or offline** (for example, object-lock storage, a vendor "immutable" retention setting, or media physically disconnected), so that an attacker with administrator access cannot delete or encrypt it.
5. Restores must be verified so that there are **0** unresolved errors in backup jobs and test restores.

### 4.3 Protecting backups

1. Backups must be encrypted in transit and at rest. Encryption keys must be stored separately from the backups and recoverable if the primary environment is lost.
2. Access to backup consoles and storage must use separate administrator accounts from the main environment, protected by phishing-resistant MFA.
3. Backup systems should not be joined to the same domain or identity tenant as production systems, where practical.
4. Deleting backups or shortening retention must require MFA and, where the product supports it, a second approver or a delay period.
5. Backup media and off-site copies must be protected at the same classification level as the data they contain (see [Data Classification and Handling Policy](07-data-classification-and-handling.md)).

### 4.4 Frequency and retention

1. Backup frequency must be sufficient to meet each system's RPO.
2. Unless the business or legal requirements say otherwise, backups must be retained as follows:

   | Backup type | Minimum retention |
   | --- | --- |
   | Daily | 30 days |
   | Weekly | 12 weeks |
   | Monthly | 12 months |
   | Yearly (if required for legal or financial records) | {{YEARLY_BACKUP_RETENTION}} |

3. Retention must not exceed what is allowed under the company's data retention schedule and privacy obligations.

### 4.5 Monitoring

1. Backup jobs must be monitored daily, with alerts sent to {{IT_PROVIDER}} on failure.
2. A failed backup of a tier 1 or 2 system must be investigated and resolved, or escalated to {{SECURITY_LEAD}}, within 1 business day.
3. {{IT_PROVIDER}} must provide a monthly backup status report to {{SECURITY_LEAD}}.

### 4.6 Testing

1. A sample of files, mailboxes and records must be test-restored at least **quarterly**.
2. A full restore of each tier 1 system must be tested at least **annually**, measuring actual recovery time against the RTO.
3. Test results, including failures and time taken, must be recorded using the template in section 7.2, and gaps tracked to resolution.

### 4.7 Disaster recovery

1. {{COMPANY_NAME}} must maintain a recovery runbook for each tier 1 and tier 2 system describing recovery steps, dependencies, required credentials and contacts.
2. Runbooks and this policy must be available offline or outside the primary environment.
3. A disaster is declared by the {{EXECUTIVE_SPONSOR}} (or delegate) on the advice of {{IT_PROVIDER}}. Where the cause may be an attack, the [Incident Response Plan](04-incident-response-plan.md) must be followed as well, and systems must not be restored until the Incident Lead is satisfied that restoring will not reintroduce the attacker.
4. Recovery follows the priority order in section 5 unless the Executive Sponsor decides otherwise.
5. Staff must be told how to keep working during an outage (for example, alternative communication channels, manual processes) as part of the business continuity arrangements.

## 5. Recovery objectives (RPO/RTO)

- **RPO (Recovery Point Objective):** the maximum amount of data, measured in time, that the business can afford to lose. An RPO of 4 hours means backups must run at least every 4 hours.
- **RTO (Recovery Time Objective):** the maximum time a system can be unavailable before the impact is unacceptable.

Replace the example systems and values below with your own.

| Tier | Description | Example systems | RPO | RTO | Backup method |
| --- | --- | --- | --- | --- | --- |
| 1: Critical | Business stops without it. | Identity provider, email, core line-of-business app, finance/payments | 4 hours | 8 hours | Continuous or 4-hourly snapshots + immutable off-site copy |
| 2: Important | Significant disruption within a day. | File storage, CRM, phone system | 24 hours | 24 hours | Daily backup + immutable off-site copy |
| 3: Standard | Can work around it for a few days. | HR system, intranet, project tools | 24 hours | 72 hours | Daily backup + off-site copy |
| 4: Low | Inconvenient but not urgent. | Archive data, test environments | 7 days | 2 weeks | Weekly backup or re-create from source |

System inventory (maintain here or in a linked register):

| System | Owner | Tier | RPO | RTO | Backup tool/provider | Last full restore test |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## 6. Exceptions

Where a system cannot meet its RPO/RTO or the 3-2-1 rule, the system owner must document the risk, compensating measures and planned remediation, and obtain approval from {{SECURITY_LEAD}} and {{EXECUTIVE_SPONSOR}}. Exceptions are reviewed at least every 12 months.

## 7. Enforcement and records

### 7.1 Enforcement

Deleting or disabling backups without authorisation, or failing to report backup failures, may lead to disciplinary action. Unresolved backup failures for tier 1 or 2 systems must be reported to the Executive Sponsor.

### 7.2 Restore test record

```text
Test date:
System / data set:
Tier:          RPO:          RTO:
Test type:     File sample / Full system / Failover
Restore point used (date/time):
Time to restore (actual):
Data verified by (system owner):
Result:        Pass / Pass with issues / Fail
Issues found and actions (owner, due date):
```

## 8. Review cadence

{{POLICY_OWNER}} reviews this policy at least annually, after any major restore or disaster, after significant changes to systems or backup tools, and whenever RPO/RTO targets are changed.

## 9. Related documents

- [Incident Response Plan](04-incident-response-plan.md)
- [Data Classification and Handling Policy](07-data-classification-and-handling.md)
- [Vendor and Third-Party Risk Policy](06-vendor-and-third-party-risk.md)

## Version history

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 1.0 | {{EFFECTIVE_DATE}} | {{POLICY_OWNER}} | Initial version, adapted from the CalliArc SMB Security Policies template v0.1.0 |
