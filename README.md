# Boolean Logic Inference Engine

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)
![Status](https://img.shields.io/badge/status-under%20development-yellow)

A Python library that models **propositional logic** using **Abstract Syntax Trees (AST)** and automatically derives logical conclusions through formal inference rules.

This project was created after taking a Logic course during my Data Science degree. Its primary goal is to deepen my understanding of **Python**, **object-oriented programming**, **algorithms**, and **formal logic** by implementing a modular inference engine from scratch.

---

# Features

- Build logical expressions using an Abstract Syntax Tree (AST)
- Evaluate logical expressions under custom truth assignments
- Generate complete truth tables
- Classify expressions as:
  - Tautology
  - Contradiction
  - Contingency
- Automatically derive conclusions using inference rules
- Modular architecture that allows new inference rules to be easily added

---

# Supported Inference Rules

Currently implemented:

- ✅ Modus Ponens
- ✅ Modus Tollens
- ✅ Double Negation

Planned:

- De Morgan's Laws
- Commutativity
- Associativity
- Distribution
- Conditional Equivalence
- Contraposition
- Hypothetical Syllogism
- Disjunctive Syllogism

---

# Tech Stack

- Python
- Object-Oriented Programming (OOP)
- Abstract Syntax Trees (AST)
- Algorithms
- Data Structures
- Recursion
- Git

---

# Project Structure

```
boolean_logic/
│
├── ast_types/
│   ├── ast_var.py
│   ├── ast_and.py
│   ├── ast_or.py
│   ├── ast_not.py
│   └── ast_implication.py
│
├── engine/
│   ├── engine.py
│   ├── rules.py
│   └── step.py
│
├── truth_table.py
│
└── examples/
```

The project follows a modular architecture where logical expressions are represented by an AST, evaluated independently, and processed by the inference engine.

---

# Example

Starting with the premises:

- P
- P → Q

the engine automatically infers **Q** using **Modus Ponens**.

```python
from boolean_logic.ast_types.ast_var import Var
from boolean_logic.ast_types.ast_implication import Implication

from step import Step
from engine import run

p = Var("P")
q = Var("Q")

steps = [
    Step(p),
    Step(Implication(p, q))
]

run(steps)
```

Output

```
1. P (Hypothesis)

2. (P → Q) (Hypothesis)

3. Q (Modus Ponens [MP]: 1,2)
```

---

# Building Expressions

Every logical expression is represented as an AST.

Simple proposition

```python
p = Var("P")
```

Negation

```python
Not(p)
```

Conjunction

```python
And(p, q)
```

Disjunction

```python
Or(p, q)
```

Implication

```python
Implication(p, q)
```

More complex expressions can be built by nesting nodes.

```python
expr = And(
    Implication(Not(p), q),
    r
)

print(expr)
```

Output

```
((¬P → Q) ∧ R)
```

---

# Evaluating Expressions

Logical values are assigned through a context dictionary.

```python
expr = And(p, q)

context = {
    "P": True,
    "Q": False
}

print(expr.eval(context))
```

Output

```
False
```

---

# Truth Tables

The engine can generate the complete truth table for any expression.

```python
expr = Implication(
    And(p, q),
    Or(r, Not(q))
)

table = TruthTable(expr)
table.print_truth_table()
```

Example

| P | Q | R | Result |
|---|---|---|--------|
|1|1|1|1|
|1|1|0|0|
|...|...|...|...|

Expression Type

```
CONTINGENCY
```

---

# Automatic Inference

The inference engine continuously applies all available inference rules until no further conclusions can be derived.

Each generated statement stores:

- the inference rule used
- the premises involved
- the resulting expression

This allows complete proof construction.

Example:

```
1. P

2. P → Q

3. Q      (MP: 1,2)

4. Q → R

5. R      (MP: 3,4)
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/Vinicius-GRibeiro/InferenceEngine.git
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Roadmap

- Natural Deduction Proofs
- Predicate Logic
- Parser for textual logical expressions
- SAT Solver
- CNF Conversion
- Proof visualization
- Performance optimizations
- Unit tests
- Documentation website

---

# Why this project?

Instead of relying on existing symbolic logic libraries, the objective was to implement the entire inference engine from scratch in order to better understand:

- logical expression representation
- recursive evaluation
- inference algorithms
- software architecture
- extensible rule systems

The project also serves as a foundation for future implementations involving predicate logic, SAT solving and automated theorem proving.
