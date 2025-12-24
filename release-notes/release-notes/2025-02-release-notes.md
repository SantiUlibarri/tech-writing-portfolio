# Proscai Release Notes — February 2025

## Overview
The February 2025 release focuses on improving **Point of Sale (POS) stability**, **inventory accuracy**, and **security controls**.  
These updates reduce operational friction for retail teams and improve system reliability in high-volume transaction environments.

---

## ✨ What’s New

### Enhanced Inventory Validation (POS)
Inventory movements now include additional validation checks when selecting lots during POS transactions.  
This prevents incorrect stock deductions and improves inventory accuracy across locations.

**Who benefits**
- Store managers
- Inventory and operations teams

**Why it matters**
Incorrect lot selection could previously result in mismatched inventory counts. This update ensures stock movements align with real-world transactions.

---

## 🔧 Fixes

### POS Transaction Stability
- Fixed an issue where POS transactions could fail silently when inventory lots were missing or misconfigured.
- Improved error handling to surface actionable messages to users instead of generic failures.

### Inventory Movements
- Resolved edge cases where inventory movements were registered twice under specific POS workflows.
- Corrected validation logic affecting multi-warehouse setups.

---

## ⚡ Improvements

### System Reliability
- Improved internal logging for POS and inventory workflows, enabling faster troubleshooting by support teams.
- Optimized background validation processes to reduce latency during peak transaction hours.

### User Feedback Handling
- Refined internal checks to ensure invalid configurations are detected earlier in the workflow, reducing downstream errors.

---

## 🛡 Security Updates

### Root Credential Handling Improvements
As part of an ongoing security initiative, internal processes related to root credential management were improved.

- Root key operations now follow a formal validation and execution workflow.
- All actions are logged for traceability and audit purposes.

These changes reduce operational risk and align with security best practices.

---

## ⚠️ Known Limitations

- POS users may need to refresh the session to see updated validation messages after configuration changes.
- Additional performance optimizations are planned for upcoming releases.

---

## 📌 Action Required

No action is required for most users.

System administrators should review internal security procedures related to credential management to ensure alignment with updated workflows.

---

## 📅 Release Information
- **Release month:** February 2025  
- **Affected modules:** POS, Inventory, Security  
- **Deployment:** Automatic
