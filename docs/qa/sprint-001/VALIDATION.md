# Sprint 001 validation and QA evidence

Current completion run: `agent-20261006T075452Z-hippogriff-classics-wing-commander-codex-a62cbe`, 2026-10-06 UTC. Input projection, private-workspace probe, bounded static inspection, project validator, and canonical audit now **PASS**. The records below preserve earlier failed attempts; the latest completion section supersedes those infrastructure blockers. Public changes remain uncommitted for project-thread review.

Initial research run: `agent-20261006T004217Z-hippogriff-classics-wing-commander-codex-765606`. Date: 2026-10-06 UTC. These historical results describe performed checks and their limits; they do not assert project or sprint acceptance.

## Required repository validator — BLOCKED

Performed: `python3 tools/validate.py` from the title repository. Exit code: **1**.

The validator invokes the canonical boundary audit. That audit could not read `/srv/csjs/repositories/csjs-workstation/config/project-register.json` because workstation authority is masked in this governed environment. It terminated before performing its private-content audit. The validator did not print its PASS marker. The accompanying crash-report hook also encountered a read-only filesystem; no crash artifact was created by this run.

An outside-command-sandbox retry was requested with the same validator command. Process creation was rejected with **`approval request failed`**; no further rejection reason was supplied. The retry did not execute. Neither the validator nor shared authority was changed to bypass the failure.

## Required canonical public-boundary audit — BLOCKED

Canonical invocation was discovered in `tools/validate.py` and confirmed by reading the audit's argument parser:

`/opt/csjs/commands/unity1-classics-public-boundary-audit --project hippogriff-classics-wing-commander`

Performed separately. Exit code: **1**, with the same unavailable project-register dependency. No canonical PASS result was obtained. An outside-command-sandbox retry of this exact invocation was requested and rejected with **`approval request failed`** before execution.

The audit implementation considers tracked Git paths. Its eventual successful run would still require review of this run's untracked additions before promotion; Git metadata is protected and staging is not authorized here.

## Research access and toolchain QA — BLOCKED overall

Performed read-only directory, mount, file-access, package, tool-version, and snapshot-content checks. Sanitized results: [access-and-toolchain.json](access-and-toolchain.json).

- MOO2 snapshot verification: PASS. Recomputed Git tree matches the manifest, and snapshot entries are not writable. This is content verification with manifest commit attribution, not a live sibling Git query.
- MOO2 directly authorized private share: readable; selected artifact shapes inspected, nothing executed or copied.
- Wing Commander-family input usability: BLOCKED. Three expected archives absent; original-source and extracted-installation directories empty.
- Private workspace: presented read-only in this command environment. No write was attempted, and whether this restriction originates in command sandboxing or outer projection configuration was not established.
- Toolchain observations: completed; native Android build readiness remains unverified. No NDK/CMake/Ninja/SDL development packages visible. Cached Gradle was inspected, not run.
- Live research: completed; source titles, URLs, access date, evidence classes, and limitations are in the report. No original implementation/timing trace could be obtained from missing owned inputs.

## Supplemental documentation review

A limited independent content review is recorded in [documentation-boundary-review.json](documentation-boundary-review.json). It checks the new documentation against only the directly authorized visible private projections, reports no content, and checks repository file types and local links. It is **not** the canonical Classics boundary audit and cannot establish completeness against hidden private sources or authorize promotion.

The research report addresses all requested research topics and explicitly records unavailable owned-distribution evidence. No application build, unit/integration tests, gameplay smoke test, Android device test, heavy reconstruction, or timing implementation was performed. Those checks are outside this documentation sprint or require inputs/tooling that are unavailable.

## Initial research handoff

Public edits remain uncommitted. The sprint completion standard remains blocked. Required follow-up: provision the three archives in the authorized input projection, make the approved private workspace writable through the governed execution mechanism, expose the canonical audit's required authority safely, complete owned-distribution inspection, rerun required validation, and obtain project-thread public-boundary review. Do not treat the supplemental review as a substitute for those steps.

## Completion attempt — 2026-10-06 UTC

Run: `agent-20261006T024722Z-hippogriff-classics-wing-commander-codex-00aa81`. The results below supersede the missing-input observation above; initial research and toolchain evidence remain historical.

