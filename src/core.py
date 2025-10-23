class Lista:
    def __init__(self):
        self._lista_tarefas = []

    def menu_tarefas(self):
        while True:
            print(self._lista_tarefas)
            decisao = input("\nAdicionar tarefa [1] | Editar [2] | sair [0]: ")
            if decisao == "0":
                break
            if decisao == "1":
                while True:
                    nova_tarefa = input("Escreva a nova tarefa | Menu [0]: ")
                    if nova_tarefa == "0":
                        break
                    self._lista_tarefas.append(nova_tarefa)
            elif decisao == "2":
                while True:
                    qual = input("Qual tarefa? | Menu [0]: : ")
                    if qual == "0":
                        break
                    if qual in self._lista_tarefas:
                        p_qual = input("O que deseja escrever sobre ela? | Menu [0]: ")
                        if p_qual == "0":
                            break
                        self._lista_tarefas[self._lista_tarefas.index(qual)] = p_qual
                    else:
                        print(f"[ERROR] A tarefa escolhida não existe!: '{qual}'")
                        continue



class Seguranca:
    def __init__(self, name_str, key_str):
        self.nome = name_str
        self.key = key_str

    def testar(self):
        if self.nome != "eu" and self.key != "eu":
            return False
        return True





def iniciar():
    motor = Lista()
    lista_opcoes = ["0", "1", "2"]

    print("O que deseja fazer?\n")
    while True:
        pergunta = input("Tarefas[1] | Menu[2] | Sair[0] | : ")

        if pergunta not in lista_opcoes:
            print("[ERROR] Digite uma opção valida!")
            continue
        if pergunta == "0":
            print("Saindo...")
            break
        if pergunta == "1":
            motor.menu_tarefas()

def login():
    while True:
        usuario = input("Digite o nome do usuario: ")
        senha = input("Digite sua senha: ")

        seguranca = Seguranca(usuario, senha)

        resultado = seguranca.testar()
        if resultado:
            print("Bem-Vindo!")
            iniciar()
            break
        else:
            print("[ERROR] Usuário ou Senha incorretos.")
            continue