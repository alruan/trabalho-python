vet = []
vazar = 0

while vazar != 1:
    print("------------------------------------------------------------------------")
    print("\t Agenda Telefônica \t")
    print("1 - Listar contatos")
    print("2 - Inserir contato")
    print("3 - Buscar contato")
    print("4 - Alterar contato")
    print("5 - Remover contato")
    print("6 - Salvar em arquivo")
    print("7 - Sair")

    dig = input("Digite a opção desejada: ")

    if dig == "1":
        if len(vet) == 0:
            print("A agenda está vazia.")
        else:
            print("----------")
            print("Contatos:")
            for var in vet:
                print(f'Nome: {var[0]} \t Telefone: {var[1]}')

    elif dig == "2":
        print("----------------------------------------------------------")
        nick = input("Digite o nome do contato: ")
        tel = input("Digite o telefone do contato: ")
        var = [nick, tel]
        vet.append(var)
        print("O contato foi inserido dentro da lista telefônica com sucesso.")

    elif dig == "3":
        nick = input("Digite o nome do contato a ser procurado: ")
        encon = False
        for var in vet:
            if var[0] == nick:
                print("Contato encontrado:")
                print(f'Nome: {var[0]} \t Telefone: {var[1]}')
                encon = True
        if not encon:
            print("Contato não encontrado.")

    elif dig == "4":
        nick = input("Digite o nome do contato a ser alterado: ")
        encon = False
        for var in vet:
            if var[0] == nick:
                novo_nick = input("Digite o novo nome: ")
                novo_tel = input("Digite o novo telefone: ")
                var[0] = novo_nick
                var[1] = novo_tel
                print("O contato foi alterado com sucesso.")
                encon = True
        if not encon:
            print("Contato não encontrado.")

    elif dig == "5":
        nick = input("Digite o nome do contato a ser excluído da lista telefônica: ")
        encon = False
        var2 = 0
        while var2 < len(vet):
            if vet[var2][0] == nick:
                del vet[var2]
                print("Contato foi excluído com sucesso.")
                encon = True
                break
            else:
                var2 += 1
        if not encon:
            print("O contato não foi encontrado.")

    elif dig == "6":
        dig2 = input("Digite o nome do arquivo para salvar a agenda telefônica: ")
        arq = open(dig2, "w")
        for var in vet:
            l = var[0] + "," + var[1]
            print(l, file=arq)
        arq.close()
        print("A agenda foi salva no arquivo com sucesso.")

    elif dig == "7":
        print("Se retirando da agenda telefônica...")
        vazar = 1

    else:
        print("A opção escolhida é inválida. Digite novamente!")