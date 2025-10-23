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

                    # 1. Checar saída
                    if qual_id == "0":
                        break

                    # 2. Tentar encontrar o ID no banco (como você fez)
                    self._cursor.execute("SELECT id FROM Tarefas WHERE id = ?", (qual_id,))

                    # 3. Puxar o resultado para o Python (O PASSO QUE FALTA)
                    tarefa_encontrada = self._cursor.fetchone()
                    # (fetchone() retorna a tupla (id,) se achar, ou None se não achar)

                    # 4. A NOVA VALIDAÇÃO (Substitui o "if qual in ...")
                    if tarefa_encontrada:  # (Se "tarefa_encontrada" não for None)
                        # 4a. O ID EXISTE. Agora sim, peça o novo texto
                        p_qual = input("O que deseja escrever sobre ela? | Menu [0]: ")

                        if p_qual == "0":
                            break  # (Sai do loop de edição)

                        # 4b. Aplicar o UPDATE (O NOVO COMANDO SQL)
                        # (Substitui a linha do .index())
                        # self._cursor.execute("UPDATE Tarefas SET descricao = ? WHERE id = ?", (p_qual, qual_id))

                        # 4c. Salvar a mudança (O COMMIT)
                        # self._conexao.commit()

                        # (Opcional, mas bom: print("Tarefa atualizada!") e dê um 'break' para voltar ao menu)

                    else:  # (Se "tarefa_encontrada" for None)
                        # 5. O ID NÃO EXISTE. Avise o usuário.
                        print(f"[ERROR] ID não encontrado: '{qual_id}'")
                        # (O 'continue' é automático aqui)



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