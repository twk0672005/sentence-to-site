# Security policy

## Reporting a vulnerability

Please do not post security-sensitive details, credentials, or exploit steps in a public issue. Use the repository host's private security-reporting channel when available, or contact the maintainer through a private channel listed on the repository profile.

## Scope

Browser utilities reject static roots containing `.git`, `.env`, private-key
files or symlinks, require an identity marker, and restrict external URLs unless
explicitly enabled. A bypass, path escape, stale-port false pass,
browser-process leak, or secret-bearing receipt is in scope.

This repository contains documentation and local verification utilities. Reports are especially useful for unsafe file handling, accidental secret disclosure, dependency risks, or behavior that could cause an unintended public action.

Please include a minimal reproduction, impact, affected version or commit, and a safe remediation suggestion where possible.
