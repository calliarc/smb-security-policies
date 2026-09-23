# Password and MFA Policy

<!-- TEMPLATE NOTE: This policy is written to align with NIST SP 800-63B (Digital Identity Guidelines: Authentication and Authenticator Management), Revision 4, finalised in 2025. Check the current revision before adopting, and delete this comment before publishing. -->

| Field | Value |
| --- | --- |
| Policy owner | {{POLICY_OWNER}} |
| Approved by | {{EXECUTIVE_SPONSOR}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Classification | Internal |
| Review cadence | Annually |

## 1. Purpose

Stolen and guessed passwords are one of the most common ways attackers get into small and mid-size businesses. This policy sets practical rules for passwords and multi-factor authentication (MFA) at {{COMPANY_NAME}}. It follows modern guidance: long passphrases, a password manager, MFA everywhere it is available, and no pointless password rotation.

## 2. Scope

This policy applies to every account used to access {{COMPANY_NAME}} systems or data, including:

- User accounts in {{IDENTITY_PROVIDER}} and every application connected to it.
- Local accounts on devices, network equipment and servers.
- Administrator, service and shared "break-glass" accounts.
- Third-party SaaS accounts used for company business, even where single sign-on (SSO) is not available.

It applies to all employees, contractors and third parties who have such accounts.

## 3. Roles and responsibilities

| Role | Responsibilities |
| --- | --- |
| All users | Create strong passphrases, use the company password manager, enrol in MFA, and report suspected compromise. |
| {{IT_PROVIDER}} | Configure systems to enforce this policy, manage SSO and MFA, maintain the password blocklist, and handle resets securely. |
| {{SECURITY_LEAD}} | Owns the policy, approves exceptions, and monitors for compromised credentials. |
| System owners | Make sure applications they own meet this policy or are connected to SSO. |

## 4. Policy statements

### 4.1 Single sign-on first

1. Business applications should be connected to {{IDENTITY_PROVIDER}} for single sign-on wherever the application supports it, so that one strong, MFA-protected identity controls access.
2. When buying new software, SSO and MFA support should be treated as a selection criterion (see the [Vendor and Third-Party Risk Policy](06-vendor-and-third-party-risk.md)).

### 4.2 Password requirements

1. Passwords used as the **only** factor to sign in must be at least **15 characters** long.
2. Passwords used together with MFA must be at least **12 characters** long. (NIST permits 8; {{COMPANY_NAME}} sets a higher bar.)
3. Systems must allow passwords of at least 64 characters, and should accept spaces and all printable characters, so that people can use passphrases.
4. Systems must **not** impose composition rules such as "must contain an uppercase letter, a number and a symbol". Length does far more for security than complexity rules, which tend to produce predictable passwords like `Summer2026!`.
5. Systems must check new passwords against a blocklist of commonly used, expected or known-compromised passwords (for example, breach corpuses, dictionary words, repeated or sequential characters, and the company or product name) and reject matches.
6. Passwords must **not** be required to change on a fixed schedule (for example, every 90 days). Passwords must be changed promptly when there is evidence or reasonable suspicion of compromise.
7. Systems must not use password hints or knowledge-based "security questions" (such as "Which street did you grow up on?") for account recovery.
8. Systems should allow users to paste passwords, so that password managers work.
9. Systems must limit the number of failed sign-in attempts (rate limiting or temporary lockout) to slow down guessing attacks.
10. Passwords must be stored only as salted hashes using a password-hashing function designed for the purpose. Systems that store passwords in plain text or with reversible encryption must not be used for company data.

### 4.3 Using and protecting passwords

1. Users must use a unique password for every account. Reusing a company password on any other site is not allowed.
2. Users must store passwords in the company password manager, {{PASSWORD_MANAGER}}, and should let it generate random passwords where they do not need to type them.
3. The password manager's own master password must be a passphrase of at least 15 characters that is not used anywhere else, and the vault must be protected with MFA.
4. Users must not write passwords on paper, store them in spreadsheets, notes apps or documents, or send them over email or chat.
5. Credentials that must be shared (for example, for a legacy system with a single login) must be shared only through a shared vault in {{PASSWORD_MANAGER}}, with access limited to named people. These accounts should be removed or moved to individual accounts when possible.

### 4.4 Multi-factor authentication

1. MFA must be enabled for:
   1. Email and the identity provider ({{IDENTITY_PROVIDER}}).
   2. All remote access, including VPN, remote desktop and remote management tools.
   3. All administrator and privileged accounts.
   4. All internet-facing applications that hold company or customer data.
   5. The password manager, finance and banking platforms, payroll and HR systems.
2. Phishing-resistant MFA (FIDO2/WebAuthn security keys or platform passkeys, or certificate-based authentication) must be used for administrator accounts and should be offered to everyone.
3. Authenticator app push notifications must use number matching or an equivalent feature that prevents "push fatigue" approvals.
4. SMS and voice call codes should only be used as a fallback when stronger options are not available, and must not be used for administrator accounts.
5. Users must never approve an MFA prompt they did not initiate. An unexpected prompt must be denied and reported to {{SECURITY_EMAIL}} as a possible incident.
6. Users must never read out, forward or type an MFA code for anyone else, including someone claiming to be from IT.

### 4.5 Privileged, service and break-glass accounts

1. Administrators must use a separate administrator account for privileged tasks, and must not use it for email or web browsing.
2. Service accounts must have long, randomly generated secrets (or use certificates or managed identities), be recorded in an inventory with an owner, and be restricted to the systems they need.
3. {{COMPANY_NAME}} should keep at least two emergency ("break-glass") administrator accounts for the identity provider, excluded from normal conditional-access rules but protected with phishing-resistant MFA, stored securely, and monitored so that any use raises an alert.
4. Default passwords on devices and software must be changed before the device or software is put into use.

### 4.6 Resets and recovery

1. Help desk staff must verify a user's identity before resetting a password or MFA method, using a method that an attacker would not easily have (for example, a video call with ID, or confirmation from the user's manager through a known channel). Caller ID, email or chat alone are not sufficient.
2. Temporary passwords must be single-use and must be changed at next sign-in.
3. Resets of administrator accounts or MFA methods must be logged and reviewed.

