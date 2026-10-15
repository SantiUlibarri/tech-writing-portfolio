---
title: Security Update - Root Key Rotation
---

# Security Update: Root Key Rotation Process

## Summary
As part of an ongoing security initiative, Proscai updated the workflow for rotating and managing root-level credentials.  
The goal of this change is to improve **traceability**, reduce operational risk, and align internal handling with security best practices.

> **Note:** This document is a sanitized portfolio sample. It demonstrates structure and tone without exposing proprietary or sensitive details.

---

## What Changed
- Root key rotations now follow a formal **request → validation → execution → verification** workflow.
- Root key operations are logged to support operational traceability and audit readiness.
- Administrative checks were added to ensure credential changes are performed only with authorization.

---

## Who Is Affected
- System administrators responsible for infrastructure configuration.
- Support teams involved in customer credential-related requests.

---

## Why This Matters
Root-level credentials provide elevated access. By standardizing how credential rotations are requested, approved, and executed, the organization reduces:
- Unauthorized changes
- Miscommunication between support and admin teams
- Risk of accidental service impact during rotations

---

## What You Need to Do
Most users do not need to take action.

If you need a root key rotation, follow the official request procedure:
- **Root Key Rotation — Customer Request Guide** (see: `security/root-key-rotation-request-guide.md`)
