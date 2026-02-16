# overlap-rigidity-counterexamples

Canonical repository of **explicit counterexamples and obstruction instances** for overlap‑rigidity and locality‑based rigidity hypotheses.

This repository exists to make **failure modes first‑class objects**. Every graph, profile, or construction here is an explicit witness showing why certain naive or over‑strong rigidity statements cannot hold without additional hypotheses.

No claims are made. No conjectures are proposed. Only concrete counterexamples are recorded.

---

## Role in the program

This repository plays a defensive and clarifying role in the rigidity stack:

```
mathlib / raw constructions
        ↓
overlap-rigidity-counterexamples   (this repo)
        ↓
formal frameworks / conditional indices / manuscripts
```

Any rigidity statement or conditional assumption must be **compatible with every instance recorded here**. If it is not, the statement is false or incomplete.

---

## Scope

* Collects **explicit graphs and structures** exhibiting overlap‑rigidity failure modes
* Records **minimal obstruction instances** where possible
* Serves as a **reference set** for proof exclusions and hypothesis sharpening

This repository intentionally avoids abstraction. Every item is concrete.

---

## What this repository is

* A catalog of **known counterexamples**
* A regression suite against over‑strong claims
* A shared reference for reviewers, collaborators, and formalization work

## What this repository is not

* A proof repository
* A conjecture generator
* A place for heuristic or probabilistic arguments

---

## Repository structure

```
.
├── graphs/
│   ├── *.edgelist          # explicit graph counterexamples
│   ├── *.json              # structured profiles / annotations
│   └── README.md           # per‑graph notes (optional)
├── scripts/
│   ├── validate_graph.py   # minimal loaders and sanity checks
│   └── inspect_example.py  # lightweight inspection helpers
├── certs/                  # generated witness artifacts (if any)
├── tests/                  # loader and format sanity checks
├── STATUS.md               # classification of known failure modes
└── README.md
```

File names and counts may evolve, but **the meaning of each entry must remain explicit**.

---

## Counterexample classes

Typical categories include (non‑exhaustive):

* **Local homogeneity without global rigidity**
* **Cycle overlap insufficiency**
* **FOᵏ locality blind spots**
* **WLᵏ indistinguishability failures**
* **Support saturation without symmetry breaking**

Each counterexample should be classifiable under at least one failure mode.

---

## Usage

### Validate an example

```bash
python3 scripts/validate_graph.py graphs/example.edgelist
```

This checks format validity and basic invariants only.

### Inspect structure (optional)

```bash
python3 scripts/inspect_example.py graphs/example.edgelist
```

Inspection tools are intentionally lightweight and non‑analytic.

---

## Determinism and reproducibility

* All stored artifacts are **fully explicit**
* Any generated witnesses must record:

  * construction parameters
  * random seeds (if applicable)
  * tool version

Reproduction must not rely on undocumented choices.

---

## Update policy

This repository follows strict rules:

* **Add** a counterexample when a rigidity claim fails on a concrete instance
* **Document** the failure mode in `STATUS.md`
* **Never remove** a counterexample unless it is shown to be invalid or malformed

Counterexamples, once validated, are permanent.

---

## Relationship to other repositories

* Referenced by `final-wall-conditional-index` to justify conditionals
* Used by formal layers to define excluded regimes
* Used by manuscripts to prevent overstatement

No downstream work may ignore an entry here.

---

## Status

* Purpose: **counterexample catalog**
* Claims: **none**
* Proofs: **none**
* Authority: **canonical for obstruction instances**

See `STATUS.md` for the current list of failure modes and example counts.

---

## License

MIT or CC0 (choose one and record explicitly).

---

## Integrity note

Rigidity programs fail most often by forgetting counterexamples. This repository exists to ensure that **every false path remains visibly false**.

If a structure breaks a claim, it belongs here.
