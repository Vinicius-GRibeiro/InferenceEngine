from core.step import Step
from ast_types.ast_implication import Implication
from ast_types.ast_not import Not
from ast_types.ast_var import Var
# from ast_types.ast_and import And
# from ast_types.ast_or import Or


def apply_modus_tollens(steps: list[Step]):
    new_steps = []

    for i, step1 in enumerate(steps):
        if isinstance(step1.hipotesis, Implication):
            left = step1.hipotesis.left
            right = step1.hipotesis.right

            for j, step2 in enumerate(steps):
                if isinstance(step2.hipotesis, Not) and step2.hipotesis.expr == right:
                    conclusion = Not(left)

                    if any(s.hipotesis == conclusion for s in steps + new_steps):
                        continue

                    new_steps.append(
                        Step(hipotesis=conclusion, rule_name='Modus Tollens [MT]',
                            dependencies_index=sorted([i, j])
                        )
                    )

    return new_steps

if __name__=="__main__":
    p = Var('P')
    q = Var('Q')
    nq = Not(q)
    implication = Implication(p, q)
    steps = [Step(implication), Step(nq)]

    mt = apply_modus_tollens(steps)

    for step in mt:
        print(step)
