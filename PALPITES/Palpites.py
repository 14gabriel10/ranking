import sqlite3 

def criar_tabela():  # Funçao para criar a tabela no banco de dados

    # Conecta-se ao DB (ou criar um se nao existir)
    conexao = sqlite3.connect("palpites.db")
    cursor = conexao.cursor()

    # Cria tabela de PALPITES
    cursor.execute ('''
                
    CREATE TABLE IF NOT EXISTS palpite (
        id INTEGER PRIMARY KEY,          
        nome TEXT NOT NULL,    
        rodada TEXT NOT NUll,     
        jogo1 TEXT NOT NULL,          
        jogo2 TEXT NOT NULL,
        jogo3 TEXT NOT NULL,
        jogo4 TEXT NOT NULL
    )
       ''')
    
    # Conmit para salvar as alteraçoes e fecha conexao
    conexao.commit()
    conexao.close()
#------------------------------------------------------------------------------------------------------------------------------------------
def fazer_palpite(nome,rodada,jogo1,jogo2,jogo3,jogo4):# Funçao para adicionar PALPITES
    conexao = sqlite3.connect("palpites.db") # Conecta-se ao banco de dados
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO palpite(nome, rodada, jogo1, jogo2, jogo3, jogo4)VALUES(?, ?, ?, ?, ?, ?)',(nome, rodada, jogo1, jogo2, jogo3, jogo4)) # Insere os dados na tabela

    conexao.commit()
    conexao.close()
#--------------------------------------------------------------------------------------------------------------------------------------------
def visualizar_palpite(): # Funçao para listar 
    conexao = sqlite3.connect("palpites.db") # Conecta-se ao banco de dados
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM palpite')# Execute uma consulta SQL 
    palpites= cursor.fetchall() # Recupera todos os registros de palpites
    conexao.close
    return palpites
#-----------------------------------------------------------------------------------------------------------------------------------------------
def excluir_palpite(palpite_id):# Funçao para excluir
    conexao = sqlite3.connect('palpites.db')
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM palpite WHERE id=?',(palpite_id,))

    conexao.commit()
    
    conexao.close
#----------------------------------------------------------------------------------------------------------------------------------------------
def main():
    print("=== Faça seu Palpite!===")
    while True:
        print("Escolha uma opçao:")
        print("1.Palpitar")
        print("2.Visualizar Palpites")
        print("3.Excluir Palpites")
        print("4.Sair")
        opcao = input("Opçao: ")

        if opcao == "1":
            nome = input("Nome: ")
            rodada=int(input("Numero Rodada: "))
            jogo1= input("Palpite Nº_1: ")
            jogo2= input("Palpite Nº_2: ")
            jogo3= input("Palpite Nº_3: ")
            jogo4= input("Palpite Nº_4: ")
            criar_tabela()
            fazer_palpite(nome,rodada,jogo1,jogo2,jogo3,jogo4)
            print("Palpites feitos com sucesso!")
        
        elif opcao == "2":
            palpite=visualizar_palpite()
            if not palpite:
                print("Nenhum palpite encontrado.")
            else:
                print("\t=== Lista de Palpites ===")
                for nome in palpite:
                    print(f"ID {nome [0]} __ Nome: | {nome [1]} | Nº Rodada: {nome[2]} || Palpite Nº1: {nome[3]} || Palpite Nº2: {nome [4]} || Palpite Nº3: {nome[5]} || Palpite Nº4: {nome[5]}.")
        
        elif opcao == "3":
            palpite_id = int(input("ID do palpite a ser excluído: "))
            excluir_palpite(palpite_id)
            print("Palpite excluido com sucesso!")

        elif opcao == "4":
            print("\tSaindo...")
        else:
            print("Opçao invalida.\nEscolha uma opçao de 1 a 5.\nTente novamente")

if __name__== "__main__":
    main()