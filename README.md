# Motor de lógica Booleana
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Este projeto implementa um motor de inferência lógica baseado em lógica proposicional,
utilizando árvores sintáticas (AST) para representação de expressões e regras formais
de inferência como _Modus Ponens_ e _Modus Tollens_.

Após ter uma matéria de lógica na faculdade, resolvi testar e aprimorar meus conhecimentos tanto em programação com Python, quanto na lógica em si.

<ul>
    <li><a href="#classes">Classes</a></li>
    <li><a href="#expressoes">Criando expressões</a></li>
    <li><a href="#valores">Atribuindo valores lógicos</a></li>
    <li><a href="#tabela">Tabela Verdade</a></li>
    <li><a href="#inferencia">Novos argumentos por inferência</a></li>
    <li><a href="#provas">Provando argumentos específicos</a></li>
    <li><a href="#uso">Como usar</a></li>
</ul>

---

### Exemplos
A partir das proposições ``P`` e `P → Q`, o programa infere a proposição `Q` por _Modus Ponens_

```python
p = Var('P')
q = Var('Q')
imp = Implication(p, q)
step1 = Step(hipotesis=p)
step2 = Step(hipotesis=imp)

engine.run([step1, step2])
```
Saída
>> 1. P (Hipotesis)
>> 2. (P → Q) (Hipotesis)
>> 3. Q (Modus Ponens [MP]: 1, 2)

---

<div id="classes">

## Classes
### Var (`name`)
É a menor unidade da expressão lógica, são as proposições em si, representadas por letras.
Para criar os objetos que serão as proposições, utilizamos esta classe e atribuimos uma letra.

<table>
  <tr>
    <th colspan="2">Atributos</th>
  </tr>
  <tr>
    <td><code>name</code></td>
    <td>Nome dado à proposição. Utilize uma letra maiúscula.</td>
  </tr>
</table>


**Exemplo**
```python
p = Var('P')
q = Var('Q')

print(p)
print(q)
```
`>> P`

`>> Q`

---

### Or (`left`, `right`)
É utilizada para representar a disjunção (∨) entre proposições.

<table>
  <tr>
    <th colspan="2">Atributos</th>
  </tr>
  <tr>
    <td><code>left</code></td>
    <td>Primeiro valor a ser utilizado na expressão OR</td>
  </tr>
<tr>
    <td><code>right</code></td>
    <td>Segundo valor a ser utilizado na expressão OR</td>
  </tr>
</table>

**Exemplo**

```python
p = Var('P')
q = Var('Q')

print(Or(p, q))
```
`>>> (P ∨ Q)`

---

### And (`left`, `right`)
É utilizada para representar a conjunção (∧) entre proposições.

<table>
  <tr>
    <th colspan="2">Atributos</th>
  </tr>
  <tr>
    <td><code>left</code></td>
    <td>Primeiro valor a ser utilizado na expressão AND</td>
  </tr>
<tr>
    <td><code>right</code></td>
    <td>Segundo valor a ser utilizado na expressão AND</td>
  </tr>
</table>

**Exemplo**

```python
p = Var('P')
q = Var('Q')

print(And(p, q))
```
`>>> (P ∧ Q)`

---

### Not (`expr`)
É utilizada para representar a negação (¬) de proposições.

<table>
  <tr>
    <th colspan="2">Atributos</th>
  </tr>
  <tr>
    <td><code>expr</code></td>
    <td>Expressão a ser negada</td>
  </tr>
</table>

**Exemplo**
```python
p = Var('P')

print(Not(p))
```
`>>> ¬P`

---

### Implication (`left`, `right`)

É utilizada para representar a relação condicional (→) entre proposições.

<table>
  <tr>
    <th colspan="2">Atributos</th>
  </tr>
  <tr>
    <td><code>left</code></td>
    <td>Expressão antecedente</td>
  </tr>
<tr>
    <td><code>right</code></td>
    <td>Expressão consequente</td>
  </tr>
</table>
<br>

**Exemplo**

```python
p = Var('P')
q = Var('Q')

print(Implication(p, q))
```
`>>> P → Q`
</div>

<div id="expressoes">

---

### Expressões mais complexas
Assim como nas expressões comuns, também podemos usá-las umas dentro da outra, bastando apenas prestar atenção ao aninhamento.

