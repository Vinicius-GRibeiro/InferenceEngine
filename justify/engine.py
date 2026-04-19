from modus_tollens import apply_modus_tollens, Implication, Not, Var, Step, And, Or
from modus_ponens import apply_modus_ponens
from double_not import apply_double_not

def run(premisses_steps: list[Step]):
    known_exprs = set(step.hipotesis for step in premisses_steps)
    all_steps = premisses_steps.copy()

    while True:
        _new_steps = []

        candidates = []
        candidates += apply_modus_ponens(premisses_steps)
        candidates += apply_modus_tollens(premisses_steps)
        candidates += apply_double_not(premisses_steps)

        for step in candidates:
            expr = step.hipotesis
            if expr not in known_exprs:
                known_exprs.add(expr)
                _new_steps.append(step)
        if not _new_steps:
            break

        premisses_steps.extend(_new_steps)
        all_steps.extend(_new_steps)

    for i, step in enumerate(all_steps):
        print(f"{i + 1}. {step}")

if __name__ == "__main__":
    run([
        Step(Var('P')),
        Step(Implication(Var('P'), Var('Q')))
    ])