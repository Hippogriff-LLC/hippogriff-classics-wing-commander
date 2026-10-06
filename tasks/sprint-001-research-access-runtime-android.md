# Sprint 001 — Research, Access Verification, Runtime Behavior, and Android Port Direction

## Project

Hippogriff Classics — Wing Commander

Primary title:
- Wing Commander

Expansion content owned by this same project:
- Secret Missions 1
- Secret Missions 2

Modern target direction:
- Recover/reconstruct the actual original DOS implementation.
- Recompile/reconstruct it as a genuinely portable native core.
- Make Android the first modern playable host target for Wing Commander.
- Keep the recovered core portable enough to support later native and/or WASM hosts.

This is not an inspired-by rewrite.
DOSBox/emulation may be used for investigation/reference, but is not the final architecture.

## Sprint character

This is a RESEARCH sprint.

Do not begin large-scale decompilation/reimplementation.
Do not generate a large body of mechanically recovered source.
Do not spend the run trying to produce a playable build.

The purpose is to establish evidence, verify governed access, understand the title/runtime/expansion constraints, study the successful MOO2 precedent, assess Android host options, and record findings so the later heavy reverse-engineering sprint begins from a strong factual foundation.

Use your own technical judgment about how to investigate. Do not follow a canned subsystem sequence merely because it is conventional.

## 1. Prove Wing Commander private-input access

Verify that the governed environment exposes this title's canonical private material read-only.

Expected project-owned private inputs:
- CSJS_Wing_Commander.zip
- CSJS_wcsecretmissions1.zip
- CSJS_wcsecretmissions2.zip

Establish that all three are visible and usable from the governed run.

Inspect them sufficiently to understand what distributions/installations they contain and what executable/data layout will be available for later reverse engineering.

You may perform lightweight inspection/extraction into the governed writable private workspace when useful.

Do NOT copy proprietary material into public Git.

Do NOT publish original bytes, executable contents, proprietary assets, mechanically reconstructed source, executable-derived builds/images, or other protected title-derived material.

Record private-sensitive observations only in the governed private writable workspace when necessary.

The safe public research report should state whether access succeeded and summarize useful high-level facts without reproducing proprietary content.

## 2. Prove MOO2 sibling-repository access and study its techniques

Find the governed immutable read-only snapshot of:
- hippogriff-classics-moo2

Verify:
- the snapshot is accessible;
- it is read-only;
- its exact committed SHA;
- the important repository files documenting or implementing the reverse-engineering/decompilation/static-recompilation approach used there.

MOO2 successfully progressed from original DOS implementation investigation toward a portable native/WebAssembly architecture.

Study the actual MOO2 repository rather than relying on generic assumptions.

Identify techniques, tooling, architecture decisions, validation patterns, and reverse-engineering lessons that may transfer to Wing Commander, including where present:
- executable analysis;
- decompilation;
- static recompilation;
- recovery of structures/globals/functions/algorithms;
- executable/data boundary handling;
- DOS/runtime compatibility replacement;
- portable native-core design;
- behavior comparison against the original;
- public/private separation of proprietary recovered material and independently authored code;
- WASM/native portability.

Explicitly distinguish:
1. MOO2 techniques likely reusable for Wing Commander;
2. techniques that are game-specific and should not simply be copied;
3. new questions Wing Commander requires us to answer.

Do not modify the MOO2 snapshot.

## 3. Live web research — original Wing Commander runtime/timing problems

Use live public-web research and record source URLs/titles plus access date.

Research the historical runtime/timing behavior of original DOS Wing Commander, including reports that gameplay behavior became CPU-speed dependent on later/faster systems.

Do not assume the operator's initial description is technically exact. Determine the real mechanism from evidence.

Investigate as applicable:
- CPU-speed-dependent gameplay;
- delay/busy loops;
- simulation/game-loop timing;
- PIT/timer/tick dependencies;
- animation/input timing;
- combat speed;
- sound timing if relevant;
- failures on faster processors;
- historical official patches;
- fan/community fixes;
- later-release compatibility fixes;
- source-level fixes if any source-port or reimplementation evidence is useful;
- emulator workarounds only insofar as they reveal the underlying intended behavior.

The core research question is:

What timing behavior did the original implementation intend, what implementation choices made it hardware-dependent, and how should a reconstructed portable native implementation preserve intended behavior without preserving the hardware-speed bug?

Identify known fixes and the technical principle behind them.

Where evidence permits, assess reconstruction approaches such as:
- fixed or semi-fixed simulation timestep;
- explicit elapsed-time accounting;
- reproduction of DOS timer ticks;
- throttled main-loop timing;
- another evidence-supported mechanism.

Do not implement a timing system in this sprint.

Clearly distinguish verified facts, strong inference, community reports, and unresolved claims.

Prefer primary/technical sources where available and corroborate community preservation sources when practical.

## 4. Secret Missions 1 and 2 integration research

