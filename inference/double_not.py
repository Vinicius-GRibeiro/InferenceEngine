from core.step import Step
from ast_types.ast_not import Not
from ast_types.ast_var import Var

def apply_double_not(steps: list[Step]):
    new_steps = []

    for i, step in enumerate(steps):
        if isinstance(step.hipotesis, Not):
            expr = step.hipotesis
            counter = 0

            while isinstance(expr, Not):
                expr = expr.expr
                counter += 1

            if counter % 2 == 0:
                result = expr
            else:
                result = Not(expr)

            if any(s.hipotesis == result for s in steps + new_steps):
                continue

            new_steps.append(
                Step(result, "Double Negation [DN]", [i])
            )

    return new_steps

if __name__=="__main__":
    p = Var('P')
    np = Not(p)
    nnp = Not(np)

    steps = apply_double_not([Step(nnp)])
    for s in steps:
        print(s)