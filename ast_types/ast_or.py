class Or:
    def __init__(self, left, right):
        self.__left = left
        self.__right = right

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    def aval(self, context: dict) -> bool:
        return self.left.aval(context) or self.right.aval(context)

    def __extract_var_duplicated(self):
        return self.left.extract_var() + self.right.extract_var()

    def extract_var(expr):
        return list({v.name: v for v in expr.__extract_var_duplicated()}.values())

    def __repr__(self):
        return f"({self.left} ∨ {self.right})"

    def __eq__(self, other):
        return (
                isinstance(other, Or)
                and self.left == other.left
                and self.right == other.right
        )

    def __hash__(self):
        return hash(("Or", self.left, self.right))