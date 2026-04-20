from ast_types.ast_var import Var
from core.step import Step
from ast_types.ast_implication import Implication

def apply_hypothetical_syllogism(steps: list[Step]):
    new_steps = []

    for i, step1 in enumerate(steps):
        if isinstance(step1.hipotesis, Implication):
            p = step1.hipotesis.left
            q1 = step1.hipotesis.right

            for j, step2 in enumerate(steps):
                if isinstance(step2.hipotesis, Implication) and step2!= step1:
                    q2 = step2.hipotesis.left
                    r = step2.hipotesis.right

                    if q2 == q1:
                        conclusion = Implication(p, r)

                        if any(s.hipotesis == conclusion for s in steps + new_steps):
                            continue

                        new_steps.append(
                            Step(conclusion, "Hypothetical Syllogism [HS]", sorted([i, j]))
                        )

    return new_steps
