import sqlite3 

def criar_tabela():  
    conexao = sqlite3.connect("ranking.db")
    cursor = conexao.cursor()

    cursor.execute ('''
    CREATE TABLE IF NOT EXISTS classificacao (  
        id INTEGER PRIMARY KEY,                     
        nome TEXT NOT NULL,                        
        pontuacao INTEGER NOT NULL           
    )
       ''')
    
    conexao.commit()
    conexao.close()
#--------------------------------------------------------------------------------------------------------
def adicionar_nome(nome,pontuacao):
    conexao = sqlite3.connect("ranking.db") 
    cursor = conexao.cursor()

    cursor.execute('INSERT INTO classificacao(nome, pontuacao)VALUES(?, ?)',(nome, pontuacao)) 
    conexao.commit()
    conexao.close()

#---------------------------------------------------------------------------------------------------------

def listar_ranking(): 
    conexao = sqlite3.connect("ranking.db") 
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM classificacao ORDER BY pontuacao DESC')
    classificacao= cursor.fetchall() 
    conexao.close
    return classificacao # retonar lista 

#---------------------------------------------------------------------------------------------------------

def atualizar_ranking(palpite_id, nova_pontuacao):
    conexao = sqlite3.connect('ranking.db')
    cursor = conexao.cursor()

    cursor.execute('UPDATE classificacao SET pontuacao=? WHERE id=?',(nova_pontuacao, palpite_id))
    conexao.commit()
    conexao.close()

#----------------------------------------------------------------------------------------------------------
def excluir_id(palpite_id):# Funçao para excluir com base no ID
    conexao = sqlite3.connect('ranking.db')
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM classificacao WHERE id=?',(palpite_id,))

    conexao.commit()
    conexao.close
#----------------------------------------------------------------------------------------------------------
def main():
    print("=== Ranking===")
    while True:
        print("Escolha uma opçao")
        print("1.Adicionar nome no Ranking ")
        print("2.Ver Ranking ")
        print("3.Atualizar Pontuaçoes ")
        print("4.Excluir ID  ")
        print("5.Sair")
        opcao = input("Opçao: ")

        if opcao == "1":
            nome = input("Insira seu nome: ")
            pontuacao = int(input("Pontuaçao: "))
            criar_tabela() 
            adicionar_nome(nome, pontuacao)
            print("Você está no ranking !")
        #-------------------------------------------------------------------------
        elif opcao == "2":
            ver_ranking=listar_ranking()
            if not ver_ranking:
                print("Nenhum nome cadastrado.")
            else:
                print("=== Ranking ===")
                for nome in ver_ranking:
                    print(f"ID__ {nome [0]}| {nome [1]} || Pontos: {nome [2]}")
        #--------------------------------------------------------------------------
        elif opcao == "3":
            pontuacao_id = int(input("ID a ser atualizado: "))

            nova_pontuacao=int(input("Nova pontuacao: "))
            atualizar_ranking(pontuacao_id,nova_pontuacao)
            print("Pontuaçao atualizada com sucesso!")
        #----------------------------------------------------------------------------
        elif opcao == "4":
            pontuacao_id = int(input("ID a ser excluído: "))
            excluir_id(pontuacao_id)
            print("Nome excluido com sucesso!")
        #---------------------------------------------------------------------------
        elif opcao == "5":
            print("")
        else:
            print("Opçao invalida.\nEscolha uma opçao de 1 a 5.\nTente novamente")

if __name__== "__main__":
    main()
            




