class Step:
    def __init__(self, hipotesis, rule_name="Hipotesis", dependencies_index=None):

        self.__hipotesis = hipotesis
        self.__rule_name = rule_name
        self.__dependencies_index = dependencies_index or []

    @property
    def hipotesis(self):
        return self.__hipotesis

    @property
    def rule_name(self):
        return self.__rule_name

    @property
    def dependencies_index(self):
        return self.__dependencies_index

    def __str__(self):
        if not self.dependencies_index:
            return f"{self.hipotesis} ({self.rule_name})"

        deps = ", ".join(str(i + 1) for i in self.dependencies_index)
        return f"{self.hipotesis} ({self.rule_name}: {deps})"

    def __eq__(self, other):
        return (
                isinstance(other, Step) and
                self.hipotesis == other.hipotesis
        )

