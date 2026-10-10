# Quality gates / Критерии завершения ролей

A role is not complete merely because it produced a handoff. It is complete only when its minimum diagnostic/editorial gate is satisfied or when unresolved failures are explicitly marked as blocking/routed onward.

## General gate rule

Every specialist should end with one of:

- `PASS` — role-specific minimum quality gate met;
- `PASS_WITH_KNOWN_RISKS` — usable downstream, with explicit non-blocking risks;
- `BLOCKED` — unresolved problem makes downstream work unsafe;
- `AUTHOR_DECISION_REQUIRED` — several materially different valid paths remain.

The result belongs in the handoff and, when it changes workflow state, in `story-status.md` / queue.

Every role in the manifest has a gate. Roles below have compact gates; roles `015`, `020`, `050`, `100`, `135`, `140`, `150` have detailed gates further down.

## Compact gates

| role | minimum gate | block when |
| --- | --- | --- |
| `003` | every feedback item is sorted; earliest affected role named; queue and `story-status.md` updated with `Next launch` | route requires a role/decision that does not exist or author preferences conflict |
| `005` | target length/form known or explicitly assumed; essential questions marked; author intent not invented | core intent is unknowable without the author |
| `010` | premise has character + want + obstacle + cost; story engine and reader promise named; format fit checked | no dramatic engine survives, only a situation |
| `030` | every scene in the table has a value change and causal link; turning point is the protagonist's choice; ending setups listed; length budget fits target | structure depends on coincidence or cannot fit the target length |
| `040` | every irreversible choice is psychologically motivated; key characters have conflicting wants | a required choice is psychologically implausible and no repair is offered |
| `060` | motifs mapped to scenes; ambiguity vs clarity stated; `pre-draft-brief.md` compiled only from approved decisions | brief would need decisions the author has not made |
| `070` | voice contract approved (or calibration options offered and stopped); draft covers the scene table; length reported vs target; quick anti-LLM pass done | no approved brief/voice contract |
| `080` | planned vs actual scene table reconciled; setups/payoffs checked; length inside target or deviation justified | structural fix requires premise/ending change → route via `003` |
| `090` | each voice-contract field satisfied or justified; full anti-LLM pass reported with before/after counts | voice contract conflicts with canon or author profile |
| `110` | ending promise vs payoff stated; ambiguity judged productive or evasive; final image tested | ending contradicts canonical ending direction |
| `120` | implied worldview named; opposing positions checked for real force | the story accidentally argues the opposite of its intended meaning |
| `130` | expected beats listed; inevitability separated from boredom; disruptions preserve premise | the ending is guessable from the first scene and the author has not accepted that |

## 015 — Criterion Stress Tester

Minimum gate before premise-dependent downstream work:

- all active candidate rules received the same core attack corpus;
- obvious `why not simply X?` exploits were tested;
- repairs were regression-tested against affected earlier attacks;
- long-horizon effects were tested when consequences persist;
- undefined metrics/terms are listed rather than hand-waved;
- at least one surviving rule is narratively expressible without pathological legalistic complexity, or the role blocks;
- materially different survivors are returned to the author instead of silently choosing canon.

Block when the premise rule remains trivially exploitable, impossibly strict, or undefined in a way that collapses the intended story.

## 020 — Brutal Critic

The critic is an adversarial gate, not a balanced review.

Minimum gate:

- assume the concept may fail and actively search for rejection reasons;
- produce independent failure modes across premise, stakes, causality, reader access, cliché/predictability, emotional investment, overload, and false depth where relevant;
- classify findings at least as `fatal`, `major`, `repairable`, `minor`;
- attempt the strongest plausible hostile-reader interpretation;
- include `why would I stop reading?`, `why is this merely X?`, and `why doesn't the protagonist/world simply do Y?` attacks when applicable;
- distinguish genuine strengths only insofar as they identify what must survive repairs;
- do not dilute severe findings with generic praise.

A first pass that finds almost no meaningful weaknesses should explicitly perform a second hostile pass before declaring `PASS`.

## 050 — Worldlogic Auditor

Minimum gate:

- core mechanics have actors, incentives, information flow, enforcement/failure modes, and adoption reasons;
- institutions do not work by unexplained universal compliance;
- technology/magic does not acquire capabilities merely because the plot needs them;
- obvious substitutes/workarounds are considered;
- timing, scale, cost, safety, abuse, and fallback are tested when relevant;
- the world remains understandable without requiring specialist technical knowledge.

Block when a central causal chain depends on institutional or technical behavior that the story cannot plausibly support.

## 100 — Reader Simulator

Minimum gate:

- simulate at least an ordinary reader and, when relevant, a technically literate reader;
- identify exact confusion/dropout points rather than giving general impressions;
- distinguish intended ambiguity from accidental incomprehensibility;
- report emotional engagement trajectory, not only plot comprehension;
- name at least the strongest reason a target reader might stop, disengage, or misunderstand;
- recommendations are prioritized by impact.

Do not pass a candidate merely because the themes are intelligible to the workshop agents.

## 135 — Similarity & IP Auditor

Minimum gate when invoked:

- compare only the most relevant works, not a random large list;
- distinguish trope/idea overlap from distinctive selection-and-arrangement and expressive overlap;
- separate reader-perception risk from legal-risk signal;
- verify named/current comparison works with public research where needed;
- identify convergence clusters, not just isolated matching details;
- state research limits and avoid claiming legal clearance;
- high-risk clusters receive targeted distancing options across at least two independent dimensions when feasible.

Block finalization when a high-risk similarity cluster plausibly survives at mechanism + causal-sequence/payoff or other distinctive-expression level and requires structural change.

## 140 — Continuity Auditor

Minimum gate:

- compare draft against canonical state and decisions log;
- check timeline/causality, identities/names, terminology, world rules, factual state, and emotional memory;
- distinguish draft error from stale canonical documentation;
- all severe contradictions are either fixed/routed or explicitly blocking;
- unresolved continuity findings cite stable paragraph IDs when available.

Do not pass a final candidate with a known contradiction that changes reader interpretation of causality, character motivation, or world rules.

## 150 — Final Editor and manuscript completion

`150` cannot itself declare publication readiness.

It may produce a `manuscript_complete` candidate only when:

- blocking upstream quality-gate failures have been resolved or explicitly accepted by the author;
- `140` has no unresolved severe continuity contradiction;
- high-risk `135` findings, when `135` was required, have been resolved/accepted;
- the author reaches the final checkpoint after the `150` export.

See `docs/post-manuscript-frameworks.md` for the boundary after this point.