Expressão `(¬P → Q) ∧ R`
```python
p = Var('P')
q = Var('Q')
r = Var('R')

expressao = And(Implication(Not(p), q), r)
print(expressao)
```
`>>> ((¬P → Q) ∧ R)`

---
</div>

<div id="valores">

### Atribuindo valores lógicos
Ao instanciar as classes é importante notar que elas só representam as estruturas lógicas das expressões. Elas não não possuem valor lógico inicialmente.

Para atribuir valores lógicos às expressões, precisamos utilizar o método `aval()`, que todas elas possuem. Esse método recebe um dicionário como parâmetro e nele, identificamos as proposições (chaves) e os seus respectivos valores.

```
EXPRESSÃO: P ∧ Q
Com P=1 e Q=0
O resultado entre 1 ∧ 0 é 0
```

```python
p = Var('P')
q = Var('Q')

expr = And(p, q)

contexto = {
    'P': True, # 1
    'Q': False # 0
}

print(expr.aval(contexto))
```
`>>> False`


Cada proposição utilizada na expressão, precisa ter um par de chave-valor no dicionário, onde a chave é seu nome, informado na hora de instanciar a proposição.

```
EXPRESSÃO: (P ∧ Q) → (R ∨ ¬Q)
Com P=1, Q=0 e R=0
O resultado entre (1 ∧ 0) → (0 ∨ ¬0) é 1
```

`(P ∧ Q) → (R ∨ ¬Q)`
```python
p = Var('P')
q = Var('Q')
r = Var('R')

expr = Implication((And(p, q)), (Or(r, Not(q))))

contexto = {
    'P': True, # 1
    'Q': False, # 0
    'R': False # 0
}

print(expr)
print(expr.aval(contexto))
```
`>>> ((P ∧ Q) → (R ∨ ¬Q))`

`>>> True`

---

</div>

<div id="tabela">

---

### Tabela-Verdade (`exp`)
A classe ``TruthTable`` gera a tabela-verdade para uma determinada expressão.

<table>
  <tr>
    <th colspan="2">Atributos</th>
  </tr>
  <tr>
    <td><code>expr</code></td>
    <td>Expressão da qual será construida a tabela-verdade</td>
  </tr>
</table>

Após gerar a tabela, a expressão também é classificada como:
- ``Tautologia`` - Todos os resultados possíveis são verdadeiros. 
- ``Contradição`` - Todos os resultados possíveis são falsos. 
- ``Contingência`` - As combinações assumem valores verdadeiros e falsos. 


**Exemplo**

Gerando a tabela-verdade para a expressão `(P ∧ Q) → (R ∨ ¬Q)`

```python
p = Var('P')
q = Var('Q')
r = Var('R')

expr = Implication((And(p, q)), (Or(r, Not(q))))

tt = TruthTable(expr)
tt.print_truth_table()
```

| P | Q | R | ((P ∧ Q) → (R ∨ ¬Q)) |
|---|---|---|----------------------|
| 1 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 0 | 1 | 1 |
| 0 | 0 | 0 | 1 |

**Expression Type: CONTINGENCY**

---

</div>

<div id="inferencia">

### Novos argumentos por inferência e equivalência
O programa implementa a inferência de novos argumentos utilizando:
- _Modus Ponens_ (MP)
- _Modus Tollens_ (MT)
- Dupla Negação (DN)
- Lei de Morgan (de Morgan) [Em implementação]
- Comutatividade (COM) [Em implementação]
- Associatividade (ASS) [Em implementação]
- Distributividade (DIST) [Em implementação]
- Condicional (COND) [Em implementação]
- Contraposição (CONT) [Em implementação]
- Silogismo Hipotético (SH) [Em implementação]
- Silogismo Disjuntivo (SD) [Em implementação]

A responsável por controlar e gerar as novas expressões é a classe `Step(hipotesis, rule_name, dependencies_index)`.

<table>
  <tr>
    <th colspan="2">Atributos</th>
  </tr>
  <tr>
    <td><code>hipotesis</code></td>
    <td>Expressão que iremos utilizar na inferência.</td>
  </tr>
<tr>
    <td><code>rule_name</code></td>
    <td>Nome da regra utilizada para chegar naquela expressão. Por padrão, seu valor é a string "hipotesis". As expressões iniciais são sempre "hipotesis".</td>
  </tr>
<tr>
    <td><code>dependencies_index</code></td>
    <td>Lista com os índices das expressões utilizadas para chegar nas novas expressões. Por padrão, seu valor é uma lista vazia.</td>
  </tr>
