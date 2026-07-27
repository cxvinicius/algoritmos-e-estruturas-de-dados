# Binary Search Tree

Implementação de uma **Árvore Binária de Busca** (*Binary Search Tree — BST*) desenvolvida durante a Missão 02 do projeto **Do Zero ao Estágio**.

A estrutura foi implementada do zero em Python com o objetivo de compreender a organização hierárquica dos dados, a navegação entre nós, a busca baseada em comparações e o uso de recursão em percursos de árvore.

## O que é uma árvore?

Uma árvore é uma estrutura de dados não linear formada por nós conectados de maneira hierárquica.

O primeiro nó é chamado de **raiz**. Cada nó pode possuir referências para outros nós, chamados de filhos.

Nesta implementação, cada nó pode ter no máximo dois filhos:

* filho à esquerda;
* filho à direita.

## Árvore Binária de Busca

Uma Árvore Binária de Busca organiza seus valores seguindo uma regra:

* valores menores que o nó atual são direcionados para a esquerda;
* valores maiores que o nó atual são direcionados para a direita.

Exemplo:

```text
        50
       /  \
     30    70
    / \    / \
   20 40  60 80
```

Essa organização permite procurar valores tomando decisões a cada comparação, sem precisar percorrer obrigatoriamente todos os elementos.

## Estrutura do diretório

```text
tree/
├── __init__.py
├── tree.py
├── README.md
├── examples/
│   ├── __init__.py
│   └── api_response_time_monitor.py
└── tests/
    ├── __init__.py
    └── test_tree.py
```

## Classes implementadas

### `Node`

Representa cada nó da árvore.

Cada nó armazena:

* `data`: valor do nó;
* `left`: referência para o filho esquerdo;
* `right`: referência para o filho direito.

### `BinarySearchTree`

Representa a Árvore Binária de Busca.

Ao ser criada, sua raiz começa com o valor `None`, indicando que a árvore está vazia.

## Métodos

### `insert(data)`

Insere um novo valor na árvore.

O método compara o novo valor com os nós existentes até encontrar uma posição disponível:

* valores menores seguem para a esquerda;
* valores maiores seguem para a direita;
* valores duplicados são ignorados.

### `search(data)`

Procura um valor na árvore.

Retorna:

* `True` quando o valor é encontrado;
* `False` quando o valor não está armazenado.

### `find_min()`

Retorna o menor valor armazenado.

Como os menores valores ficam à esquerda, o método percorre os filhos esquerdos até encontrar o último nó desse caminho.

Se a árvore estiver vazia, retorna `None`.

### `find_max()`

Retorna o maior valor armazenado.

Como os maiores valores ficam à direita, o método percorre os filhos direitos até encontrar o último nó desse caminho.

Se a árvore estiver vazia, retorna `None`.

### `in_order()`

Percorre a árvore seguindo esta ordem:

1. subárvore esquerda;
2. nó atual;
3. subárvore direita.

Em uma Árvore Binária de Busca, esse percurso retorna os valores em ordem crescente.

O método utiliza recursão e retorna uma lista.

## Complexidade

As operações dependem da altura da árvore.

| Operação          | Caso médio | Pior caso |
| ----------------- | ---------: | --------: |
| Inserção          |   O(log n) |      O(n) |
| Busca             |   O(log n) |      O(n) |
| Encontrar mínimo  |   O(log n) |      O(n) |
| Encontrar máximo  |   O(log n) |      O(n) |
| Percurso em ordem |       O(n) |      O(n) |

O pior caso acontece quando os valores são inseridos de maneira já ordenada e a árvore se torna semelhante a uma lista encadeada.

Exemplo:

```text
10
  \
   20
     \
      30
        \
         40
```

Esta implementação não realiza balanceamento automático.

## Example Oficial

O arquivo `api_response_time_monitor.py` simula um pequeno componente de backend responsável por registrar tempos de resposta de uma API.

A árvore é utilizada para:

* armazenar os tempos de resposta;
* consultar se um tempo foi registrado;
* identificar o menor tempo;
* identificar o maior tempo;
* produzir um relatório em ordem crescente.

Para executar o exemplo a partir da raiz do repositório:

```bash
python -m estruturas.tree.examples.api_response_time_monitor
```

## Testes automatizados

Os testes verificam:

* criação de uma árvore vazia;
* inserção da raiz;
* inserção nos lados esquerdo e direito;
* busca de valores existentes e inexistentes;
* localização do menor e do maior valor;
* percurso em ordem crescente;
* tratamento de valores duplicados.

Para executar somente os testes da árvore:

```bash
python -m pytest estruturas/tree/tests -v
```

Para executar todos os testes do repositório:

```bash
python -m pytest -v
```

## Conceitos praticados

* estruturas de dados não lineares;
* relações entre nós;
* raiz, filhos e folhas;
* Árvore Binária de Busca;
* busca baseada em comparações;
* percursos em árvores;
* recursão;
* casos de borda;
* testes automatizados com pytest;
* organização modular de projetos Python.

## Limitações atuais

Esta versão foi criada para estudo dos fundamentos e não possui:

* remoção de nós;
* balanceamento automático;
* armazenamento de valores duplicados;
* outros percursos, como pré-ordem e pós-ordem.

Esses recursos podem ser estudados futuramente em um bloco de aprofundamento.
