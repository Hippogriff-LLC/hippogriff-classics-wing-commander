# Sprint 001 Completion — Private Projection Verification and Distribution Inspection

## Purpose

Complete Sprint 001 after the three owned Wing Commander-family archives were installed into the canonical private title tree.

This is a narrow completion run. Do NOT repeat the already-completed broad web research or MOO2 research unless necessary to reconcile a specific new finding.

Do NOT begin heavy decompilation or implementation.

## Required checks

### 1. Verify governed private projection

Confirm the governed run can see all three expected owned inputs:

- CSJS_Wing_Commander.zip
- CSJS_wcsecretmissions1.zip
- CSJS_wcsecretmissions2.zip

Record safe metadata sufficient to prove access, including filename, byte size, and SHA-256 if available.

Do not copy proprietary bytes into public Git.

### 2. Verify owned-workspace write access

The governed private workspace is expected to be writable.

Prove this by creating, reading back, and deleting a small marker file beneath the projected owned-workspace.

Record whether this succeeds.

If the workspace is unexpectedly read-only, treat that as an infrastructure blocker and report it clearly. Do not work around the governed boundary by writing private-derived material elsewhere.

### 3. Inspect the three owned distributions

Inspect the archive manifests and, where useful, extract only into the governed private writable workspace.

Determine enough concrete private evidence to complete the Sprint 001 questions concerning:

- base Wing Commander executable/data layout;
- Secret Missions 1 executable/data layout;
- Secret Missions 2 executable/data layout;
- shared versus distinct executable names;
- installation/layout relationship;
- shared versus expansion-specific data;
- evidence relevant to campaign selection/launch behavior;
- evidence relevant to whether SM1 behaves as base-engine content/variant and whether SM2 is a distinct executable/program variant;
- save/state continuity clues if visible from filenames/layout/configuration;
- version/build identifiers if safely observable;
- overlay/runtime format clues relevant to later decompilation;
- executable fingerprints/hashes for later provenance, kept private where necessary.

Do not perform large-scale decompilation.
Do not generate or promote mechanically recovered source.
Do not expose proprietary filenames/content in the public report beyond what is safe and necessary.

### 4. Reconcile Sprint 001 public report

Update:

docs/research/SPRINT_001_RESEARCH.md

Only where the newly available owned-distribution evidence materially changes or confirms the existing conclusions.

Explicitly distinguish:
- confirmed by our owned distributions;
- supported by public historical evidence;
- inference;
- still unresolved.

Update the Sprint 002 recommendation if necessary.

### 5. Update QA evidence

Update the existing Sprint 001 QA records as appropriate:

docs/qa/sprint-001/VALIDATION.md
docs/qa/sprint-001/access-and-toolchain.json
docs/qa/sprint-001/documentation-boundary-review.json

Record:
- all three private inputs projected successfully or not;
- owned-workspace writable successfully or not;
- private/public boundary result;
- project validation result.

Detailed proprietary inspection notes, hashes, extracted files, and title-derived working material belong only in the governed private workspace.

## Validation

Run:

python3 tools/validate.py

Run the canonical governed Classics public-boundary audit.

Do not commit or push.

Leave public changes uncommitted for project-thread review.

## Completion standard

The run succeeds only if:

- all three private archives are visible to the governed agent;
- owned-workspace write/create/read/delete succeeds;
- the three distributions are inspected enough to replace the missing private-evidence section of Sprint 001;
- the public research report is reconciled with that evidence;
- validation passes;
- public-boundary audit passes;
- no heavy decompilation/implementation is started;
- no proprietary material crosses into public Git.

If either private-input projection or owned-workspace writability still fails, stop and report the exact blocker rather than compensating around governance.
