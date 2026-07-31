Service Desk — Projeto Final da Missão 02

Sistema de gerenciamento de chamados desenvolvido como projeto final da Missão 02 — Estruturas de Dados da trilha Do Zero ao Estágio.

O projeto integra estruturas de dados implementadas anteriormente no repositório, atribuindo a cada uma uma responsabilidade real e bem delimitada. O objetivo não é reproduzir um sistema corporativo completo, mas demonstrar domínio de organização de código, orientação a objetos, testes automatizados e aplicação prática de estruturas de dados.

Objetivo

Construir um Service Desk pequeno e funcional capaz de:

abrir chamados;

armazenar e buscar chamados por ID;

controlar a ordem de atendimento;

atualizar o status de um chamado;

desfazer a última mudança de status;

listar os chamados cadastrados;

gerar um relatório ordenado por prioridade.

Estruturas de dados utilizadas

Estrutura

Responsabilidade no projeto

Hash Table

Armazenar os chamados e permitir busca por ID

Queue

Controlar os chamados aguardando atendimento em ordem FIFO

Stack

Registrar mudanças de status e permitir desfazer a última alteração

Binary Search Tree

Gerar um relatório de chamados em ordem crescente de prioridade

A BST é usada somente para relatório. Ela não interfere na ordem real de atendimento, que continua sendo responsabilidade exclusiva da Queue.

Escopo

Funcionalidades implementadas

abrir chamado;

buscar chamado por ID;

atender o próximo chamado da fila;

atualizar status;

desfazer a última mudança de status;

listar chamados cadastrados;

exibir relatório de prioridades usando BST.

Fora do escopo

banco de dados;

persistência em arquivos;

API;

interface gráfica;

autenticação;

controle de permissões;

múltiplos atendentes;

exclusão complexa;

uso de Graph ou Linked List.

Esses limites são intencionais. O projeto prioriza clareza, conclusão e qualidade arquitetural, evitando implementar recursos sem necessidade real.

Organização do projeto

projetos/
└── mission_02_service_desk/
    ├── __init__.py
    ├── models/
    │   ├── __init__.py
    │   └── ticket.py
    ├── core/
    │   ├── __init__.py
    │   └── service_desk.py
    ├── examples/
    │   ├── __init__.py
    │   └── service_desk_demo.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_service_desk.py
    └── README.md

As estruturas não são reimplementadas dentro do projeto. O ServiceDesk importa diretamente as classes já existentes em estruturas/.

Modelo Ticket

A classe Ticket representa um chamado do sistema.

Cada objeto possui:

Atributo

Responsabilidade

ticket_id

Identificador único gerado automaticamente

title

Título resumido do chamado

description

Descrição do problema ou solicitação

priority

Prioridade do chamado

status

Estado atual do atendimento

Prioridades permitidas

low
medium
high

Status permitidos

waiting
in_progress
resolved

Todo chamado começa com status waiting.

Classe ServiceDesk

A classe ServiceDesk coordena as regras do sistema e a integração entre as estruturas de dados.

Atributos principais

self.tickets

Hash Table responsável por armazenar os objetos Ticket usando o ID como chave.

self.waiting_tickets

Queue que armazena os IDs dos chamados aguardando atendimento.

self.status_history

Stack que registra as alterações de status necessárias para a operação de desfazer.

self.ticket_ids

Lista auxiliar com os IDs cadastrados. Ela existe porque a Hash Table criada na missão não oferece um método público para percorrer todos os valores.

self.next_ticket_number

Número usado para gerar IDs sequenciais.

Métodos

_generate_ticket_id()

Gera IDs sequenciais no formato:

TCK-001
TCK-002
TCK-003

É um método privado porque essa geração pertence ao funcionamento interno do serviço.

_validate_priority(priority)

Verifica se a prioridade informada pertence às prioridades permitidas pelo modelo Ticket.

Caso o valor seja inválido, lança ValueError.

_validate_status(status)

Verifica se o novo status pertence aos status permitidos.

Caso o valor seja inválido, lança ValueError.

_change_status(ticket, new_status)

Centraliza a alteração de status.

Fluxo:

recebe o Ticket e o novo status
        ↓
verifica se o status realmente mudou
        ↓
guarda o status anterior
        ↓
altera o objeto Ticket
        ↓
registra a mudança na Stack
        ↓
retorna o Ticket atualizado

A Stack armazena somente:

(ticket_id, status_anterior)

Essas são exatamente as informações necessárias para desfazer a alteração.

open_ticket(title, description, priority)

Abre um novo chamado.

Fluxo:

valida a prioridade
        ↓
gera o ID
        ↓
cria um objeto Ticket
        ↓
armazena o Ticket na Hash Table
        ↓
adiciona o ID à Queue
        ↓
registra o ID na lista auxiliar
        ↓
retorna o novo Ticket

find_ticket(ticket_id)

Busca um chamado na Hash Table usando seu ID.

Retorna:

o objeto Ticket, quando encontrado;

None, quando o ID não existe.

attend_next_ticket()

Atende o primeiro chamado da Queue.

Como a Queue segue FIFO, o primeiro chamado aberto será o primeiro retirado para atendimento.

Fluxo:

remove o primeiro ID da Queue
        ↓
busca o Ticket na Hash Table
        ↓
altera o status para in_progress
        ↓
registra o status anterior na Stack
        ↓
retorna o Ticket atendido

