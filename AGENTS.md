# Hippogriff Classics title agent guidance

Governing objective: owned original DOS binary/data -> reverse-engineer actual implementation ->
recover real logic/structures/globals/algorithms/behavior -> reconstruct portable native core ->
WASM/browser and/or modern native targets -> thin modern host layer.

Frontier agents own the reverse-engineering strategy. Do not impose a generic subsystem sequence.
The public repo may contain independently authored analyzers/recompilers, runtimes, compatibility
layers, tests, tooling, and safe knowledge. Keep original bytes, proprietary assets, mechanically
recovered code, executable-derived private images/builds, and similar title-derived material in
the governed private Classics workspace.

Governed `csjs-agent` runs receive approved public sibling repos as exact-SHA read-only snapshots.
When private references are authorized, the title's own private source is read-only, its dedicated
private workspace is writable, approved sibling private shares are read-only, and Git metadata is
protected. Leave public-repo edits uncommitted until the Classics public-boundary review passes.
