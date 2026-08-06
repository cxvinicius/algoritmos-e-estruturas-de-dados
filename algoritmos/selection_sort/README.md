# 🔎 Selection Sort

> Implementação do algoritmo **Selection Sort** desenvolvida durante a **Missão 03 — Sprint 02** da trilha **Do Zero ao Estágio**.

---

## 📌 Sobre o algoritmo

O **Selection Sort** é um algoritmo de ordenação baseado na seleção do menor elemento disponível.

A cada rodada, o algoritmo percorre a parte ainda não ordenada da lista, identifica o menor valor e o coloca na posição correta.

Sua lógica pode ser resumida em três etapas:

1. selecionar a posição atual;
2. procurar o menor elemento na parte restante da lista;
3. trocar o menor elemento encontrado com o valor da posição atual.

---

## ⚙️ Como funciona

Considere a lista:

```text
[64, 25, 12, 22, 11]
```

Na primeira rodada, o algoritmo procura o menor valor de toda a lista.

```text
Menor valor encontrado: 11
```

Depois, troca o valor `11` com o elemento da primeira posição:

```text
[11, 25, 12, 22, 64]
```

Na rodada seguinte, a primeira posição não precisa mais ser analisada:

```text
[11 | 25, 12, 22, 64]
```

O processo continua até que toda a lista esteja ordenada:

```text
[11, 12, 22, 25, 64]
```

---

## 🧠 Estrutura da lógica

Durante a execução, o algoritmo utiliza três índices principais:

- `current_index`: posição que está sendo organizada;
- `min_index`: posição do menor valor encontrado;
- `comparison_index`: posição utilizada para percorrer a parte não ordenada.

O `min_index` começa com o mesmo valor de `current_index`.

```python
min_index = current_index
```

Quando um elemento menor é encontrado, o índice é atualizado:

```python
if sorted_values[comparison_index] < sorted_values[min_index]:
    min_index = comparison_index
```

Depois que toda a região restante é analisada, a troca é realizada:

```python
sorted_values[current_index], sorted_values[min_index] = (
    sorted_values[min_index],
    sorted_values[current_index],
)
```

---

## 💻 Implementação

```python
def selection_sort(values):
    sorted_values = values.copy()

    for current_index in range(len(sorted_values) - 1):
        min_index = current_index

        for comparison_index in range(
            current_index + 1,
            len(sorted_values),
        ):
            if sorted_values[comparison_index] < sorted_values[min_index]:
                min_index = comparison_index

        if min_index != current_index:
            sorted_values[current_index], sorted_values[min_index] = (
                sorted_values[min_index],
                sorted_values[current_index],
            )

    return sorted_values
```

A função cria uma cópia da lista recebida. Dessa forma, os valores originais são preservados.

---

## 🔄 Selection Sort x Bubble Sort

| Característica | Bubble Sort | Selection Sort |
|---|---|---|
| Estratégia | Compara elementos vizinhos | Seleciona o menor elemento |
| Trocas | Podem acontecer várias vezes por rodada | No máximo uma troca por rodada |
| Melhor caso | `O(n)` com otimização | `O(n²)` |
| Caso médio | `O(n²)` | `O(n²)` |
| Pior caso | `O(n²)` | `O(n²)` |
| Espaço auxiliar | `O(1)` | `O(1)` |
| Estabilidade | Estável | Geralmente não estável |

O Selection Sort costuma realizar menos trocas, mas continua fazendo muitas comparações.

---

## ⏱️ Complexidade

### Tempo

| Cenário | Complexidade |
|---|---|
| Melhor caso | `O(n²)` |
| Caso médio | `O(n²)` |
| Pior caso | `O(n²)` |

Mesmo quando a lista já está ordenada, o algoritmo continua procurando um elemento menor na parte restante.

### Espaço

```text
O(1)
```

O algoritmo utiliza apenas algumas variáveis auxiliares, sem criar outra estrutura proporcional ao tamanho da entrada.

> Nesta implementação, uma cópia da lista é criada para preservar os dados originais. Portanto, considerando essa decisão da função, existe também o custo da nova lista retornada.

---

## 🏆 Example Oficial

O Example Oficial da sprint é o **Tournament Time Ranking**.

O programa recebe tempos de corrida e utiliza o Selection Sort para organizá-los do competidor mais rápido para o mais lento.

### Dados utilizados

```python
race_times = [30, 34, 56, 60, 45, 23, 29]
```

### Resultado esperado

```text
===== TOURNAMENT TIME RANKING =====

Recorded times:
30 seconds
34 seconds
56 seconds
60 seconds
45 seconds
23 seconds
29 seconds

Ranking from fastest to slowest:
1. 23 seconds
2. 29 seconds
3. 30 seconds
4. 34 seconds
5. 45 seconds
6. 56 seconds
7. 60 seconds
```

---

## ▶️ Como executar o exemplo

Na raiz do projeto, execute:

```bash
python -m algoritmos.selection_sort.examples.tournament_time_ranking
```

---

## 🧪 Como executar os testes

Na raiz do projeto, execute todos os testes:

```bash
python -m pytest -v
```

Para executar somente os testes do Selection Sort:

```bash
python -m pytest algoritmos/selection_sort/tests/test_selection_sort.py -v
```

---

## 📁 Organização

```text
selection_sort/
├── __init__.py
├── selection_sort.py
├── README.md
├── examples/
│   ├── __init__.py
│   └── tournament_time_ranking.py
└── tests/
    ├── __init__.py
    └── test_selection_sort.py
```

---

## 🎯 Aprendizados da sprint

Nesta sprint foram praticados:

- divisão entre região ordenada e não ordenada;
- controle de índices;
- busca pelo menor elemento;
- troca de valores por posição;
- análise de complexidade;
- comparação entre algoritmos;
- preservação da lista original;
- criação de testes automatizados com pytest.

---

## 📚 Projeto

Este algoritmo faz parte do repositório **Algoritmos e Estruturas de Dados**, desenvolvido durante a trilha **Do Zero ao Estágio**.
