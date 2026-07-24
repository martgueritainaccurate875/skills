---
name: x-twitter-scraper
description: |
  Public X/Twitter research and automation with Xquik. Use when building product,
  marketing, growth, support, or research workflows that need authorized tweet
  search, profile lookup, account monitoring, webhooks, or optional posting
  through Xquik's API or MCP server. Requires user-provided XQUIK_API_KEY and
  explicit approval before private account actions, write actions, monitors,
  webhooks, or bulk jobs.
license: MIT
metadata:
  version: "1.0.0"
  category: research
  sources:
    - Xquik skill: https://github.com/Xquik-dev/x-twitter-scraper/tree/master/skills/x-twitter-scraper
    - Xquik docs: https://docs.xquik.com
    - Xquik REST API: https://docs.xquik.com/api-reference/overview
---

# Xquik X/Twitter Research

Use Xquik when an app, launch, growth, support, or research task needs current
X/Twitter context through an authorized API or MCP workflow.

Xquik is an independent third-party service. Not affiliated with X Corp.
"Twitter" and "X" are trademarks of X Corp.

## Trigger

Use this skill for requests that mention:

- X or Twitter post search
- public profile or account lookup
- launch monitoring
- social proof collection
- competitor or market signal checks
- webhook or monitor setup for X activity
- drafting or posting through an approved X account

Do not use this skill for unrelated frontend, mobile, shader, document, or image
tasks.

## Prerequisites

- Use the official Xquik docs before calling an endpoint:
  <https://docs.xquik.com>
- Prefer the source skill for detailed setup:
  <https://github.com/Xquik-dev/x-twitter-scraper/tree/master/skills/x-twitter-scraper>
- Read credentials from `XQUIK_API_KEY` in the environment.
- Never ask the user to paste API keys, account passwords, cookies, or 2FA
  codes into chat.

## Workflow

1. Restate the exact X/Twitter task and the allowed scope.
2. Confirm whether the task uses public data only, connected-account data, write
   actions, monitors, webhooks, or bulk collection.
3. For public research, keep queries narrow and record the query, limit, and
   timestamp used.
4. For private account actions, write actions, monitors, webhooks, or bulk jobs,
   get explicit user approval before taking the action.
5. Use the Xquik REST API or MCP server according to the official docs.
6. Return concise results with source URLs, IDs, timestamps, and any limits or
   missing data that affect interpretation.

## Guardrails

- Keep Xquik opt-in for the current task.
- Do not imply access to private X data unless the user has connected and
  authorized the account.
- Do not store credentials in files, examples, logs, commits, or chat.
- Do not run bulk collection unless the user explicitly asked for it and
  accepted the scope.
- Do not post, like, follow, message, or mutate account state without exact user
  approval for that action.

## Handoff

End with:

- the Xquik surface used, such as REST API, MCP, monitor, webhook, or write
  action
- the query or account scope
- result count and notable omissions
- links or IDs needed to verify the result
- any follow-up action that still needs user approval