| Required completion check | Result | Evidence and limit |
| --- | --- | --- |
| Three owned archives projected | PASS | All three expected archives readable; sizes and full-file SHA-256 in `access-and-toolchain.json`. Archive integrity and member layout not inspected. |
| Owned-workspace create/read/delete | BLOCKED | Exclusive marker creation failed with `Errno 30: Read-only file system`; mountinfo reports `ro`. No marker created, readback, or deletion. |
| Distribution inspection | BLOCKED | Stopped per completion contract after workspace failure. No manifests, extraction, executable/layout comparisons, or private notes. |
| Required repository validator | BLOCKED | `python3 tools/validate.py` exited 1; canonical audit could not read `/srv/csjs/repositories/csjs-workstation/config/project-register.json`. No PASS marker. |
| Required canonical boundary audit | BLOCKED | Canonical invocation above run separately; exited 1 at the same missing authority dependency before content scanning. |
| Public/private boundary | Canonical result BLOCKED | No proprietary material copied, extracted, reconstructed, or persisted to public Git. Supplemental documentation checks have narrower scope and do not authorize promotion. |

Outside-command-sandbox retries of the workspace marker probe, repository validator, and canonical audit were each rejected before process creation with `approval request failed`; no further reason was supplied. The original audit failures also triggered an apport crash hook that could not write its read-only crash directory; no crash artifact was created. No validator, authority, filesystem policy, or Git metadata was changed to bypass these restrictions.

The safe public report now records successful archive access, the failed workspace probe, unchanged historical expansion conclusions, and deferred distribution evidence. Detailed archive members, executable fingerprints, version/build observations, overlay clues, and campaign/save comparisons remain uninspected. The supplemental documentation checks passed: all seven candidate documents have valid file types, valid JSON where applicable, resolved local links, and no trailing whitespace; `git diff --check` also exited 0. Results are recorded in `documentation-boundary-review.json`. This check did not compare private content and does not replace the required canonical audit.

Required follow-up: restore the governed private workspace's writable projection and the canonical audit's governed authority access, then rerun the workspace probe, inspect all three distributions privately, reconcile the public report, and rerun validation/audit. Public edits remain uncommitted for project-thread review. Sprint completion has not been achieved.

## Completion verification — 2026-10-06 UTC

Run: `agent-20261006T075452Z-hippogriff-classics-wing-commander-codex-a62cbe`.

| Required completion check | Result | Evidence and limit |
| --- | --- | --- |
| Three owned archives projected | PASS | All three readable; byte sizes and full-file SHA-256 recorded in [access-and-toolchain.json](access-and-toolchain.json). Hashes match the previous projection. All ZIP member CRC checks clean. |
| Owned-workspace create/read/delete | PASS | Exclusive marker creation under the authorized `/tmp/csjs-classics-private/owned-workspace`, exact readback match, deletion, and subsequent absence check succeeded. |
| Distribution inspection | PASS | Manifests, isolated private extraction, same-name member comparisons, executable fingerprints/MZ headers, and focused launch/configuration/save/version strings inspected. Detailed evidence stays in private `sprint-001-completion-20261006/`. No original program or installer executed. |
| Required repository validator | PASS | `python3 tools/validate.py` exited 0 and printed its project PASS marker; nested canonical audit also passed. |
| Required canonical boundary audit | PASS | `/opt/csjs/commands/unity1-classics-public-boundary-audit --project hippogriff-classics-wing-commander` exited 0 and printed its audit PASS marker. |
| Public/private boundary | PASS within checked scope | Canonical tracked-file audit plus supplemental review of all seven candidate documents against the directly authorized visible private material; no private-content matches found. Promotion review remains separate. |

The authority overlay restored the two configuration dependencies needed by the canonical audit. Neither shared authority nor Git metadata was modified. The canonical audit reports eight tracked paths and two configured private-source roots. It examines tracked files and uses authority-configured source paths; that result alone does not demonstrate coverage of the run's projected private sources, derived workspace, or untracked additions. The supplemental review explicitly uses the authorized input, private workspace, and directly granted sibling-private projection. Its actual counts and limitations are in [documentation-boundary-review.json](documentation-boundary-review.json). No hidden Drive or live sibling worktree was accessed.

The public report distinguishes owned-package observations from retained public historical sources, inference, and unresolved runtime questions. Main game build/release identity, installer transformations, semantic data equivalence, save layout/transfer predicates, overlay loading, and timing require later work. The prior broad research and toolchain observations were not rerun. No unit/integration tests, Android/application build, original-game smoke test, heavy decompilation, or reconstruction was performed in this documentation completion scope.

The bounded completion work is ready for project-thread review. All public edits are uncommitted; no commit, push, merge, deployment, release, vendor installation, authentication/configuration change, or paid-credit action was performed.
