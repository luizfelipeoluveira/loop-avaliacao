avalicao_excelente = 0
avaliacao_bom = 0
avaliacao_ruim = 0
avaliacao_total = 0


while avaliacao_total < 50:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    if not nome  or not idade:
        print("Dados inseridos incorretamente, por favor tente novamente.")
        continue

    idade_1 = int(idade)
    if idade_1 < 0:
        print("Dados inseridos incorretamente, por favor tente novamente.")
        continue

    user_opiniao = int(input("Digite em número sua opinião:\n 1. Excelelente\n 2. Bom\n 3. Ruim\n "))

    match user_opiniao:
        case 1:
            print("Avaliação validada com sucesso")
            avalicao_excelente += 1
            avaliacao_total += 1
        case 2:
            print("Avaliação validada com sucesso")
            avaliacao_bom += 1
            avaliacao_total += 1
        case 3:
            print("Avalição validada com sucesso")
            avaliacao_ruim += 1
            avaliacao_total += 1

print(" Total de avaliações: {}\n Avaliações excelentes: {}\n Avaliações boas: {}\n Avaliações ruins: {}\n".format(avaliacao_total, avalicao_excelente, avaliacao_bom, avaliacao_ruim))
