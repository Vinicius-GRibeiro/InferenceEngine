class Implication:
    def __init__(self, left, right):
        self.__left = left
        self.__right = right

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    def aval(self, context):
        return (not self.left.aval(context)) or self.right.aval(context)

    def __extract_var_duplicated(self):
        return self.left.extract_var() + self.right.extract_var()

    def extract_var(self):
        return list({v.name: v for v in self.__extract_var_duplicated()}.values())

    def __repr__(self):
        return f"({self.left} → {self.right})"

    def __eq__(self, other):
        return (
                isinstance(other, Implication)
                and self.left == other.left
                and self.right == other.right
        )

    def __hash__(self):
        return hash(("Implication", self.left, self.right))