# 📌 Insertion Sort

> Implementação do algoritmo **Insertion Sort** desenvolvida durante a **Missão 03 — Algoritmos** da trilha **Do Zero ao Estágio**.

---

# 📖 Sobre

O **Insertion Sort** é um algoritmo de ordenação baseado na ideia de **inserir cada elemento na posição correta dentro de uma região já ordenada da lista**.

Seu funcionamento é semelhante à forma como organizamos cartas de baralho nas mãos: a cada nova carta recebida, ela é inserida no lugar correto entre as cartas já organizadas.

É um algoritmo simples, estável e bastante eficiente para listas pequenas ou parcialmente ordenadas.

---

# ⚙️ Funcionamento

O algoritmo segue os seguintes passos:

1. Considera o primeiro elemento como uma região ordenada.
2. Percorre a lista a partir do segundo elemento.
3. Armazena o elemento atual temporariamente.
4. Compara esse elemento com os anteriores.
5. Desloca os elementos maiores uma posição para a direita.
6. Insere o elemento armazenado na posição correta.
7. Repete o processo até o final da lista.

---

# 📈 Complexidade

| Caso | Complexidade |
|------|--------------|
| Melhor Caso | **O(n)** |
| Caso Médio | **O(n²)** |
| Pior Caso | **O(n²)** |
| Memória | **O(1)** (in-place) |

---

# ✅ Vantagens

- Implementação simples.
- Algoritmo estável.
- Excelente desempenho em listas pequenas.
- Muito eficiente para listas parcialmente ordenadas.
- Utilizado como parte de algoritmos modernos, como o **TimSort**.

---

# ❌ Desvantagens

- Pouco eficiente para listas grandes.
- Complexidade quadrática no caso médio e pior caso.
- Perde desempenho quando a lista está muito desordenada.

---

# 📂 Estrutura

```text
insertion_sort/
├── __init__.py
├── insertion_sort.py
├── README.md
├── examples/
│   ├── __init__.py
│   └── example_oficial.py
└── tests/
    ├── __init__.py
    └── test_insertion_sort.py
```

---

# ▶️ Exemplo Oficial

O projeto contém um exemplo simulando a organização cronológica dos registros de check-in de uma conferência.

```
===== CONFERENCE CHECK-IN ORGANIZER =====

Recorded check-ins:
08:00
08:03
08:06
08:10
08:08
08:12
08:15

Check-ins in chronological order:
1. 08:00
2. 08:03
3. 08:06
4. 08:08
5. 08:10
6. 08:12
7. 08:15
```

---

# 🧪 Testes

Os testes automatizados validam os principais comportamentos do algoritmo:

- Lista desordenada;
- Lista já ordenada;
- Lista em ordem inversa;
- Lista com elementos duplicados;
- Lista vazia;
- Preservação da lista original.

Execute os testes com:

```bash
python -m pytest -v
```

---

# 🚀 Execução

Para executar o Example Oficial:

```bash
python -m algoritmos.insertion_sort.examples.example_oficial
```

---

# 📚 Aprendizados

Durante esta sprint foram estudados:

- Ordenação por inserção;
- Região ordenada e região não processada;
- Deslocamento de elementos;
- Estabilidade do algoritmo;
- Complexidade de tempo;
- Comparação com Bubble Sort e Selection Sort;
- Aplicações práticas do Insertion Sort.

---

## 👨‍💻 Projeto

Desenvolvido durante a trilha **Do Zero ao Estágio**, com foco na implementação manual de algoritmos e estruturas de dados utilizando **Python**, priorizando compreensão profunda, organização de código e boas práticas de desenvolvimento.