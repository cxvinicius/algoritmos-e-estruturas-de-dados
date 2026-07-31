# 🎫 Service Desk

> Projeto Final da Missão 02 — Do Zero ao Estágio

Sistema de gerenciamento de chamados desenvolvido para aplicar, em um projeto único, as principais estruturas de dados implementadas durante a Missão 02.

---

## 📚 Estruturas utilizadas

| Estrutura | Responsabilidade |
|-----------|------------------|
| Hash Table | Armazenamento e busca dos chamados |
| Queue | Ordem FIFO de atendimento |
| Stack | Histórico de mudanças de status |
| Binary Search Tree | Relatório ordenado por prioridade |

---

## 🏗️ Arquitetura

```text
                 Novo chamado
                      │
                      ▼
                ServiceDesk
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Hash Table        Queue            Stack
 (Tickets)      (Atendimento)    (Histórico)

                      │
                      ▼
              Binary Search Tree
            (Relatório por prioridade)
```

---

## 📂 Estrutura do projeto

```text
mission_02_service_desk/
├── core/
├── models/
├── examples/
├── tests/
└── README.md
```

---

## ⚙️ Como executar

### Executar o exemplo

```bash
python -m projetos.mission_02_service_desk.examples.service_desk_demo
```

### Executar os testes

```bash
python -m pytest projetos/mission_02_service_desk/tests/test_service_desk.py -v
```

---

## 🚀 Funcionalidades

- ✅ Abrir chamado
- ✅ Buscar chamado por ID
- ✅ Atender próximo chamado
- ✅ Atualizar status
- ✅ Desfazer última alteração de status
- ✅ Listar chamados
- ✅ Gerar relatório ordenado por prioridade

---

## 💻 Exemplo

```text
===== SERVICE DESK =====

✔ Ticket criado:
[TCK-001] Database Error

✔ Próximo atendimento:
[TCK-001]

✔ Status atualizado:
waiting → in_progress

✔ Undo realizado:
in_progress → waiting
```

---

## 🎯 Conceitos demonstrados

- Programação Orientada a Objetos
- Estruturas de Dados
- Organização em camadas
- Responsabilidade única
- Reutilização de código
- Testes automatizados com pytest

---

## 🛠️ Tecnologias

- Python 3
- Pytest
- Git
- GitHub

---

## 📌 Projeto desenvolvido durante a trilha

**Do Zero ao Estágio**

Missão 02 — Estruturas de Dados