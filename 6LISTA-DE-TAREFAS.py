# criar lista de tarefas
tarefas = []

#adicionar tarefa
def add_tarefa(tarefa):
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print("tarefa adicionada: ", tarefa)

# remover tarefa
def remove_tarefa(tarefa):
    for t in tarefas:
        if t["tarefa"] == tarefa:
            tarefas.remove(t)
            print("tarefa removida: ", tarefa)
            return
    print("tarefa não encontrada.")

# concluir tarefa
def concluir_tarefa(tarefa):
    for t in tarefas:
        if t["tarefa"] == tarefa:
            t["concluida"] = True
            print("\n-->tarefas concluida: ", tarefa)
            return
    print("tarefa não concluida.")

#exibir tarefas
def list_tarefas():
    if tarefas:
        print("\n---> lista de tarefas <---") 
        for t in tarefas:
            status = "concluida" if t["concluida"] else "pendente"
            print(f"{t['tarefa']} - ({status})")
    else:
        print("\n sem tarefas no momento.")

#limpar lista
def clear_list():
    tarefas.clear()
    print("todas as tarefas foram removidas.")

# selecionar
while True:
    print("\n---> gerenciador de tarefas <---")
    print(" 1-adicionar tarefa")
    print(" 2-concluir tarefa")
    print(" 3-remover tarefa")
    print(" 4-exibir tarefas")
    print(" 5-limpar lista de tarefas")
    print(" 0-sair")

    opção = input("\n digite a opção desejada ==> ")
    if opção == "0":
        print("\n...encerrando o gerenciador de tarefas")
        break

    elif opção == "1":
        tarefa_name = input("digite o nome da tarefa ==> ")
        add_tarefa(tarefa_name)  

    elif opção =="2":
        tarefa_name = input("digite o nome da tarefa que deseja concluir ==> ")
        concluir_tarefa(tarefa_name)

    elif opção =="3":
        tarefa_name = input("digite o nome da tarefa que gostaria de remover ==> ")
        remove_tarefa(tarefa_name)

    elif opção =="4":
        list_tarefas()

    elif opção =="5":
        clear_list()            