### 4.7 Suspected compromise

1. If a user suspects a password has been exposed (for example, they entered it on a phishing page), they must change it immediately and report it to {{SECURITY_EMAIL}}.
2. {{IT_PROVIDER}} must revoke active sessions and tokens when resetting a compromised account, and review sign-in logs for suspicious activity.
3. {{COMPANY_NAME}} should monitor for company credentials appearing in public breach data and force resets for affected accounts.

## 5. Exceptions

Some legacy systems cannot meet these requirements. Exceptions must be requested from {{SECURITY_LEAD}} with a description of the system, the reason, compensating controls (for example, network isolation, IP restrictions or extra monitoring), and a target date for remediation. Exceptions are recorded in the exception register and reviewed at least every 12 months.

## 6. Enforcement

Where possible, this policy is enforced technically through {{IDENTITY_PROVIDER}}, {{PASSWORD_MANAGER}} and device management. Deliberately sharing credentials, disabling MFA, or approving MFA prompts for others may lead to loss of access and disciplinary action, as described in the [Acceptable Use Policy](01-acceptable-use.md).

## 7. Review cadence

{{POLICY_OWNER}} reviews this policy at least annually, after any credential-related incident, and whenever NIST SP 800-63B or relevant regulatory guidance is revised.

## 8. Related documents

- [Acceptable Use Policy](01-acceptable-use.md)
- [Access Control and Onboarding/Offboarding Policy](03-access-control-and-onboarding-offboarding.md)
- [Incident Response Plan](04-incident-response-plan.md)
- NIST SP 800-63B, Digital Identity Guidelines: Authentication and Authenticator Management (<https://pages.nist.gov/800-63-4/sp800-63b.html>)

## Version history

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 1.0 | {{EFFECTIVE_DATE}} | {{POLICY_OWNER}} | Initial version, adapted from the CalliArc SMB Security Policies template v0.1.0 |
