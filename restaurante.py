import os
import time

# Função para limpar o terminal
def limpa_terminal():
    os.system("cls || clear")

# Função para exibir o cardápio
def exibir_cardapio():
    print("\nCardápio:")
    print("1 - Miojo - R$ 5.00")
    print("2 - Macarrão - R$ 10.00")
    print("3 - Hambúrguer - R$ 15.00")
    print("4 - Churros - R$ 20.00")
    print("5 - X Tudo - R$ 25.00")
    print("6 - Yakisoba - R$ 30.00")
    print("7 - Nuggets - R$ 35.00")
    print("Digite 0 para encerrar o pedido.\n")
    time.sleep(0.5)

# Função para calcular o valor total com base na forma de pagamento
def calcular_total(lista_pratos, forma_pagamento):
    precos = {1: 5.00, 2: 10.00, 3: 15.00, 4: 20.00, 5: 25.00, 6: 30.00, 7: 35.00}
    soma_total = 0 
    for prato in lista_pratos:
        preco_prato = precos[prato]
        soma_total += preco_prato
    
    match forma_pagamento:
        case 1:
            desconto = soma_total * 0.10
            total = soma_total - desconto
            
        case 2:
            acrescimo = soma_total * 0.10
            total = soma_total + acrescimo
    
    return subtotal, total


# Função principal para processar o pedido
def processar_pedido():
    lista_pratos = []
    
    while True:
        limpa_terminal()
        exibir_cardapio()
        
        numero = int(input("Digite a numeração do prato desejado: "))
        
        match numero:
            case 0:  # Encerrar pedido
                break
            case 1 | 2 | 3 | 4 | 5 | 6 | 7:  # Pratos válidos
                lista_pratos.append(numero)
                print("Prato adicionado com sucesso!")
                time.sleep(0.5)
            case _:  # Número inválido
                print("Número inválido! Tente novamente.")
                time.sleep(0.5)
        
        # Perguntar se o usuário deseja continuar pedindo
        continuar = input("Deseja adicionar outro prato? se sim digite s, se não 0: ").strip().lower()
        if continuar != 's':
            break
    
    # Solicitar a forma de pagamento
    print("\nFormas de pagamento:")
    print("1 - À vista (10% de desconto)")
    print("2 - Cartão de crédito (10% de acréscimo)")
    time.sleep(0.5)
    
    while True:
        forma_pagamento = entrada_inteiro("Escolha a forma de pagamento: ")
        
        match forma_pagamento:
            case 1 | 2:  # Opções válidas
                break
            case _:  # Opção inválida
                print("Opção inválida! Escolha 1 ou 2.")
                time.sleep(0.5)
    
    # Calcular total dentro do for each
    subtotal, total = calcular_total(lista_pratos, forma_pagamento)
    
    # Exibir os resultados
    print("\nResumo do pedido:")
    time.sleep(0.5)
    
    pratos_nomes = {1: "Lasanha", 2: "Pizza", 3: "Hambúrguer", 4: "Salada", 5: "Sopa", 6: "Filé Mignon", 7: "Frango Grelhado"}
    
    for prato in lista_pratos:
        print(f"Prato {prato}: {pratos_nomes[prato]}")
        time.sleep(0.5)
    
    print(f"Subtotal: R$ {subtotal:.2f}")
    time.sleep(0.5)
    
    match forma_pagamento:
        case 1:
            print("Forma de pagamento: À vista")
        case 2:
            print("Forma de pagamento: Cartão de crédito")
    
    time.sleep(0.5)
    print(f"Total a pagar: R$ {total:.2f}")

# Executa o processamento do pedido
processar_pedido()