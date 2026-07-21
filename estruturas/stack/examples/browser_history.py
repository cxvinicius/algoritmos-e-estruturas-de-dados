from estruturas.stack.stack import Stack

historico = Stack()

print("\n=== NAVEGANDO ===")
historico.push("google.com")
historico.push("github.com")
historico.push("github.com/cxvinicius/projetos")
historico.push("github.com/cxvinicius/projetos/estrutura-de-dados")

print(f"Páginas visitadas: {historico.items}")
print(f"Página atual: {historico.peek()}")

print("\n=== VOLTANDO (botão 'voltar' do navegador) ===")
print(f"Saindo de: {historico.pop()}")
print(f"Página atual agora: {historico.peek()}")

print(f"Saindo de: {historico.pop()}")
print(f"Página atual agora: {historico.peek()}")

print("\n=== VERIFICAÇÃO ===")
print(f"Histórico vazio: {historico.is_empty()}")
print(f"Páginas no histórico: {historico.size()}")

print(f"Saindo de: {historico.pop()}")
print(f"Saindo de: {historico.pop()}")

print(f"Páginas no histórico: {historico.size()}")
print(f"Histórico vazio: {historico.is_empty()}")
