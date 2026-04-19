from itertools import product

class TruthTable:
    def __init__(self, exp):
        self.__exp = exp

    @property
    def exp(self):
        return self.__exp

    def __create_context(self, variables):
        names = [v.name for v in variables]

        combinations = product([True, False], repeat=len(names))

        contexts = [
            dict(zip(names, valores))
            for valores in combinations
        ]

        return contexts

    def print_truth_table(self):
        variables = self.__get_variables()

        contexts = self.__create_context(variables)

        for var in variables:
            print(f"  {var}  |", end='')
        print(f'  {self.exp}')

        all_values = []

        for context_dict in contexts:
            values = list(context_dict.values())
            for value in values:
                print(f"  {'1' if value else '0'}  |", end='')
            print(f'  {'1' if self.exp.aval(context_dict) else '0'}')
            all_values.append(self.exp.aval(context_dict))

        print('Expression Type: ', end='')
        if all(all_values):
            print("TAUTOLOGY")
        elif not any(all_values):
            print("CONTRADICTION")
        else:
            print('CONTINGENCY')


    def __get_variables(self):
        return sorted(self.exp.extract_var(), key=lambda k: k.name)
