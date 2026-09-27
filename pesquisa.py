# Inicialização dos contadores de respostas
qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

# Definição do total de entrevistados
total_entrevistados = 50

print("=======================================")
print("   PESQUISA DE SATISFAÇÃO - TUDOWEB   ")
print("=======================================")

# Estrutura FOR: indicada quando sabemos a quantidade exata de repetições
for i in range(1, total_entrevistados + 1):
    print(f"\n--- Entrevistado {i} de {total_entrevistados} ---")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    # Exibição do menu
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = int(input("Digite a opção (1, 2 ou 3): "))
    
    # Estrutura WHILE com operador OR: repete enquanto a opção for inválida
    while opiniao < 1 or opiniao > 3:
        print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
        opiniao = int(input("Digite a opção (1, 2 ou 3): "))
    
    # Estrutura de decisão para contabilizar os resultados
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 2:
        qtd_bom += 1
    elif opiniao == 3:
        qtd_ruim += 1

# Exibição do relatório final
print("\n=======================================")
print("         RESULTADO DA PESQUISA         ")
print("=======================================")
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'BOM': {qtd_bom}")
print(f"c) Quantidade de respostas 'RUIM': {qtd_ruim}")
print("=======================================")