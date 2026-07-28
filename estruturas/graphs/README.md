# Graphs

Implementação de um **Grafo** (*Graph*) desenvolvida durante a Missão 02 do projeto **Do Zero ao Estágio**.

A estrutura foi implementada do zero em Python com o objetivo de compreender como representar relações entre objetos, explorar conexões entre vértices e aplicar os algoritmos clássicos de busca em largura (BFS) e profundidade (DFS).

## O que é um grafo?

Um grafo é uma estrutura de dados não linear formada por um conjunto de **vértices** conectados por **arestas**.

Diferentemente das árvores, um vértice pode possuir conexões com vários outros vértices, permitindo representar relacionamentos complexos encontrados em diversos sistemas do mundo real.

Exemplos de aplicações:

- redes sociais;
- mapas e rotas;
- dependências entre serviços;
- redes de computadores;
- sistemas de recomendação.

## Grafos direcionados e não direcionados

Esta implementação suporta dois tipos de grafos.

### Grafo não direcionado

Uma conexão é compartilhada pelos dois vértices.

Exemplo:

```text
A ----- B
```

Se existe uma aresta entre **A** e **B**, ambos são considerados vizinhos.

---

### Grafo direcionado

As conexões possuem direção.

Exemplo:

```text
A -----> B
```

Nesse caso existe uma conexão de **A** para **B**, mas não necessariamente de **B** para **A**.

Esse tipo de grafo é bastante utilizado para representar dependências, fluxos e relacionamentos unilaterais.

## Representação utilizada

Foi utilizada a representação por **lista de adjacência**.

Cada vértice é armazenado como uma chave de um dicionário, enquanto seus vizinhos são armazenados em um conjunto (`set`).

Exemplo:

```text
A → B, C
B → D
C → E
```

Essa representação é eficiente para grafos esparsos e facilita consultas de vizinhos e percursos.

## Estrutura do diretório

```text
graphs/
├── __init__.py
├── graph.py
├── README.md
├── examples/
│   ├── __init__.py
│   └── service_dependency_explorer.py
└── tests/
    ├── __init__.py
    └── test_graph.py
```

## Classe implementada

### `Graph`

Representa um grafo utilizando lista de adjacência.

Ao criar um objeto é possível escolher entre:

- grafo direcionado;
- grafo não direcionado.

## Métodos

### `add_vertex(vertex)`

Adiciona um novo vértice ao grafo.

Caso o vértice já exista, nenhuma alteração é realizada.

---

### `add_edge(source, destination)`

Cria uma conexão entre dois vértices.

Caso algum dos vértices ainda não exista, ele é criado automaticamente.

Em grafos não direcionados, a conexão é criada nos dois sentidos.

---

### `has_vertex(vertex)`

Verifica se um vértice está armazenado.

Retorna:

- `True` quando existir;
- `False` caso contrário.

---

### `has_edge(source, destination)`

Verifica se existe uma aresta entre dois vértices.

Retorna:

- `True` quando a conexão existir;
- `False` caso contrário.

---

### `get_neighbors(vertex)`

Retorna um conjunto contendo todos os vizinhos do vértice informado.

Caso o vértice não exista, retorna um conjunto vazio.

---

### `breadth_first_search(start)`

Realiza uma busca em largura (**Breadth-First Search — BFS**).

O algoritmo visita os vértices por níveis, explorando primeiro todos os vizinhos antes de avançar para níveis mais profundos.

Nesta implementação foi reutilizada a estrutura **Queue**, desenvolvida anteriormente no projeto.

Retorna uma lista com a ordem de visita dos vértices.

---

### `depth_first_search(start)`

Realiza uma busca em profundidade (**Depth-First Search — DFS**).

O algoritmo explora um caminho até o máximo possível antes de retornar para caminhos alternativos.

Nesta implementação foi reutilizada a estrutura **Stack**, também desenvolvida anteriormente.

Retorna uma lista com a ordem de visita dos vértices.

## Complexidade

| Operação | Complexidade |
| --------- | -----------: |
| Inserção de vértice | O(1) |
| Inserção de aresta | O(1) |
| Busca de vértice | O(1) |
| Busca de aresta | O(1) |
| Consulta de vizinhos | O(k) |
| BFS | O(V + E) |
| DFS | O(V + E) |

Onde:

- **V** representa a quantidade de vértices;
- **E** representa a quantidade de arestas;
- **k** representa a quantidade de vizinhos do vértice consultado.

## Example Oficial

O arquivo `service_dependency_explorer.py` simula um pequeno ambiente de microsserviços.

Cada serviço é representado por um vértice, enquanto as dependências entre eles são representadas por arestas direcionadas.

O exemplo demonstra:

- criação de serviços;
- criação de dependências;
- consulta de vértices;
- consulta de arestas;
- consulta de vizinhos;
- busca em largura (BFS);
- busca em profundidade (DFS).

Para executar o exemplo a partir da raiz do repositório:

```bash
python -m estruturas.graphs.examples.service_dependency_explorer
```

## Testes automatizados

Os testes verificam:

- criação de vértices;
- criação de arestas;
- grafos direcionados;
- grafos não direcionados;
- consulta de vizinhos;
- métodos especiais;
- Breadth-First Search;
- Depth-First Search;
- comportamento para vértices inexistentes.

Para executar somente os testes dos grafos:

```bash
python -m pytest estruturas/graphs/tests -v
```

Para executar todos os testes do repositório:

```bash
python -m pytest -v
```

## Conceitos praticados

- grafos;
- vértices e arestas;
- lista de adjacência;
- grafos direcionados;
- grafos não direcionados;
- Breadth-First Search (BFS);
- Depth-First Search (DFS);
- reutilização de estruturas de dados;
- testes automatizados com pytest;
- organização modular de projetos Python.

## Limitações atuais

Esta implementação foi criada para estudo dos fundamentos e ainda não possui:

- remoção de vértices;
- remoção de arestas;
- grafos ponderados;
- detecção de ciclos;
- algoritmo de Dijkstra;
- algoritmo de Prim;
- algoritmo de Kruskal.

Esses recursos serão estudados futuramente em um bloco de aprofundamento sobre grafos.