class Not:
    def __init__(self, expr):
        self.__expr = expr

    @property
    def expr(self):
        return self.__expr

    def aval(self, context):
        return not self.expr.aval(context)

    def __extract_var_duplicated(self):
        return self.expr.extract_var()

    def extract_var(expr):
        return list({v.name: v for v in expr.__extract_var_duplicated()}.values())

    def __repr__(self):
        return f"¬{self.expr}"

    def __eq__(self, other):
        return isinstance(other, Not) and self.expr == other.expr

    def __hash__(self):
        return hash(("Not", self.expr))