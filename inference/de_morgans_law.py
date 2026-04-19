from core.step import Step
from ast_types.ast_not import Not
from ast_types.ast_var import Var
from ast_types.ast_and import And
from ast_types.ast_or import Or

def apply_de_morgan(steps: list[Step]):
    new_steps = []

    for i, step1 in enumerate(steps):
        if isinstance(step1.hipotesis, Not):
            expr = step1.hipotesis
            inner_expr = expr.expr
            result = None

            if isinstance(inner_expr, And):
                result = Or(Not(inner_expr.left), Not(inner_expr.right))
            elif isinstance(inner_expr, Or):
                result = And(Not(inner_expr.left), Not(inner_expr.right))

            if result is None:
                continue

            if any(s.hipotesis == result for s in steps + new_steps):
                continue

            new_steps.append(Step(result, "De Morgan [DM]", [i]))

    return new_steps

