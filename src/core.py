import sqlite3
import pandas as pd
class Lista:
    def __init__(self):

        self._conexao = sqlite3.connect("bb_tarefas.db")

        self._cursor = self._conexao.cursor()

        self._cursor.execute("CREATE TABLE IF NOT EXISTS Tarefas(id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT NOT NULL)")

        self._conexao.commit()


    def menu_tarefas(self):
        while True:
            df = pd.read_sql_query("SELECT id, descricao FROM Tarefas", self._conexao)
            print(df)
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
                    if qual_id == "0":
                        break
                    try:
                        qual_id_int = int(qual_id)
                        if qual_id_int < 0:
                            print("[ALERT] Id precisa ser positivo!")
                            continue
                    except ValueError as v:
                        print(f"[ERROR] Digite um id válido (Inteiro maior que zero): {v}")
                        continue

                    self._cursor.execute("SELECT id FROM Tarefas WHERE id = ?", (qual_id_int,))

                    tarefa_encontrada = self._cursor.fetchone()
                    if tarefa_encontrada:
                        p_qual = input("O que deseja escrever sobre ela? | Menu [0]: ")

                        if p_qual == "0":
                            break

                        self._cursor.execute("UPDATE Tarefas SET descricao = ? WHERE id = ?", (p_qual, qual_id_int) )
                        self._conexao.commit()

                        print("Tarefa atualizada!")
                        break

                    else:
                        print(f"[ERROR] ID não encontrado: '{qual_id_int}'")



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
        pergunta = input("Tarefas[1] | Sair[0] | : ")

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