</table>

</div>

**Exemplo**
```python
p = Var('P')
q = Var('Q')
imp = Implication(p, q)
```
Temos 3 expressões. `P` e `Q`, representando proposições simples e `imp`, representando o condicional `P → Q`. Precisamos inserir estas expressões na classe `Step`.
```python
step1 = Step(hipotesis=p)
step2 = Step(hipotesis=imp)
```
Como são as expressões iniciais, não precisamos passar os atributos ``rule_name`` e `dependencies_index`, eles serão preenchidos pelo próprio 
programa ao gerar novas expressões.

Temos os argumentos: ``P`` e `P → Q`, através de _Modus Ponens_, podemos inferir `Q`

Faremos isso, utilizando a função ``run(premisses_steps)`` do módulo ``engine``.
Precisamos passar como argumentos, uma lista de ``Step`` e a partir desta lista, serão gerados e impresos na tela, as novas conclusões. 

```python
p = Var('P')
q = Var('Q')
imp = Implication(p, q)
step1 = Step(hipotesis=p)
step2 = Step(hipotesis=imp)

engine.run([step1, step2])
```

>> 1. P (Hipotesis)
>> 2. (P → Q) (Hipotesis)
>> 3. Q (Modus Ponens [MP]: 1, 2)

A expressão 3, foi inferida automaticamente, utilizando _Modus Ponens_ (MP) e as expressões 1 e 2.

---

<div id="provas">

### Provando argumentos específicos [Em implementação]
Dado um argumento, o programa prova se ele é válido ou não. Utilizando as regras de inferência e de equivalência tautológica, o programa verifica se a conclusão é válida de acordo com as premissas dadas.


</div>

---

<div id="uso">

### Como usar
#### 1. Instalação
Clone o repositório:
```
git clone https://github.com/Vinicius-GRibeiro/InferenceEngine.git
```

<br>

#### 2. Crie proposições
As proposições são representadas pela classe ``Var``
```python
from boolean_logic.ast_types.ast_var import Var

p = Var('P')
q = Var('Q')
```

<br>

#### 3. Monte expressões
Utilize as classes que representam as expressões básicas.

```python
from boolean_logic.ast_types.ast_and import And
from boolean_logic.ast_types.ast_or import Or
from boolean_logic.ast_types.ast_not import Not
from boolean_logic.ast_types.ast_implication import Implication

p = Var('P')
q = Var('Q')

expr = Implication(And(p, q), Or(p, Not(q)))

print(expr)
```
> ((P ∧ Q) → (P ∨ ¬Q))

<br>

#### 4. Avaliando expressões
Para avaliar uma expressão, utilize o método ``aval()`` passando um dicionário com os valores:

```python
from boolean_logic.ast_types.ast_and import And
from boolean_logic.ast_types.ast_or import Or
from boolean_logic.ast_types.ast_not import Not
from boolean_logic.ast_types.ast_implication import Implication

p = Var('P')
q = Var('Q')

expr = Implication(And(p, q), Or(p, Not(q)))

contexto = {
    'P': True,
    'Q': False
}

resultado = expr.aval(contexto)
print(resultado)
```
>> ((P ∧ Q) → (P ∨ ¬Q))
> True

<br>

#### 5. Gerando Tabela-Verdade

```python
from boolean_logic.ast_types.ast_and import And
from boolean_logic.ast_types.ast_or import Or
from boolean_logic.ast_types.ast_not import Not
from boolean_logic.ast_types.ast_implication import Implication
from core.truth_table import TruthTable

p = Var('P')
q = Var('Q')

expr = Implication(And(p, q), Or(p, Not(q)))

tt = TruthTable(expr)
tt.print_truth_table()
```

Isso irá gerar todas as combinações possíveis e classificar a expressão como:

- Tautologia
- Contradição
- Contingência

<br>

#### 6. Inferência automática
O motor de inferência gera novas conclusões a partir de premissas.

```python
from step import Step
from engine import run

p = Var('P')
q = Var('Q')

imp = Implication(p, q)

steps = [
    Step(p),
    Step(imp)
]

run(steps)
```

Saída esperada:
```
1. P (Hipotesis)
2. (P → Q) (Hipotesis)
3. Q (Modus Ponens [MP]: 1, 2)
```

</div>
