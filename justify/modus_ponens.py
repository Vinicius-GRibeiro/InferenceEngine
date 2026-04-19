from step import Step
from boolean_logic.ast_types.ast_implication import Implication
from boolean_logic.ast_types.ast_var import Var
from boolean_logic.ast_types.ast_and import And

def apply_modus_ponens(steps: list[Step]):
    new_steps = []

    for i, step1 in enumerate(steps):
        if isinstance(step1.hipotesis, Implication):
            left = step1.hipotesis.left
            right = step1.hipotesis.right

            for j, step2 in enumerate(steps):
                if step2.hipotesis == left:
                    if any(s.hipotesis == right for s in steps + new_steps):
                        continue

                    new_steps.append(
                        Step(hipotesis=right, rule_name="Modus Ponens [MP]",
                             dependencies_index=sorted([i, j])
                             )
                    )

    return new_steps



if __name__ == "__main__":
    steps = []
    p = Var('P')
    q = Var('Q')

    steps.append(Step(Implication(p, q)))
    steps.append(Step(p))

    new_steps = apply_modus_ponens(steps)
    steps.extend(new_steps)

    for i, step in enumerate(steps):
        print(f"{i+1}. {step}")
