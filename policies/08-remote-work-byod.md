# Remote Work and BYOD Policy

<!-- TEMPLATE NOTE: Check local employment and privacy law before enforcing device management on personal devices. In some places, employees must consent, and you may need to reimburse costs. Remove this comment before publishing. -->

| Field | Value |
| --- | --- |
| Policy owner | {{POLICY_OWNER}} |
| Approved by | {{EXECUTIVE_SPONSOR}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Classification | Internal |
| Review cadence | Annually |

## 1. Purpose

Many people at {{COMPANY_NAME}} work from home, while travelling, or on their own phones. This policy sets out the security basics for working outside the office and for using personal devices ("bring your own device", or BYOD), so that flexibility does not come at the cost of company or customer data.

## 2. Scope

This policy applies to:

- Anyone working for {{COMPANY_NAME}} from a location other than a company office.
- Any personal device (phone, tablet, computer) used to access company email, chat, files or applications.

It adds to, and does not replace, the [Acceptable Use Policy](01-acceptable-use.md).

## 3. Roles and responsibilities

| Role | Responsibilities |
| --- | --- |
| Remote workers and BYOD users | Follow this policy, keep devices updated and secure, and report loss or compromise promptly. |
| Managers | Approve remote work arrangements and make sure team members have what they need to work securely. |
| {{IT_PROVIDER}} | Provides and manages remote access tools and device management; enforces minimum device requirements. |
| {{SECURITY_LEAD}} | Owns this policy and approves exceptions. |
| {{HR_LEAD}} | Handles the employment side of remote work and BYOD agreements. |

## 4. Policy statements

### 4.1 Working remotely

1. Remote workers must use company-managed devices for company work wherever possible.
2. Home Wi-Fi must be protected with WPA2 or WPA3 and a strong passphrase, and the router's default admin password must be changed. Router firmware should be kept up to date.
3. On public or untrusted networks, users must use {{VPN_OR_SECURE_ACCESS}} where required, or a personal mobile hotspot.
4. Users must position screens and take calls so that Confidential information cannot be seen or overheard by others, including household members.
5. Users must not leave devices unattended in public places, and must lock devices when away from them even at home.
6. Company paper documents should not be taken home. Where unavoidable, they must be stored securely and returned to the office or disposed of using a cross-cut shredder.
7. Users must not use public or shared computers (for example, hotel business centres) to access company systems.

### 4.2 Travel

1. Users should take only the devices and data they need when travelling.
2. Before travelling internationally, users should check with {{SECURITY_LEAD}} for any destination-specific guidance, including laws on encryption and device inspection at borders.
3. Users must report any device that was taken out of their sight by officials or others while travelling.

### 4.3 Personal devices (BYOD): eligibility

1. Personal devices may be used to access company email, chat and approved applications only if they meet the minimum requirements in section 4.4 and the user has accepted the BYOD agreement in section 5.
2. Personal devices must not be used to access Restricted data, or administrative consoles, unless an exception has been approved.
3. Personal computers (as opposed to phones and tablets) should only access company services through a web browser or a virtual desktop, not by syncing files locally.

### 4.4 Personal devices: minimum requirements

1. The device must run an operating system version that still receives security updates from its manufacturer, and updates must be installed promptly.
2. The device must be protected by a PIN of at least 6 digits, a password, or biometric unlock, and must lock automatically after no more than 5 minutes of inactivity.
3. The device must not be jailbroken or rooted.
4. Device encryption must be turned on (this is the default on current iOS and Android devices with a passcode set).
5. Company apps must be installed from official app stores only.
6. Company data must be accessed only through approved apps managed by {{DEVICE_MANAGEMENT}} (for example, work profiles or app protection policies), which keep company data separate from personal data.

### 4.5 What {{COMPANY_NAME}} can and cannot do on personal devices

1. {{COMPANY_NAME}} **can**: require a passcode and encryption; check the operating system version and whether the device is jailbroken; manage and remove company apps and data; block access from non-compliant devices.
2. {{COMPANY_NAME}} **will not**: read personal email, messages, photos or browsing history; track device location except where the user requests it to find a lost device; wipe personal data except as described in 4.5.3.
3. Where device management is limited to a work profile or app protection, only company data will be wiped. A full device wipe will only be performed if the user has agreed to it (for example, for a device that was enrolled in full management) and the device is lost or stolen.

### 4.6 Separation of data

1. Users must not copy company data from managed apps into personal apps, personal cloud storage, or personal email.
2. Users must not back up company data to personal backup services; company data is backed up by {{COMPANY_NAME}}.

### 4.7 Loss, theft and leaving

1. Users must report a lost or stolen device used for company work to {{IT_HELPDESK}} as soon as possible and within 24 hours at the latest, so that access can be blocked and company data removed.
2. When a user leaves {{COMPANY_NAME}}, or stops using a personal device for work, company apps and data will be removed from the device. Users must not keep copies of company data.
3. Before selling, giving away or trading in a personal device that has been used for work, users must remove company apps and accounts, or ask {{IT_HELPDESK}} to do it.

## 5. BYOD agreement

To be accepted by each user before enrolling a personal device.

> I want to use my personal device to access {{COMPANY_NAME}} systems. I have read the Remote Work and BYOD Policy and agree to:
>
> - Keep my device updated, protected with a passcode, encrypted, and not jailbroken or rooted.
> - Access company data only through approved apps, and not copy it into personal apps or services.
> - Report loss, theft or suspected compromise within 24 hours.
> - Allow {{COMPANY_NAME}} to manage and remove company apps and data from my device, and to block access if the device does not meet requirements.
>
> I understand that {{COMPANY_NAME}} will not access my personal data, and that support for my personal device is limited to company apps.

| Name | Device (make/model) | Signature | Date |
| --- | --- | --- | --- |
| | | | |

## 6. Exceptions

Exceptions (for example, a personal laptop used by a contractor who has no company device) must be approved by {{SECURITY_LEAD}}, with compensating controls such as browser-only access or a virtual desktop, and an end date. Exceptions are reviewed at least every 12 months.

## 7. Enforcement

Devices that do not meet requirements will be blocked from accessing company services until they are fixed. Deliberately bypassing controls, or moving company data into personal services, may lead to disciplinary action.

## 8. Review cadence

{{POLICY_OWNER}} reviews this policy at least annually, and when device management tools, remote access methods, or relevant laws change.

## 9. Related documents

- [Acceptable Use Policy](01-acceptable-use.md)
- [Data Classification and Handling Policy](07-data-classification-and-handling.md)
- [Password and MFA Policy](02-password-and-mfa.md)
- [Incident Response Plan](04-incident-response-plan.md)

## Version history

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 1.0 | {{EFFECTIVE_DATE}} | {{POLICY_OWNER}} | Initial version, adapted from the CalliArc SMB Security Policies template v0.1.0 |
