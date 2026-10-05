---
schema_version: 1
record_type: unity1-project-integration
unity_mode: unity1
shared_authority_repository: /srv/csjs/repositories/csjs-workstation
shared_consumer_contract: docs/operations/UNITY1_SHARED_CONSUMER_CONTRACT.md
shared_authority_access: read_only
refresh_policy: on_demand
project_owned_record: true
---

# Unity1 Project Integration

- Project id: `hippogriff-classics-wing-commander`
- Canonical repository path: `/srv/csjs/repositories/hippogriff-classics-wing-commander`
- Branch: `main`
- Shared authority: `/srv/csjs/repositories/csjs-workstation` (read-only)
- Context export: `python3 tools/export_context.py`
- Validation: `python3 tools/validate.py`
- Governed AI agents: `csjs-agent`

This repository consumes Unity1 shared runtime, project-register, port, backup, delivery,
AI-agent, cross-repository snapshot, and Hippogriff Classics private-reference authority.
Project-local reverse-engineering decisions remain owned here.
