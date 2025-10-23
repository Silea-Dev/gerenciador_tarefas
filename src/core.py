import sqlite3

class Lista:
    def __init__(self):

    # 1. Conectar ao banco (cria se não existir)
        self._conexao = sqlite3.connect("bb_tarefas.db")

    # 2. Pegar o cursor
        self._cursor = self._conexao.cursor()

    # 3. Executar o "CREATE TABLE IF NOT EXISTS ..."
        self._cursor.execute("CREATE TABLE IF NOT EXISTS Tarefas(id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT NOT NULL)")

    # 4. Salvar a criação da tabela
        self._conexao.commit()

    # O self._lista_tarefas = [] não é mais necessário aqui.

    def menu_tarefas(self):
        while True:
            self._cursor.execute("SELECT * FROM Tarefas")
            resultados = self._cursor.fetchall()
            print(resultados)
            decisao = input("\nAdicionar tarefa [1] | Editar [2] | sair [0]: ")
            if decisao == "0":
                break
            if decisao == "1":
                while True:
                    nova_tarefa = input("Escreva a nova tarefa | Menu [0]: ")
                    if nova_tarefa == "0":
                        break
                    self._cursor.execute("INSERT INTO Tarefas(descricao) VALUES(?)", (nova_tarefa,))
                    self._conexao.commit()
            elif decisao == "2":
                while True:
                    qual_id = input("Qual o ID da tarefa que deseja editar? | Menu [0]: ")
                    self._cursor.execute("SELECT id FROM Tarefas WHERE id = ?", (qual_id,))
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
        if self.nome == "eu" and self.key == "eu":
            return True
        return False





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