Research how these original DOS products relate technically:
- Wing Commander
- Secret Missions 1
- Secret Missions 2

Use BOTH:
1. evidence obtainable from our three owned private distributions; and
2. public historical/technical sources.

Determine as far as evidence permits:
- installation model;
- executable model;
- whether expansions patch/replace/share the base executable;
- whether separate executables exist;
- shared versus expansion-specific data;
- save-game/state continuity;
- campaign/progression relationship;
- installation-directory relationship;
- launch/entry-point behavior;
- relevant version differences;
- whether SM1/SM2 are technically content packs, engine variants, separate program variants, or a combination.

Do not expose proprietary contents in the public report.

Assess what this means for the modern architecture.

Preferred modern user experience:
- one Wing Commander Android application containing the base campaign plus Secret Missions 1 and Secret Missions 2;
- preserve original behavior/content boundaries where technically meaningful;
- avoid three unrelated applications unless evidence makes that necessary.

Do not force a conclusion if evidence is incomplete.

## 5. Android native-port architecture research

The target is a decompiled/reconstructed/recompiled native port, not a JavaScript recreation.

Investigate an appropriate Android host architecture around a portable recovered native core.

The operator has no predetermined preference between a directly built Android application and an Expo/React Native application.

Unity1 can build Android applications directly and can also support Expo/React Native workflows.

Inspect the CURRENT Unity1 environment without installing or mutating global tooling. Record what is already available, where relevant:
- Java/JDK;
- Android SDK;
- Android NDK;
- Gradle;
- CMake;
- Ninja;
- Node/npm;
- React Native / Expo tooling;
- SDL or other useful native host dependencies/tooling;
- existing Android build conventions visible through approved read-only sibling snapshots if useful.

Compare realistic approaches, including at least:

A. Portable C/C++ recovered core + Android NDK/native application host.

B. Portable C/C++ recovered core + thin Kotlin/Java Android host.

C. Portable native core + SDL or similar cross-platform native host layer if technically appropriate.

D. React Native / Expo application shell with a native module/core underneath, but only if that genuinely improves the product/engineering model.

Do not choose Expo merely because it is convenient for ordinary mobile applications.

Evaluate options against:
- fidelity;
- performance;
- audio;
- graphics/framebuffer presentation;
- touch input;
- keyboard/controller support;
- filesystem/save data;
- app lifecycle/pause/resume;
- packaging or importing user-owned game data;
- debugging;
- testability;
- Unity1 build reproducibility;
- later desktop/WASM portability;
- unnecessary framework complexity.

Make a recommendation, preserving uncertainty where evidence warrants it.

## 6. Research outputs

Create one primary SAFE public research report:

docs/research/SPRINT_001_RESEARCH.md

It should contain:
1. Executive findings.
2. Wing Commander private-input access verification.
3. MOO2 sibling snapshot verification and exact SHA.
4. Exact public MOO2 paths consulted.
5. Transferable MOO2 reverse-engineering techniques.
6. Wing Commander runtime/timing research.
7. Known historical fixes and reconstruction lessons.
8. Secret Missions 1/2 technical integration findings.
9. Android architecture comparison.
10. Current Unity1 Android-toolchain observations.
11. Recommended direction for Sprint 002.
12. Open questions / unresolved evidence.
13. Web bibliography with URLs, source titles, and access date.

If detailed proprietary/title-derived notes are necessary, place them only beneath the governed private writable workspace, e.g.:

derived/agent-workspace/sprint-001/

Do not put private-derived artifacts in public Git.

The public report may contain safe reverse-engineering knowledge and independently authored conclusions.

## 7. Boundary and scope constraints

This repository is the only writable Git repository.

Approved sibling repositories are immutable read-only exact-SHA snapshots.

Do not attempt to mutate MOO2 or any other sibling.

Do not access hidden sibling live worktrees.

Keep title-private material private.

Do not commit or push changes during this run.

Because private references are mounted, leave public-repo changes uncommitted for project-thread review.

Before completion run:

python3 tools/validate.py

and run the governed Classics public-boundary audit:

unity1-classics-public-boundary-audit

If the audit requires project/path arguments, discover and use the canonical governed invocation rather than guessing.

Record validation and audit results.

## 8. Completion standard

This sprint succeeds only if the report demonstrates, with evidence:
- all three Wing Commander-family private inputs are accessible;
- the immutable MOO2 sibling snapshot is accessible and its exact SHA is identified;
- specific useful MOO2 files/techniques were actually inspected;
- live web research succeeded and is cited;
- the Wing Commander timing/runtime issue is materially better understood;
- SM1/SM2 integration is materially better understood;
- Android architecture options are assessed against the native-core objective;
- current Unity1 Android-build capability is inspected;
- a reasoned Sprint 002 recommendation exists;
- no heavy implementation/decompilation was prematurely started;
- proprietary/private material did not cross into public Git.
