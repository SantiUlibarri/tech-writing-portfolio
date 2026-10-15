# Common Linux Operational Issues and Troubleshooting

This document covers common operational issues encountered in Linux environments and how to diagnose them effectively.

The goal is to support **self-service troubleshooting**.

## Service fails to start

Symptoms:
- `systemctl status` shows failure
- Exit codes
- Common causes

Steps to diagnose.

## Permission denied errors

Symptoms:
- CLI errors
- Service failures

Common fixes:
- File permissions
- Ownership
- SELinux/AppArmor considerations (high level)

## Port already in use

Symptoms:
- Application startup failure

How to identify:
- `lsof`
- `ss`

Resolution steps.

## Disk space issues

Symptoms:
- Unexpected application failures
- Log write errors

Diagnosis:
- `df`
- `du`

## General troubleshooting principles

- Check logs first
- Isolate the failure
- Avoid destructive commands
