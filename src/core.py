import sqlite3
import pandas as pd

class Lista:
    def __init__(self):
        self._conexao = sqlite3.connect("bb_tarefas.db")
        self._cursor = self._conexao.cursor()
        self._cursor.execute("CREATE TABLE IF NOT EXISTS Tarefas(id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT NOT NULL, concluida INTEGER NOT NULL DEFAULT 0)")
        self._conexao.commit()


    def adicionar_tarefas(self):
        while True:
            nova_tarefa = input("Escreva a nova tarefa | Menu [0]: ")
            if nova_tarefa == "0":
                break
            self._cursor.execute("INSERT INTO Tarefas(descricao) VALUES(?)", (nova_tarefa,))
            self._conexao.commit()


    def editar_tarefas(self):
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

                self._cursor.execute("UPDATE Tarefas SET descricao = ? WHERE id = ?", (p_qual, qual_id_int))
                self._conexao.commit()

                print("Tarefa atualizada!")
                break

            else:
                print(f"[ERROR] ID não encontrado: '{qual_id_int}'")


    def concluir_tarefas(self):
        while True:
            conluida_str = input("Qual o ID da tarefa concluída ? | Menu [0]: ")

            if conluida_str == "0":
                break

            try:
                conluida_int = int(conluida_str)
                novo_status_str = input("Marcar como Concluída [1] ou Pendente [0]? ")
                novo_status_int = int(novo_status_str)

                if novo_status_int not in [0, 1]:
                    print("[ERROR] Tarefas concluídas devem ser marcadas com 1, e não concluídas com 0!")
                    continue

                if conluida_int < 0:
                    print("[ALERT] Id precisa ser positivo!")
                    continue

            except ValueError as v:
                print(f"[ERROR] Digite um id válido (Inteiro maior que zero): {v}")
                continue
            self._cursor.execute("SELECT id FROM Tarefas WHERE id = ?", (conluida_int,))
            tarefa_encontrada = self._cursor.fetchone()
            if tarefa_encontrada:
                self._cursor.execute("UPDATE Tarefas SET concluida = ? WHERE id = ?", (novo_status_int, conluida_int,))
                self._conexao.commit()
                print("Status atualizado!")


    def apagar_tarefas(self):
        while True:
            apagar_str = input("Qual o ID da tarefa apagada ? | Menu [0]: ")

            if apagar_str == "0":
                break

            try:
                apagar_int = int(apagar_str)
                if apagar_int < 0:
                    print("[ALERT] Id precisa ser positivo!")
                    continue
            except ValueError as v:
                print(f"[ERROR] Digite um id válido (Inteiro maior que zero): {v}")
                continue

            self._cursor.execute("SELECT id FROM Tarefas WHERE id = ?", (apagar_int,))
            tarefa_encontrada = self._cursor.fetchone()

            if tarefa_encontrada:
                confirma = input(f"Tem certeza que deseja apagar a tarefa ID {apagar_int}? [s/n]: ")
                if confirma.lower() == 's':
                    self._cursor.execute("DELETE FROM Tarefas WHERE id = ?", (apagar_int,))
                    self._conexao.commit()
                    print("Tarefa apagada!")
                else:
                    print("Operação cancelada.")
                break
            else:
                print(f"[ERROR] ID não encontrado: '{apagar_int}'")


    def consulta_tarefas(self):
        df = pd.read_sql_query("SELECT id, descricao, concluida FROM Tarefas", self._conexao)
        print(df)
        return df


    def menu_tarefas(self):
        while True:
            self.consulta_tarefas()
            decisao = input("\nAdicionar tarefa[1] | Editar[2] | Concluir[3] | Apagar[4] | Sair [0]: ")
            if decisao == "0":
                break
            if decisao == "1":
                self.adicionar_tarefas()
            elif decisao == "2":
                self.editar_tarefas()
            elif decisao == "3":
                self.concluir_tarefas()
            elif decisao == "4":
                self.apagar_tarefas()


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