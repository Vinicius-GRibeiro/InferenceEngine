from core import engine
from core.step import Step
from ast_types.ast_or import Or
from ast_types.ast_var import Var
from ast_types.ast_not import Not
from ast_types.ast_and import And
from core.truth_table import TruthTable
from ast_types.ast_implication import Implication

# INICIE AQUI
a = Var('A')
b = Var('B')
c = Var('C')

imp1 = Implication(a, b)

engine.run([Step(Not(b)), Step(imp1)])

# TESTES
#
# A = Var('A')
# B = Var('B')
# C = Var('C')
#
# p = Var('P')
# q = Var('Q')
# r = Var('R')
# s = Var('S')
# t = Var('T')
# u = Var('U')
#
# expr = Or(Implication(Or(And(Implication((And(p, q)), (Or(r, Not(q)))), s), t), Not(t)), u)
#
# tt = TruthTable(expr)
# tt.print_truth_table()
#
# print("\n=== Teste 1: A ∧ B ===")
# exp1 = And(A, B)
# tt1 = TruthTable(exp1)
# tt1.print_truth_table()
#
# print("\n=== Teste 2: A ∨ B ===")
# exp2 = Or(A, B)
# tt2 = TruthTable(exp2)
# tt2.print_truth_table()
#
# print("\n=== Teste 3: ¬A ===")
# exp3 = Not(A)
# tt3 = TruthTable(exp3)
# tt3.print_truth_table()
#
# print("\n=== Teste 4: A → B ===")
# exp4 = Implication(A, B)
# tt4 = TruthTable(exp4)
# tt4.print_truth_table()
#
# print("\n=== Teste 5: Tautologia (A → A) ===")
# exp5 = Implication(A, A)
# tt5 = TruthTable(exp5)
# tt5.print_truth_table()
#
# print("\n=== Teste 6: Contradição (A ∧ ¬A) ===")
# exp6 = And(A, Not(A))
# tt6 = TruthTable(exp6)
# tt6.print_truth_table()
#
# print("\n=== Teste 7: Contingência (A ∨ B) ===")
# exp7 = Or(A, B)
# tt7 = TruthTable(exp7)
# tt7.print_truth_table()
#
# print("\n=== Teste 8: (A ∧ B) → C ===")
# exp8 = Implication(And(A, B), C)
# tt8 = TruthTable(exp8)
# tt8.print_truth_table()
#
# print("\n=== Teste 9: ¬A ∨ (B → C) ===")
# exp9 = Or(Not(A), Implication(B, C))
# tt9 = TruthTable(exp9)
# tt9.print_truth_table()
#
# print("\n=== Teste 10: Equivalência (A → B) e (¬A ∨ B) ===")
#
# exp10_1 = Implication(A, B)
# exp10_2 = Or(Not(A), B)
#
# print("\nTabela de (A → B):")
# TruthTable(exp10_1).print_truth_table()
#
# print("\nTabela de (¬A ∨ B):")
# TruthTable(exp10_2).print_truth_table()
#
# print("\n=== Teste 11: Avaliação manual ===")
#
# context = {'A': True, 'B': False, 'C': True}
#
# exp11 = Implication(And(A, B), C)
#
# print(f"Contexto: {context}")
# print(f"Expressão: {exp11}")
# print(f"Resultado: {exp11.aval(context)}")
