# Managing Linux Services with systemd

This document explains how to manage Linux services using `systemd`, the standard service manager on most modern Linux distributions.

The focus is on **practical operational tasks**, not exhaustive reference.

## Audience

This guide is intended for:
- Developers deploying applications on Linux
- Operators and SREs managing services
- Technical users responsible for system reliability

## What is systemd?

A brief explanation of what `systemd` is and why it matters:
- Service lifecycle management
- Startup dependencies
- Logging and monitoring integration

## Common service management tasks

### Checking service status
- `systemctl status <service>`

What the output means and what to look for.

### Starting and stopping services
- `systemctl start <service>`
- `systemctl stop <service>`

When to use each.

### Restarting and reloading services
- `systemctl restart <service>`
- `systemctl reload <service>`

Difference between restart and reload.

### Enabling services at boot
- `systemctl enable <service>`
- `systemctl disable <service>`

## Inspecting logs with journalctl

### Viewing recent logs
- `journalctl -u <service>`

### Filtering logs
- By time
- By priority

## Common failure scenarios

- Service fails to start
- Service exits unexpectedly
- Permission-related failures

How to identify the root cause.

## Best practices

- When to restart vs reboot
- Logging considerations
- Safe troubleshooting steps

## Summary

Key takeaways and operational reminders.
