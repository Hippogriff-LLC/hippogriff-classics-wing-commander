# Sprint 001 — Wing Commander research, access, timing, expansions, Android

Research date: 2026-10-05 America/New_York / 2026-10-06 UTC. Web access date: **2026-10-06 UTC** throughout. Scope: research only; no game build, heavy decompilation, timing implementation, commit, or release action.

## 1. Executive findings

**The bounded completion checks now pass:** all three owned archives are readable, private-workspace create/read/delete succeeds, distribution inspection is complete at the requested static scope, and the project validator and canonical boundary audit pass. Safe access metadata is recorded in [access evidence](../qa/sprint-001/access-and-toolchain.json); detailed manifests, extracted files, executable fingerprints, and observations remain private. The findings support a base/SM1 launch through `WC` and a distinct SM2 program through `SM2`, with shared data and separate SM2 configuration/save references. Static evidence does not establish gameplay, installer effects, or timing correctness. Public changes remain uncommitted for project-thread boundary review; audit coverage and supplemental review are described in [QA](../qa/sprint-001/VALIDATION.md).

The MOO2 snapshot is accessible, immutable, and matches its pinned Git tree. Its actual recompiler/runtime/test architecture was inspected. Ahead-of-time translation, narrow host services, explicit diagnostics, synthetic tests, and private build segregation transfer well. Its symbol-bearing 32-bit LE loader does not establish an appropriate Wing Commander loader.

