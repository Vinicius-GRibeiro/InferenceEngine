class Var:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def aval(self, context):
        return context[self.name]

    def __extract_var_duplicated(self):
        return [self]

    def extract_var(expr):
        return list({v.name: v for v in expr.__extract_var_duplicated()}.values())

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Var) and self.name == other.name

    def __hash__(self):
        return hash(("Var", self.name))

    def __lt__(self, other):
        return self.name < other.name
