# Result DAG Contract

Read this reference in full immediately before materializing, auditing,
admitting, changing, withdrawing, or migrating a result node. Apply it before
relying on an existing node whose current pair has not been checked against
this contract. Read [Verification, Status, And
Invalidation](#verification-status-and-invalidation) before defining a proof
task's acceptance criteria.

## Contents

- [Node Boundary And Admission](#node-boundary-and-admission)
- [Canonical Records And Views](#canonical-records-and-views)
- [Formal Result Documents](#formal-result-documents)
- [Support Routes And Graph Semantics](#support-routes-and-graph-semantics)
- [Verification, Status, And Invalidation](#verification-status-and-invalidation)
- [Materialization And Node Audit](#materialization-and-node-audit)
- [Maintenance And Bounded Reading](#maintenance-and-bounded-reading)

## Node Boundary And Admission

Materialize a provisional N-node only after the principal chooses one exact,
important result boundary that belongs in the global dependency structure. One
node owns one primary theorem-like or empirical statement. Split independently
reusable statements into separate nodes. Use one composite node only when its
clauses are logically inseparable and every support route proves the complete
composite statement.

Keep earlier candidate statements, proof attempts, experiments, citations, and
ChatGPT Pro material in task or consultation artifacts. Treat `candidate` as an
admission state, not a correctness verdict: a provisional node or other
unverified candidate may motivate later tasks but cannot be relied on. An
independently verified task result may be used as a checked input without
becoming a node. Such use creates no DAG edge; include the result and its
justification inside any later formal proof that uses it, or promote it to an
N-node when it should become a standalone dependency.

Reserve an N-ID when the principal materializes its provisional node pair for
audit. Never recycle it, even if admission later fails.

## Canonical Records And Views

Use `dag/nodes/Nxxx/Nxxx.yaml` as the canonical structured statement. Make it
understandable without opening a proof. Include:

- identity, graph role, admission status, and `kind` (`theoretical` or
  `empirical`);
- self-contained setup;
- complete assumptions or evaluation conditions;
- exact conclusion and concrete summary;
- exact origin artifacts; and
- one or more support routes.

Do not duplicate the TeX theorem-environment choice in YAML. The formal
environment in `Nxxx.tex` is authoritative for whether a theoretical result is
presented as a theorem, lemma, proposition, or corollary.

Create `dag/dag.yaml` when admitting the first node, using
[`assets/workspace/dag.yaml`](../assets/workspace/dag.yaml). Maintain it as the complete compact overview of
every admitted node and support route. Each node entry includes its title,
concrete summary, graph role, kind, status, record path, and document path. Each
route includes its support key, kind, prerequisites, idea, and status. Match
every compact route to its canonical `Nxxx.yaml` route by exact support key,
and make all overlapping values agree.

Make every node summary state its main conditions and result rather than merely
repeat its title or ID. Use `targets` for admitted nodes that directly answer or
resolve the investigation question; leave it empty until such a node exists.

Keep full setup, assumptions, conclusion, origin, and support metadata in
`Nxxx.yaml`. Keep the corresponding formal setup, assumptions, statement,
interpretation, and complete proof or evidence bodies in `Nxxx.tex`.
`Nxxx.yaml` remains authoritative for the full node record; every overlapping
value in `dag.yaml` must match it.

Only the principal updates durable node files, `dag.yaml`, and the compact DAG
table in `index.md`. Node auditors write only within the named support route's
audit directory; they may inspect but not edit the sources they check.

## Formal Result Documents

Put all definitions needed to understand the result in setup. Use formal,
labeled assumption environments in the TeX document for every assumption or
evaluation condition. Put every quantifier, applicability condition, parameter
dependence, and limitation in setup, assumptions, or conclusion. For an
algorithmic result, define the complete algorithm in setup and state its proved
or observed guarantee in conclusion.

Do not render `kind`, graph role, support keys, dependency lists, task paths,
audit paths, or provenance as standalone metadata paragraphs or headings in
the TeX document. Cite genuine mathematical or empirical sources normally
where they are used.

### Theoretical Nodes

Use [`assets/workspace/node.tex`](../assets/workspace/node.tex). Choose the mathematically appropriate primary
theorem-like environment, make it explicitly invoke the relevant assumptions,
and make setup, assumptions, and conclusion match YAML exactly.

Place the formal statement before any interpretation. Immediately after it,
write an accurate `Interpretation` paragraph explaining what the result means,
why it is useful, and what it does not establish. Follow it with an accurate
`Proof idea` paragraph mapping the proof's actual logical structure, then give
the complete formal proof.

With one proof, put a standard `proof` environment directly after these
paragraphs. With several alternative proofs, give each proof a descriptive
section and its own proof-idea paragraph; record the matching section title in
the route's `tex_section`. Keep route identity and AND/OR dependency semantics
in YAML rather than rendering them as mathematical exposition.

### Empirical Nodes

Use [`assets/workspace/node-empirical.tex`](../assets/workspace/node-empirical.tex). Give formal evaluation conditions,
one exact `empiricalresult`, an accurate interpretation and evidence idea, and
complete retained evidence or reproduction sections. Do not present a fixed
observed result as a universal theorem.

## Support Routes And Graph Semantics

Give every support route a unique, stable, human-readable key within its node.
Write it in lowercase kebab-case and name it for its mechanism or evidence,
such as `direct-proof`, `coupling-proof`, or `fixed-seed-reproduction`. Keep the
key through repair and continued audit. Create a new key instead of repurposing
one when the route's mechanism changes materially.

For every route, record:

- its support key and kind;
- prerequisite N-nodes;
- proof idea or evidence summary;
- final TeX source;
- human-readable proof or evidence section;
- retained empirical artifacts when applicable;
- status; and
- independent check.

Treat the pair of N-ID and support key as the route's audit identity. Enforce
these semantics:

- prerequisites within one route are AND;
- distinct verified routes supporting the same statement are OR;
- a route is usable only while every node in `requires` is currently verified;
- edges point from prerequisite node to dependent node;
- when admitting or changing a node or route, ensure its edges do not introduce
  a cycle;
- theoretical nodes use proof or checked-citation support and depend only on
  theoretical nodes; and
- empirical nodes use fixed-setup evidence with retained output and
  reproduction or independent verification.

In the audit rules below, the substantive node payload means every YAML field
except the node's `status` and each route's `status` and `checked_by`. Compare
it by parsing both YAML files, omitting those fields, and requiring the
remaining data structures to be equal.

## Verification, Status, And Invalidation

Treat correctness, completeness, self-containment, and readability as joint
hard requirements. For proof support, require a rigorous argument relative to
the node's formal setup and assumptions. State every necessary intermediate
claim, justify every inference, show the calculations needed to verify
constants and parameter dependence, and cover all relevant boundary,
degenerate, and equality cases. Never omit a step as obvious, standard,
routine, or left to the reader; split a long argument into named lemmas with
complete proofs instead.

Write notation and transitions clearly enough that a domain reader can verify
the result line by line without guessing definitions, reconstructing missing
reasoning, or opening the originating task artifact. The interpretation and
proof idea must be faithful and readable but cannot carry any logical step
missing from the proof.

For citation support, identify the exact cited result and check every required
assumption and quantifier. For empirical support, require reproduction or
independent verification of the fixed-setup evidence.

Assign a fresh independent auditor to adversarially check a theoretical support
route when it first enters audit, and use reproduction or independent
verification for empirical support. Keep the same auditor through repairs to
that route. Audit alternative routes serially.

Use these route states:

- `needs_recheck`: the current route has not cleared an audit of the current
  node pair;
- `verified`: the route has cleared the required audit and all prerequisites
  remain verified;
- `invalid`: the support route is fatally flawed.

Use these node states:

- `candidate`: admission or repair remains pending;
- `verified`: at least one usable verified route remains;
- `withdrawn`: an admitted node has lost all usable verified routes, or a
  candidate has been abandoned.

If a mathematical statement, support body, dependency, or evidence source
changes, mark the affected route `needs_recheck`, clear `checked_by`, and have
the same auditor check the exact current node pair again. Because every route
names the same `Nxxx.tex` source, any substantive change to that file
invalidates every route check on the old file.

Whenever a prerequisite loses verification, recursively mark every dependent
route that requires it `needs_recheck`, clear its old check, and withdraw every
dependent node left without a usable verified route. Re-audit repaired
descendants in topological order.

## Materialization And Node Audit

Before the first node audit:

1. Copy [`assets/workspace/node.yaml`](../assets/workspace/node.yaml) and the kind-appropriate TeX template into
   `dag/nodes/Nxxx/` as `Nxxx.yaml` and `Nxxx.tex`. Use `node.tex` for a
   theoretical node and `node-empirical.tex` for an empirical node.
2. Start the node at `status: candidate`, every route at
   `status: needs_recheck`, and every `checked_by` list empty.
3. Fully replace all placeholders and compile the standalone TeX.
4. Maintain the pair together. Put the one exact statement and every complete
   proof, citation check, or evidence route in `Nxxx.tex`.
5. Preserve every originating task artifact through `origin_sources`.
6. Point every route's `source` to `Nxxx.tex`; use `tex_section` for its
   human-readable proof or evidence section, and list retained empirical
   artifacts in `evidence_artifacts`.
7. Repair any YAML/TeX mismatch before dispatching the audit.

Never use an audit of an originating task artifact as a substitute for auditing
the current node pair.

Store each route audit under
`dag/nodes/Nxxx/audits/<support-key>/` as `audit.md`,
`audited-node.yaml`, and `audited-node.tex`. Use
[node-audit-prompt.md](node-audit-prompt.md) when a route first enters node
audit and for its repair loop.

A route clears audit only when `audit.md` identifies the exact N-ID and support
key, reports no unresolved material finding, and its retained copies still bind
the current pair: the current TeX is byte-for-byte identical to
`audited-node.tex`, and the current substantive YAML payload equals the parsed
payload of `audited-node.yaml`. Record that audit path in the route's
`checked_by` list.

Do not add the provisional node to `dag.yaml` or the Verified DAG table until
the audit has no unresolved material finding and its retained copies bind the
exact current pair. List its reserved N-ID and audit state under Pending Node
Audits in `index.md`. Apply the same node-audit contract to initial admission,
later route verification, and repair.

After an audit clears one route against the retained current pair, change only
that route's `status` and `checked_by` and, when it becomes usable, the node's
`status`. Then propagate the result to `dag.yaml` and the root views.

## Maintenance And Bounded Reading

Use `index.md` for the investigation-wide control view and `dag/dag.yaml` for a
DAG-specific bounded read. Open individual `Nxxx.yaml` and `Nxxx.tex` files
only when their full statement, metadata, proof, or evidence is needed. Future
visualization should consume `dag.yaml` rather than scan every node directory.

Treat a legacy node that lacks the required YAML fields, formal TeX
presentation, or an accepted node audit of its current YAML/TeX pair as needing
controlled migration. It cannot retain `verified` merely because an
originating task artifact was audited. Mark its affected routes
`needs_recheck`, expose the migration under Pending Node Audits, repair the
pair, and audit it before further reliance. Preserve completed historical task
and audit paths rather than renaming or migrating them solely because the
current layout changed.

When completing a round or handing off the investigation, check that:

- every admitted node and verified route satisfies this contract;
- `dag.yaml` agrees with the canonical node records;
- the Verified DAG table in `index.md` agrees with `dag.yaml`;
- Pending Node Audits agrees with provisional node pairs and route audit
  directories; and
- every referenced ID, path, source, dependency, and retained check resolves.