Retorna None quando a fila está vazia.

update_status(ticket_id, new_status)

Atualiza o status de um chamado específico.

O método valida o novo status, busca o chamado e reutiliza _change_status() para evitar repetição de lógica.

undo_last_status_change()

Desfaz a última alteração de status registrada.

Fluxo:

remove a última mudança da Stack
        ↓
recupera ticket_id e status anterior
        ↓
busca o Ticket na Hash Table
        ↓
restaura o status anterior
        ↓
retorna o Ticket restaurado

O comportamento é LIFO: a última mudança realizada é a primeira a ser desfeita.

Retorna None quando não existe histórico.

list_tickets()

Retorna todos os chamados cadastrados na ordem de abertura.

A lista ticket_ids é percorrida e cada objeto é recuperado por meio de find_ticket().

O método não acessa diretamente os buckets internos da Hash Table.

get_priority_report()

Cria um relatório temporário de chamados ordenados por prioridade.

A ordem adotada é:

low → medium → high

O método cria uma BST temporária e insere tuplas no formato:

(priority_rank, ticket_id, ticket)

O ranking existe apenas dentro desse método, pois sua única função é permitir a ordenação do relatório.

O ticket_id diferencia chamados com a mesma prioridade. Isso é necessário porque a BST implementada na missão ignora valores duplicados.

Depois do percurso in_order(), o método devolve somente os objetos Ticket.

Fluxo geral

Usuário abre chamado
        ↓
Ticket é criado
        ↓
Hash Table armazena o objeto
        ↓
Queue recebe o ID
        ↓
Chamado aguarda atendimento
        ↓
attend_next_ticket() retira o primeiro ID
        ↓
Status muda para in_progress
        ↓
Stack registra o status anterior
        ↓
Status pode ser atualizado ou desfeito

Por que a Queue armazena IDs?

A Hash Table é a fonte principal dos dados.

A Queue precisa apenas indicar a ordem de atendimento, por isso armazena o ticket_id em vez de manter outra cópia do objeto.

Queue: TCK-001 → TCK-002 → TCK-003
             ↓
Hash Table localiza o objeto completo

Isso reduz duplicação e mantém cada estrutura com uma responsabilidade clara.

Por que a BST não controla o atendimento?

A Queue representa a ordem real de chegada dos chamados.

A BST existe apenas para produzir uma visualização ordenada por prioridade.

Queue → operação do atendimento
BST   → relatório

Assim, as duas estruturas não disputam a responsabilidade de decidir qual chamado será atendido.

Como adicionar ao repositório

A pasta deve ficar neste caminho, considerando a raiz do repositório:

algoritmos-e-estruturas-de-dados/
└── projetos/
    └── mission_02_service_desk/

Portanto, copie o conteúdo deste projeto para:

C:\Dev\01_Projetos\00_Em_desenvolvimento\algoritmos-e-estruturas-de-dados\projetos\mission_02_service_desk

Executar o example oficial

Abra o terminal na raiz do repositório:

cd C:\Dev\01_Projetos\00_Em_desenvolvimento\algoritmos-e-estruturas-de-dados

Depois execute:

python -m projetos.mission_02_service_desk.examples.service_desk_demo

Não execute o arquivo diretamente pelo botão do Code Runner, pois os imports foram organizados para execução como módulo.

Executar os testes do projeto

Na raiz do repositório:

python -m pytest projetos/mission_02_service_desk/tests/test_service_desk.py -v

Para executar todos os testes do repositório:

python -m pytest -v

Testes implementados

Os testes verificam:

criação e armazenamento do chamado;

geração do primeiro ID;

inclusão na Queue;

busca de ID inexistente;

atendimento em ordem FIFO;

fila vazia;

atualização de status;

histórico na Stack;

chamado inexistente;

desfazer última alteração;

histórico vazio;

listagem dos chamados;

ordenação de prioridades;

preservação de prioridades repetidas;

rejeição de prioridades inválidas;

rejeição de status inválidos.

Executar o projeto em um ambiente virtual

Caso o ambiente virtual ainda não esteja ativado:

.\.venv\Scripts\Activate.ps1

Depois confirme o Python utilizado:

where.exe python

O primeiro resultado deve apontar para o Python dentro de .venv.

Tecnologias e conceitos demonstrados

Python;

orientação a objetos;

modularização;

imports entre pacotes;

Hash Table;

Queue e FIFO;

Stack e LIFO;

Binary Search Tree;

percurso in-order;

validação de regras de domínio;

testes automatizados com pytest;

organização profissional de repositório.

Decisões arquiteturais

Nenhuma estrutura foi reimplementada

O projeto reutiliza as implementações construídas durante a Missão 02.

Cada estrutura possui uma única responsabilidade

Hash Table armazena e busca;

Queue controla espera;

Stack mantém histórico;

BST gera relatório.

Nenhuma funcionalidade foi adicionada sem necessidade

O projeto não inclui persistência, API, interface, autenticação ou integrações artificiais.

Métodos privados concentram regras internas

A geração de IDs, validações e alteração de status ficam centralizadas, reduzindo repetição e mantendo os métodos públicos legíveis.

Resultado

Este projeto encerra a Missão 02 demonstrando que estruturas de dados não são apenas exercícios isolados. Elas podem colaborar dentro de um sistema pequeno, desde que cada uma tenha uma responsabilidade clara e justificada.