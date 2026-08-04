# 🫧 Bubble Sort

Implementação do algoritmo **Bubble Sort** desenvolvida durante a **Missão 03 — Algoritmos** da trilha **Do Zero ao Estágio**.

---

# 📖 Sobre

Bubble Sort é um algoritmo de ordenação baseado na comparação de elementos vizinhos.

Durante cada passagem pela lista, elementos fora de ordem são trocados de posição, fazendo com que os maiores valores sejam deslocados gradualmente para o final da lista.

> **Observação:** o Bubble Sort é utilizado neste projeto com finalidade **didática**, permitindo compreender os fundamentos dos algoritmos de ordenação.

---

# 🎯 Objetivo

Implementar o Bubble Sort do zero para compreender:

* Comparação entre elementos;
* Troca de posições;
* Laços de repetição aninhados;
* Otimizações simples;
* Análise de complexidade.

---

# 📂 Estrutura da pasta

```text
bubble_sort/
│
├── __init__.py
├── bubble_sort.py
├── README.md
├── examples/
│   ├── __init__.py
│   └── exam_score_organizer.py
└── tests/
    ├── __init__.py
    └── test_bubble_sort.py
```

---

# 🚀 Aplicações

Embora não seja utilizado em aplicações que exigem alto desempenho, o Bubble Sort é bastante útil para:

* Ensino de algoritmos;
* Visualização de ordenação;
* Introdução à análise de complexidade;
* Compreensão de algoritmos baseados em comparação.

---

# 📈 Complexidade

| Caso      | Complexidade |
| :-------- | :----------: |
| 🟢 Melhor |   **O(n)**   |
| 🟡 Médio  |   **O(n²)**  |
| 🔴 Pior   |   **O(n²)**  |

---

# ▶️ Example Oficial

Nesta sprint foi desenvolvido o exemplo:

**Exam Score Organizer**

O programa organiza uma pequena lista de notas utilizando a implementação do Bubble Sort.

### Executar

```bash
python -m algoritmos.bubble_sort.examples.exam_score_organizer
```

---

# 🧪 Testes

Os testes automatizados validam os principais comportamentos do algoritmo:

* Lista desordenada;
* Lista já ordenada;
* Lista em ordem inversa;
* Valores duplicados;
* Lista vazia;
* Lista com um elemento;
* Preservação da lista original.

### Executar

```bash
python -m pytest algoritmos/bubble_sort/tests/test_bubble_sort.py -v
```

---

# 📌 Status

* [x] Implementação
* [x] Example Oficial
* [x] Testes automatizados
* [x] Documentação
* [x] README