The timing problem is more specific than a single CPU-clock dependency: the DOS patch author's investigation identifies differently implemented scenes, hardware-sensitive joystick routines, and cutscenes requiring individual timing corrections. Public evidence supports replacing throughput-dependent pacing with explicit time, but does not establish the owned DOS executable's simulation quantum, PIT programming, or exact loop structure. [WCAT author discussion](https://www.wcnews.com/chatzone/threads/w-c-a-t-wc1-dos-overhaul-mod-beta-v0-8-r4-released.32327/)

Recommend a portable C/C++ core, a separately testable host interface, and an Android application using a pinned SDL host plus a small Java/Kotlin integration layer. A direct GameActivity host remains a credible alternative. Expo adds little to the current game-focused scope. Static owned-input evidence supports this program/host separation; the host choice remains provisional until a synthetic host experiment is performed.

## 2. Wing Commander private-input access verification

Completion verification: **2026-10-06 UTC**, run `agent-20261006T075452Z-hippogriff-classics-wing-commander-codex-a62cbe`. This supersedes the previous completion attempt's workspace and audit blockers; earlier observations remain in the QA history.

Authorized input: this run's `classics-private/owned-input` projection. Authorized writable workspace: `/tmp/csjs-classics-private/owned-workspace`.

| Required input/check | Observation | Result |
| --- | --- | --- |
| `CSJS_Wing_Commander.zip` | Readable; 3,336,305 bytes; full-file SHA-256 recorded; ZIP CRC check clean | PASS |
| `CSJS_wcsecretmissions1.zip` | Readable; 753,970 bytes; full-file SHA-256 recorded; ZIP CRC check clean | PASS |
| `CSJS_wcsecretmissions2.zip` | Readable; 909,334 bytes; full-file SHA-256 recorded; ZIP CRC check clean | PASS |
| Owned-workspace | Exclusive marker created, read back with exact payload match, deleted, and absence checked | PASS |
| Distribution inspection | Manifests, isolated extraction, overlapping-member comparisons, MZ headers, and focused launch/configuration/save/version strings | PASS at static scope |

All archive hashes match the previous projection observations. CRC checks establish readable ZIP members, not authenticity of a retail release. Extraction stayed beneath `owned-workspace/sprint-001-completion-20261006/`, with separate base/SM1/SM2 trees and path/symlink checks. Full member lists, raw strings, configuration contents, original bytes, executable/member hashes, and detailed comparison records are private. The public report contains independently written conclusions and safe access metadata only.

No installer, original game, transfer tool, or auxiliary executable was run. No disassembly, heavy decompilation, implementation, generated source, or playable build was started. Hidden CSJS Drive and live sibling worktrees were not searched. The minimal read-only workstation authority overlay now permits the canonical validator/audit to run; it was not modified.

## 3. MOO2 snapshot verification

Prior research snapshot: `agent-20261006T004217Z-hippogriff-classics-wing-commander-codex-765606/read-snapshots/hippogriff-classics-moo2` beneath the governed run-artifact root. The following verification and inspection were performed in that initial research run, not repeated in the completion run. The completion grant pins the same MOO2 commit.

- Ref: `refs/heads/main`.
- Exact commit: **`481bc73ed1e01e203fffdec9c3e9c05e8d430c59`**.
- Manifest tree: `5e0c3be8828e0b29d4af5341e5a022b8924927d5`.
- Independently recomputed Git tree from snapshot file bytes and executable modes: **same tree**. Hashing used Git object framing without writing Git objects or metadata.
- Snapshot root mode: `0555`; no descendant has write permission bits; effective root write access false. No write test or mutation was attempted.

The commit/ref association comes from the governed run manifest; the independently recomputed tree verifies the materialized content. The snapshot has no live Git history to query. These are distinct evidence sources, not a claim that a local `git rev-parse` verified the commit.

The directly authorized private MOO2 reconstruction share was also readable. Inspection was limited to artifact availability and generated-code shape: generated dispatch and translated code exist alongside a native artifact. Nothing was copied or executed. No recovered MOO2 functions, addresses, byte sequences, or generated source are reproduced here.

The title's `AGENTS.md`, README, governance documents, sprint, and validator were read. During initial research, workstation authority and its referenced consumer contract were unavailable; their contents were not inferred. This completion run exposes only the authorized minimal read-only authority overlay for validation/audits, rather than the live Control worktree or full consumer contract. The approved shared Classics snapshot's instructions and governance corroborate the platform/title and public/private boundaries.

## 4. Exact public MOO2 paths consulted

All paths below are relative to the pinned MOO2 snapshot. Larger implementation files were read selectively around relevant interfaces and algorithms.

| Paths | Evidence obtained |
| --- | --- |
| `AGENTS.md`, `docs/architecture/ARCHITECTURE_BOUNDARY.md`, `provenance/RECOMPILER.md` | Governance, client compute boundary, independent tools versus private generated artifacts |
| `docs/research/RECOMPILATION.md` | Actual strategy, tested behavior, approximation and coverage limits |
| `src/recomp/le.ts`, `src/recomp/watcomdbg.ts` | LE loading/relocations and Watcom symbol recovery |
| `src/recomp/x86.ts`, `src/recomp/analyze.ts`, `src/recomp/emit-c.ts`, `src/recomp/layout.ts` | Decoder assumptions, control flow, C emission, dispatch, platform overrides |
| `tools/re/recompile.ts`, `tools/port-build-lib.mjs` | Output boundary enforcement and executable/source/toolchain fingerprints |
| `runtime/host.h`, `runtime/pc.c`, `runtime/rt.c`, `runtime/native.mk`, `runtime/wasm.mk` | Host contract, time/hardware services, common core across build targets |
| `tests/recomp.test.ts`, `tests/runtime.test.ts`, `tests/port.test.ts` | Synthetic executable tests, runtime/input/audio and build freshness checks |
| `tools/smoke.mjs`, `src/port/worker.ts`, `src/port/store.ts` | Behavior smoke coverage, thread boundaries, input/audio diagnostics, local saves |
| `docs/research/SPRINT002_HUMAN_ANDROID_ACCEPTANCE_20261004.md` | Real Android Chrome acceptance and background/audio caveats |

MOO2 tests and binaries were studied, not rerun. Their recorded successes remain sibling evidence, not Wing Commander validation.

## 5. Transferable MOO2 techniques

### Reusable methods

MOO2 mechanically translates instructions to portable C ahead of time, preserving guest registers, memory, flags, call behavior, and original data structures. This gives an executable-grounded route to fidelity before replacing individual routines with understood native logic. It is not original high-level source recovery: recovered function boundaries and names do not imply recovered types or algorithm specifications.

Its analyzer combines symbols, direct calls, tail jumps, relocation-backed code pointers, and switch-table discovery. Unknown indirect targets trap with diagnostics. Reuse the evidence-driven discovery and explicit failure principles; avoid treating undiscovered code as harmless. Preserve original arithmetic width, signedness, memory aliasing, and state layouts while recovering semantic meaning.

`runtime/host.h` isolates files, monotonic time, palette/frame presentation, events, audio, and diagnostics. Native and WASM builds use the same translated program/runtime with different hosts. Wing Commander should likewise avoid Android APIs inside recovered game logic. A headless host with injected time and scripted input would let Android presentation evolve independently of reconstruction.

MOO2 uses private initial memory images/generated C and user-local game files, with writable saves separated from installation data. Build fingerprints track executable, translation sources, extra entries, and compiler inputs. Public tests use an independently hand-assembled synthetic executable and compile its translation to check actual results. Transfer those provenance, reproducibility, and synthetic-test practices.

The documented behavior checks exercise menus, saves, turns, combat, and captured audio; they distinguish paths exercised from completeness. Input and audio counters expose lost events and starvation. Wing Commander needs analogous evidence for continuous flight, not merely a successful title screen. Original-art frames, original saves, diagnostic memory dumps, and generated builds stay private.

### MOO2-specific choices not to copy

The loader and function discovery rely on a Watcom 32-bit LE program with abundant debug information. The decoder defaults to 32-bit operands/addresses; support for prefixed forms does not make it a general 16-bit segmented-program recompiler. DOS/4GW, DPMI selectors, memory placement, HLE overrides, VESA banking, Miles driver handling, and LBX/save names are title-specific assumptions.

MOO2's runtime charges approximate virtual time at execution polling points and synchronizes idle execution to host time. Its own report says animation timing was not calibrated against original hardware. That is a useful deterministic investigation model, not evidence that the same policy fixes Wing Commander's timing. The Android acceptance record is a **WASM program in Chrome**, not an NDK application. It also records guest time continuing while hidden and audio starvation increasing: explicit app suspension must be part of our host contract.

### New Wing Commander questions

The WCAT author's account explicitly mentions modifying Borland VROOMM overlay relocations. Owned WC/SM2 headers now confirm DOS MZ images with appended `FBOV`-marked regions, and both contain Borland compiler/runtime attribution. Together these support the Borland overlay hypothesis; the overlay schema and loading behavior remain unparsed. Overlay loading, far transfers, relocation, and potentially reused addresses are a high-value investigation frontier. Select a loader after that targeted investigation. Also determine whether symbols survive, how campaign variants share code/state, where simulation and scene pacing diverge, and which DOS/hardware/audio interfaces actually need replacement. [Author's implementation account](https://www.wcnews.com/chatzone/threads/w-c-a-t-wc1-dos-overhaul-mod-beta-v0-8-r4-released.32327/)

## 6. Original DOS runtime and timing

| Evidence class | Finding | Limit |
| --- | --- | --- |
| Primary technical testimony | WCAT's author added blank-synchronized pacing across differing scenes and corrected hardcoded cutscenes; also replaced hardware-sensitive joystick routines | Patch-author account, not an inspection of our owned binaries |
| Primary original documentation | SM1 installation offers compressed files to save space or expanded files for faster operation | Confirms workload affects performance; does not establish update mathematics |
| Primary emulator documentation | DOSBox cycles adjust emulated instruction throughput | A cycle setting is not a canonical simulation tick or precise MHz conversion |
| Community preservation guidance | CIC recommends constrained DOSBox cycles for WC1 and both expansions | Useful reference setup; not a universal fidelity calibration |
| Unresolved | Exact busy-loop sites, timer IRQ rates/divisors, BIOS-tick use, update quantum, and render/simulation coupling | Requires owned-binary analysis and controlled measurements |

[WCAT author's account](https://www.wcnews.com/chatzone/threads/w-c-a-t-wc1-dos-overhaul-mod-beta-v0-8-r4-released.32327/), [Origin SM1 reference card](https://www.scribd.com/document/759914554/Wing-Commander-The-Secret-Missions-Reference-Card), [DOSBox Performance](https://www.dosbox.com/wiki/Performance), [CIC technical support](https://www.wcnews.com/techsupport.shtml).

**Strong inference:** some behavior advances according to execution/scene work rather than a uniformly enforced independent clock. Increasing throughput can accelerate action or animation, while a crowded scene or decompression can reduce throughput. That explains why whole-machine slowing can help a quiet scene but degrade a busy mission. It does not prove every subsystem is frame-counted or that the original has no timer interrupts.

The source-supported intended behavior is stable, playable flight/control and correctly paced scenes across hardware. There is insufficient evidence here to assign a single historical FPS or simulation rate. Avoid asserting that a particular 386 model defines the specification. Capture empty flight, crowded combat, input response, cutscene duration, and sound-event relationships at several controlled reference speeds, then identify which differences are bugs versus intended behavior.

Busy waits, PIT/BIOS ticks, retrace polling, loop counters, and elapsed-time scaling remain separate hypotheses to test. A timer-controlled music service can coexist with CPU-sensitive flight. WCAT reports an AdLib hanging-note fix, but this does not prove a timer-rate cause. No audio or original gameplay was run in this sprint. [Current WCAT author description](https://alltinker.itch.io/wcat)

## 7. Historical fixes and reconstruction lessons

| Approach | Technical principle and status | Reconstruction lesson |
| --- | --- | --- |
| DOSBox throughput cap | Limits emulated work per interval; emulator documentation confirms the mechanism | Use as a reference control, not the native architecture |
| Hardware slowing / TSR / cache adjustments | Community workarounds reduce execution throughput; timing behavior depends on scene load | Workarounds reveal sensitivity but cannot define one correct clock |
| WCAT DOS overhaul | Author documents scene-specific pacing corrections; first public discussion June 2025, current author page lists WC1 1.0.1 | Study pacing principles; do not import its byte patches or optional gameplay changes |
| Kilrathi Saga and WCDX | A later Windows program lineage; WCDX replaces graphics interfaces/privileged operations and supports expansion executables | Compatibility and behavior fixes are version-specific |
| Recent SDL2 reconstruction | `neuromancer/wc1-re` describes a C/C++ reconstruction of the 1996 Windows release with partial DOS-data support | Useful documented comparator, not proof of DOS implementation identity |

[DOSBox](https://www.dosbox.com/wiki/Performance), [WCAT author page](https://alltinker.itch.io/wcat), [WCDX maintainer README](https://github.com/Bekenn/wcdx), [wc1-re maintainer README](https://github.com/neuromancer/wc1-re).

No universal Origin DOS CPU-speed patch was confirmed in the consulted sources. Nor was the community claim that SM2 fully fixed speed sensitivity verified. The original SM2 card establishes a calibration feature and separate launch, not a general speed limiter. Do not conflate WC2, SM2, Kilrathi Saga, or fan fixes. The external reconstruction's completeness and machine-code similarity claims are author-reported; they were not independently tested, and no reconstructed source was downloaded or adopted.

**Proposed timing direction, not implemented:** preserve recovered update order and integer/fixed-point semantics, while making time an explicit core input. If updates are per iteration, test a calibrated fixed update quantum and elapsed-time accumulator. If the original already scales by elapsed ticks, preserve that scheme and replace its clock faithfully. A semi-fixed policy is appropriate only if subdividing updates preserves original behavior. Reproduce DOS/PIT ticks for routines that demonstrably observe them; BIOS tick emulation alone cannot fix unrelated busy loops. A throttled loop may be the least invasive first comparator but can retain scene-load slowdowns.

Presentation should independently fit the device's display rate. Waiting on every Android display refresh would recreate a hardware dependency on 60/90/120 Hz devices. Android's frame-pacing library addresses presentation scheduling, not recovery of our historical simulation rate. [Android Frame Pacing](https://developer.android.com/games/sdk/frame-pacing)

## 8. Secret Missions integration

The first table summarizes **public original documentation**. Owned-distribution observations follow separately.

| Aspect | Base / SM1 | SM2 |
| --- | --- | --- |
| Installation | SM1 targets the base drive/directory and matching graphics configuration | Same base directory; hard-disk play required; matching graphics/sound configuration |
| Launch | `WC`; SM1 adds a campaign choice alongside Vega and continuation | `SM2`; `WC` continues to launch base/SM1 |
| Installer behavior | Normal add-on installation preserves base games/saves; reconfiguration has additional caveats | Installation says base/SM1 and existing saves are unaffected |
| Program model | Shared launch and campaign-aware behavior | Separate launch/program variant |
| Campaign state | SM1 transfer utility imports an eligible base pilot, retaining rank/medals, and replaces a selected save slot | Public WCAT launcher supports inter-campaign transfer; exact original SM2 transfer rules remain unverified here |

[Origin SM1 reference card](https://www.scribd.com/document/759914554/Wing-Commander-The-Secret-Missions-Reference-Card), [Origin SM2 reference card](https://pt.scribd.com/document/393839832/Wing-Commander-The-Secret-Missions-2-Reference-Card), [WCAT launcher description](https://alltinker.itch.io/wcat).

The SM1 card also instructs a new campaign to be saved/reloaded before play, and warns that transfer overwrites a slot. Treat those as version-sensitive initialization/continuity behaviors to investigate, not instructions to silently reproduce destructive transfer UX. The DOS base reference card independently lists the SM1 campaign option. [Origin DOS reference card](https://www.mocagh.org/origin/u6wc-alt-wc-refcard.pdf)

**Confirmed by our owned distributions (static inspection):**

| Question | Observed evidence | Interpretation and limit |
| --- | --- | --- |
| Base layout | Installed-style directory with `WC.EXE`, configuration, shared data directory, base and SM1-numbered campaign families, a save file, and a transfer utility | The provided base tree already contains SM1-related material; it is not a clean base-only comparison baseline |
| SM1 layout and launch | Flat installer payload; no replacement `WC.EXE`; installer references the existing base installation, base program/configuration, shared data directory, and `WC` launch | Supports base-engine content/variant integration; does not exclude in-place executable patching without an installer trace |
| SM2 layout and launch | Flat installer payload containing a distinct `SM2.EXE`, installer, transfer utility, and additional campaign/presentation data; installer identifies `SM2` launch | Confirms a separately supplied game program, rather than only new mission data |
| Shared versus specific data | Some base/SM1 same-name members are byte-identical, others differ; SM2 adds numbered campaign data and separate presentation/communications resources while referencing shared data | Expansion archives are add-on payloads, not demonstrated standalone installations; full manifests and comparisons stay private |
| Installation representations | Installer text offers compressed versus expanded storage and graphics conversion; multiple overlapping payloads differ in size/hash | Raw differences do not establish semantic content differences; normalization and actual installation effects remain unresolved |
| Campaign/save continuity | Base and SM1 have byte-identical transfer utilities; SM2 has a distinct utility referencing both base/SM1 and SM2 saves. WC and SM2 reference different configuration/save names | Supports deliberate inter-campaign transfer with separate SM2 persistent state; binary layouts and round trips remain untested |
| Runtime/overlay clues | Both game programs have MZ relocation tables, appended `FBOV` markers at their declared MZ image ends, and Borland compiler/runtime attribution | Consistent with the public Borland overlay account; no overlay loader or executable-derived implementation was recovered |
| Build/version identity | Transfer utilities have a nearby `1.7` version token; main-program version arguments were not identified. Installer `3.0` text describes EMS, not the game build | Utility token is a static version clue, not a verified runtime display. No retail/Deluxe/digital lineage or main game version is assigned |

**Inference:** the supplied base program is prepared for SM1, and the expansion's installation/configuration/data choices determine the usable campaign variant. The partly overlapping SM1 data and auxiliary viewer in the base tree mean that this archive should not be treated as untouched original retail media. SM2 is a related but distinct supplied program sharing an installation/data context. Similar compiler/overlay markers do not prove identical logic.

**Still unresolved:** actual installer mutations, transformed-data equivalence, precise main-program builds and release lineage, campaign-selection control flow, decompression/graphics-conversion formats, overlay relocation/loading semantics, save structures, and verified transfer predicates. The SM2 transfer utility's text points to late base/SM1 progress eligibility, but this has not been checked against its control flow or an original run. Filenames and text are evidence of intended interfaces, not proof of executed behavior. Public documentation continues to support historical installation/save-preservation guidance above; this run did not replay it.

**Architecture inference:** these products combine campaign data and program-version behavior, rather than being interchangeable mission files. Prefer one Android application with three campaign entries, explicit data/engine version selection, and a shared host. Preserve variant-specific loaders/routines when necessary. A common native library may contain multiple recovered program entry points before unifying verified shared logic. Maintain original save semantics inside the core, with host-managed backups and campaign-aware import/transfer. Do not assume concatenating campaign tables preserves progression. One app does not require forcing all variants into one executable implementation.

Privately compare installations in base → SM1 → SM2 order and record changes to executable/data/configuration files. Exercise both a fresh campaign and transferred pilot per variant. Public patch author's transfer-overflow report makes transition-state validation especially valuable. [WCAT](https://alltinker.itch.io/wcat)

## 9. Android architecture comparison

These are engineering judgments, assuming the recovered core presents frames/audio/events through a narrow interface. A, B, and C overlap: SDL itself uses a small Android Java/JNI layer.

| Criterion | A: NDK application / GameActivity | B: thin Kotlin/Java + native core | C: SDL host + native core | D: React Native/Expo + native core |
| --- | --- | --- | --- | --- |
| Fidelity/performance | Native loop; custom host behavior | Same core speed; keep JNI coarse | Same core; established platform services | Same native speed if gameplay stays native; additional framework |
| Graphics | Own EGL/surface/palette presentation | SurfaceView plus native renderer | Texture presentation and scaling | Custom native view; avoid JS frame transport |
| Audio | Oboe or native backend integration | Native callback/mixer under Android lifecycle | SDL audio as initial backend | Still needs a native audio backend |
| Touch/keyboard/controller | Native input buffer and mapping | Android UI/input integration; explicit event queue | Portable input/controller support; custom touch overlay | Good shell UI, but gameplay input still needs native handling |
| Files/saves/import | Android picker bridge plus native file layer | Straightforward picker/settings/export UI | Small Android bridge still required | Useful management UI, same native data adapter |
| Pause/resume | Explicit native-thread/surface handling | Clear activity ownership; thread coordination | SDL lifecycle plus app/core suspension policy | Coordinate activity, JS, native view, core, and audio |
| Debugging/testability | Native symbols, headless core tests | Native tests plus Android shell tests | Desktop harness reuse and host tests | More build/runtime boundaries and integration tests |
| Reproducibility | Pin NDK/AGP/Gradle/CMake/dependencies | Same native pins plus shell dependencies | Add pinned SDL release | Add Expo/RN/JS dependencies and generated native project policy |
| Desktop/WASM | Core portable; new host needed | Android shell stays separate | Most host concepts transfer | Core portable; JS shell does not replace a WASM host |
| Complexity | More bespoke platform services | Small native/mobile split | Moderate dependency, less bespoke host code | Highest shell complexity for present requirements |

Official Android documentation recommends GameActivity for new C/C++ intensive applications and describes its Java/native event and lifecycle bridge. NDK CMake support integrates through Gradle `externalNativeBuild`. This makes A/B direct Android builds practical; it does not eliminate the need for a small framework layer. [GameActivity](https://developer.android.com/games/agdk/game-activity), [NDK CMake](https://developer.android.com/ndk/guides/cmake)

SDL documents an Android Java/JNI shim, Gradle project, CMake integration, and a native shared-library entry point. Its current SDL3 Android documentation lists NDK r28c or later. Pin a tested release and toolchain rather than assuming the mutable documentation defines an already available build environment. The precise SDL2-versus-SDL3 choice is deferred to the host experiment; the independent core must not depend on that choice. [SDL Android documentation](https://wiki.libsdl.org/SDL3/README-android)

Expo can host custom native code, but Expo Go cannot load an arbitrary recovered core. A development/native build is required; Expo's documentation points primarily C++ modules toward React Native Turbo Modules. This option becomes attractive if a substantial cross-platform launcher/catalog product emerges. It is currently unnecessary for a framebuffer game and three campaigns. [Expo custom native code](https://docs.expo.dev/workflow/customizing/)

**Recommended host contract:** immutable imported game data, isolated writable saves, monotonic/injectable core time, indexed frames plus palette, timestamped input, native audio buffers, explicit suspend/resume, and bounded diagnostics. Prefer arm64 Android first, retaining desktop/headless tests; do not select minimum API or all ABIs without a supported-device decision. Test aliasing/alignment/endian assumptions and guest integer widths rather than equating successful x86 native compilation with ARM portability.

Use Android's Storage Access Framework for user-selected archives/folders, then validate and copy approved content into app-private storage or provide a suitable seekable adapter. A content URI is not automatically a native filesystem path. Keep original assets and private reconstructed code/builds outside public release artifacts under current governance; lawful possession does not authorize bundling them. A distributable public host and a privately produced reconstructed core need an explicit future packaging decision. [Android Storage Access Framework](https://developer.android.com/guide/topics/providers/document-provider)

On suspend, freeze game time, clear held input safely, stop/drain audio, and rebuild surface/audio state on resume without applying background wall-clock time to combat. Preserve original in-game saves; process-death restoration of an in-flight mission is a separate feature, not evidence of an existing original save capability. Test incoming interruption, backgrounding, rotation/surface replacement, controller unplug, save round trips, and 60/90/120 Hz displays. Start with SDL audio; consider Oboe only if device measurements show a reason. Android documents Oboe's low-latency native audio role. [Oboe](https://developer.android.com/games/sdk/oboe)

## 10. Current Unity1 toolchain observations

Read-only observations from the initial research run (not refreshed during completion), captured in [toolchain evidence](../qa/sprint-001/access-and-toolchain.json). Absence here is not a claim about tooling hidden outside the governed environment. No installation, Gradle build, device connection, or global configuration mutation was performed.

| Component | Observed capability |
| --- | --- |
| Java/JDK | OpenJDK and javac `17.0.20.1`; `JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64` |
| SDK | `ANDROID_HOME` and `ANDROID_SDK_ROOT` point to `/opt/csjs/android-sdk`; platform `android-36` |
| Build tools | `35.0.0`, `36.0.0` |
| SDK command tools | `15859902`, `latest`; `sdkmanager` present on PATH |
| ADB | `1.0.41`, platform-tools `37.0.1-15733141`; version query only |
| NDK | Neither side-by-side `ndk/` nor `ndk-bundle` present; no NDK environment override observed |
| CMake / Ninja | Not on PATH, no SDK CMake directory, packages not installed |
| Gradle | Not on PATH and no distro package; cached Gradle `8.14.1` script and launcher JAR present; not executed |
| Native host tools | GCC and Make present; Clang and pkg-config not on PATH |
| Node/npm | Node `v24.19.0`, npm `11.17.0` |
| Expo / React Native | No global `expo` or `react-native` command; npm global inventory includes `eas-cli@24.8.0`, `corepack@0.35.0`; no project dependency tree |
| SDL | No SDL headers observed under `/usr/include`; neither SDL2 nor SDL3 development package installed |

Java/SDK/Node/EAS availability is verified. A ready-to-use native Android toolchain is **not** verified: NDK/CMake/Ninja and host dependencies still need controlled provisioning. Cached Gradle presence is not proof that AGP dependencies resolve offline or that a native APK builds. The MOO2 snapshot offers Android-browser conventions and a native headless Makefile, not an Android Gradle/NDK application precedent.

## 11. Recommended Sprint 002 direction

Sprint 001's projection, workspace, bounded distribution inspection, and required validation/audit checks now pass. Start Sprint 002 from the privately fingerprinted WC and SM2 MZ/overlay programs and the observed SM1-aware base tree. Establish controlled installed baselines rather than treating the three archives as interchangeable clean installations; actual installer transformations and release lineage remain unresolved.

The most evidence-supported frontier is **program identity, overlay transitions, and clock coupling**. Privately establish executable/container/relocation identities across base/SM1/SM2. Investigate one representative path crossing code-loading boundaries into flight/scene timing, using a reversible trace setup and an original reference run. Record discoveries with confidence, provenance, and discriminating follow-up experiments. Choose semantic recovery, a targeted static translator, or a hybrid only after that evidence; do not copy MOO2's whole loader or impose a generic subsystem order.

Use a small, independently authored synthetic host exercise to compare SDL and GameActivity: indexed test pattern, generated audio, injected events/time, owned-data import plumbing without real assets, and pause/resume. A public synthetic app can verify Android infrastructure without moving reconstructed code into public Git. Provision pinned NDK/build dependencies through Unity1's approved mechanism in a later authorized scope; no global tooling was installed here.

Sprint 002 should produce a justified loader/recovery choice, private campaign/version matrix, measured timing hypotheses, one evidence-backed portable execution milestone, and host feasibility results. Acceptance should require a behavior comparison and clean boundaries, rather than a claim of complete gameplay. Original measurements/builds stay private; synthetic tools/tests and safe conclusions remain reviewable publicly.

## 12. Open questions and QA limits

- Owned layouts and raw member/executable fingerprints are established privately; precise release lineage, installed-data equivalence, and installer mutations remain unresolved.
- Original tick sources, PIT/IRQ use, update rates, busy-loop sites, retrace behavior, and frame-skip effects remain unmeasured.
- Distinct SM2 program/configuration/save references and transfer intent are established; semantic binary differences, verified transfer rules, campaign-state initialization, and patch lineage remain unresolved.
- WCAT is a useful comparator with optional balance/input/content changes; determine a baseline before comparing outcomes.
- The 1996 Windows reconstruction is a separate program lineage. Its licensing description does not override this project's prohibition on publishing mechanically recovered implementation.
- Minimum Android API, target device/controller set, audio backend, SDL version, and private-core packaging are not final decisions.
- No original game, emulator, Android app, MOO2 test, or reconstructed binary was executed here.
- The canonical boundary audit examines tracked Git files. New uncommitted/untracked report files need separate review; a tracked-files audit alone cannot approve this deliverable.

Project-native validator/audit PASS results and supplemental candidate-document review are recorded in [QA record](../qa/sprint-001/VALIDATION.md). Static distribution inspection satisfies this bounded completion scope; it does not validate gameplay or replace the next sprint's implementation investigation. Public changes remain uncommitted for the project-thread review required by governance.

## 13. Web bibliography

All entries accessed live **2026-10-06 UTC**. Original manuals are primary publications hosted by preservation/community services; OCR can omit text and is not owned-distribution verification. Maintainer statements are primary accounts of their projects, not independent acceptance tests.

| Source title / URL | Use and qualification |
| --- | --- |
| [W.C.A.T. — WC1 DOS Overhaul Mod (AllTinker, June 2025 discussion)](https://www.wcnews.com/chatzone/threads/w-c-a-t-wc1-dos-overhaul-mod-beta-v0-8-r4-released.32327/) | Primary patch-author timing, overlay, and investigation account |
| [Wing Commander A.T. (WCAT) Overhaul Mod](https://alltinker.itch.io/wcat) | Current primary author description, versions, input/audio/transfer fixes; no download |
| [Beta 0.8 R4 Released](https://alltinker.itch.io/wcat/devlog/967674/beta-08-r4-released) | Primary author notes: input-version support, expanded graphics requirement, SM2 progression fix; reinforces version uncertainty |
| [Wing Commander — The Secret Missions — Reference Card](https://www.scribd.com/document/759914554/Wing-Commander-The-Secret-Missions-Reference-Card) | Origin primary installation/launch/transfer instructions, hosted OCR |
| [Wing Commander — The Secret Missions 2 — Reference Card](https://pt.scribd.com/document/393839832/Wing-Commander-The-Secret-Missions-2-Reference-Card) | Origin primary installation and separate launch instructions, hosted OCR; transfer pages not available in extracted text |
| [Wing Commander DOS Reference Card (1992 CD edition)](https://www.mocagh.org/origin/u6wc-alt-wc-refcard.pdf) | Primary corroboration of SM1 menu and DOS controls; edition-specific |
| [Tech Support — Wing Commander CIC](https://www.wcnews.com/techsupport.shtml) | Community preservation guidance, installation/cycle recommendations; internally inconsistent SM2 continuation wording, resolved using original card |
| [Performance — DOSBoxWiki](https://www.dosbox.com/wiki/Performance) | Emulator's instruction-throughput and frame-skip explanation |
| [WCDX — DirectX DLL and other enhancements for Wing Commander Kilrathi Saga](https://github.com/Bekenn/wcdx) | Primary maintainer description of Windows compatibility/expansion scope |
| [Wing Commander source reconstruction and SDL2 port — wc1-re](https://github.com/neuromancer/wc1-re) | Primary README for recent 1996 Windows reconstruction; no source adopted |
| [GameActivity — Android Developers](https://developer.android.com/games/agdk/game-activity) | Official native application lifecycle/input integration |
| [CMake — Android NDK](https://developer.android.com/ndk/guides/cmake) | Official Gradle/NDK toolchain integration |
| [Android — SDL3 README](https://wiki.libsdl.org/SDL3/README-android) | Official SDL Android host and build requirements |
| [Add custom native code — Expo](https://docs.expo.dev/workflow/customizing/) | Official custom-native/development-build constraints |
| [Frame Pacing library — Android Developers](https://developer.android.com/games/sdk/frame-pacing) | Official display scheduling and variable-refresh considerations |
| [Open files using the Storage Access Framework](https://developer.android.com/guide/topics/providers/document-provider) | Official user-selected content access |
| [Oboe audio library — Android Developers](https://developer.android.com/games/sdk/oboe) | Official native low-latency audio option |

Several guessed preservation/PDF/wiki URLs failed to load, and the DOS Days SM1 PDF could not be visually rendered by the web tool. Those failed requests are not evidence for technical claims. The accessible original-card OCR and DOS reference PDF were used instead. No proprietary binary/assets/manual files were saved into this repository.
