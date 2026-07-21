# Linked List (Lista Ligada)

## 📚 O que é?

Uma Linked List (Lista Ligada) é uma estrutura de dados linear composta por nós (Nodes).

Cada nó armazena:

- um valor (`data`);
- uma referência para o próximo nó (`next`).

Diferente de uma lista do Python (`list`), os elementos não ficam armazenados de forma contínua na memória.

---

## Estrutura

```text
Head
 ↓
[A] → [B] → [C] → None
```

Cada elemento conhece apenas o próximo.

---

## Complexidade

| Operação | Complexidade |
|----------|--------------|
| prepend  | O(1)         |
| append   | O(n)         |
| find     | O(n)         |
| remove   | O(n)         | 

---

## Métodos implementados

- prepend()
- append()
- find()
- remove()
- __len__()
- __str__()

---

## Exemplo oficial

O exemplo desta sprint simula a configuração de uma pipeline de requisições em uma aplicação Back-End.

```text
Logging
↓

Authentication
↓

Validation
↓

Controller
```

O objetivo é apenas demonstrar onde uma Linked List pode aparecer em um sistema real.

---

## Estrutura da pasta

```text
linked_list/
│
├── linked_list.py
├── examples/
├── tests/
├── README.md
└── __init__.py
```

---

## Testes

Executar:

```bash
python -m pytest estruturas/linked_list/tests -v
```

Todos os comportamentos principais da estrutura possuem testes automatizados.

---

## Aprendizados

Durante esta sprint foram estudados:

- criação de nós;
- referências entre objetos;
- ponteiros (`next`);
- percorrer listas ligadas;
- inserção;
- remoção;
- busca;
- representação textual da estrutura.