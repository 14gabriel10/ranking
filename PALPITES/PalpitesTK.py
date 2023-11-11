import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def criar_banco():
    conexao = sqlite3.connect("palpites.db")
    cursor = conexao.cursor()

    # Cria tabela de PALPITES
    cursor.execute ('''
                
    CREATE TABLE IF NOT EXISTS palpite (
        id INTEGER PRIMARY KEY AUTOINCREMENT,          
        nome TEXT NOT NULL,    
        rodada TEXT NOT NUll,     
        jogo_1 TEXT NOT NULL,          
        jogo_2 TEXT NOT NULL,
        jogo_3 TEXT NOT NULL,
        jogo_4 TEXT NOT NULL               
    )
       ''')
    
    conexao.commit()
    conexao.close()

def fazer_palpite():
    nome = nome_entry.get()
    rodada = rodada_entry.get()

    time_casa1 = time_casa1_entry.get()
    time_visitante1 = time_visitante1_entry.get()
    jogo_1= (f'{time_casa1} x {time_visitante1}')

    time_casa2 = time_casa2_entry.get()
    time_visitante2 = time_visitante2_entry.get()
    jogo_2= (f'{time_casa2} x {time_visitante2}')

    time_casa3 = time_casa3_entry.get()
    time_visitante3 = time_visitante3_entry.get()
    jogo_3= (f'{time_casa3} x {time_visitante3}')

    time_casa4 = time_casa4_entry.get()
    time_visitante4 = time_visitante4_entry.get()
    jogo_4= (f'{time_casa4} x {time_visitante4}')

    
    if nome and rodada and jogo_1 and jogo_2 and jogo_3 and jogo_4:
        conexao = sqlite3.connect("palpites.db")
        cursor = conexao.cursor()
        cursor.execute('SELECT nome FROM palpite')
        palpites=cursor.fetchall()

        cursor.execute('INSERT INTO palpite (nome, rodada, jogo_1, jogo_2, jogo_3, jogo_4) VALUES (?, ?, ?, ?, ?, ?)', (nome, rodada, jogo_1, jogo_2, jogo_3, jogo_4))
        conexao.commit()
        conexao.close()

        visualizar_palpites()

        messagebox.showinfo('Info','Palpite feito com sucesso!')

    else:
        messagebox.showwarning("Aviso","Preencha seu nome e os todos palpites!")

def visualizar_palpites():
    conexao = sqlite3.connect("palpites.db")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM palpite') 
    rows= cursor.fetchall()
    conexao.close()

    for row in tree.get_children():
        tree.delete(row)

    # Insere os palpites na tela
    for row in rows:
        tree.insert('', 'end', values=row)

def excluir_palpites():
    selected_palpite = tree.selection()
    excluir = messagebox.askyesno('Confirmação', "Tem certeza que deseja excluir esse palpite?")

    if selected_palpite:
        if excluir:
            conexao = sqlite3.connect('palpites.db')
            cursor = conexao.cursor()
            for palpites in selected_palpite:
                cursor.execute('DELETE FROM palpite WHERE id = ?', (tree.item(palpites, 'values')[0],))
            conexao.commit()

            # Fecha a conexão com o banco
            conexao.close()

            # Atualiza a lista de palpites
            visualizar_palpites()
        else:
            pass
    else:
        # Mostra um aviso
        messagebox.showwarning("Aviso", "Selecione um palpite para excluir.")


def limpar_campos():
    nome_entry.delete(0,'end')
    rodada_entry.delete(0,'end')

    time_casa1_entry.delete(0,'end')
    time_visitante1_entry.delete(0,'end')

    time_casa2_entry.delete(0,'end')
    time_visitante2_entry.delete(0,'end')
    
    time_casa3_entry.delete(0,'end')
    time_visitante3_entry.delete(0,'end')

    time_casa4_entry.delete(0,'end')
    time_visitante4_entry.delete(0,'end')

# janela principal
window = tk.Tk()
window.title("Placares DS")
criar_banco()

frame_nome=tk.Frame(window)
frame_nome.pack(padx=53,pady=10,fill=tk.BOTH)
# NOME E RODADA
nome_label=tk.Label(frame_nome, text='Nome:')
nome_label.grid(row=0,column=0,padx=5,pady=10)
nome_entry=tk.Entry(frame_nome)
nome_entry.grid(row=0,column=1,padx=5)
rodada_label=tk.Label(frame_nome, text='Rodada:')
rodada_label.grid(row=0,column=3,padx=5,pady=10)
rodada_entry=tk.Entry(frame_nome)
rodada_entry.grid(row=0,column=4,padx=5)

# FRAME PALPITES JOGOS
frame_palpites=tk.Frame(window)
frame_palpites.pack(padx=53,fill=tk.BOTH)
jogo1_label=tk.Label(frame_palpites,text='Palpite Jogo 1')
jogo1_label.grid(row=2,column=1,padx=10)

jogo2_label=tk.Label(frame_palpites,text='Palpite Jogo 2')
jogo2_label.grid(row=2,column=4,padx=10)

jogo3_label=tk.Label(frame_palpites,text='Palpite Jogo 3')
jogo3_label.grid(row=2,column=6,padx=10)

jogo4_label=tk.Label(frame_palpites,text='Palpite Jogo 4')
jogo4_label.grid(row=2,column=8,padx=10)

# JOGO 1
time_casa1_label=tk.Label(frame_palpites,text="Cruzeiro")
time_casa1_label.grid(row=3,column=0)
time_casa1_entry=tk.Entry(frame_palpites)
time_casa1_entry.grid(row=3,column=1,padx=10)
time_visitante1_label=tk.Label(frame_palpites,text='Vasco')
time_visitante1_label.grid(row=4,column=0)
time_visitante1_entry=tk.Entry(frame_palpites)
time_visitante1_entry.grid(row=4,column=1,padx=10)

# JOGO 2
time_casa2_label=tk.Label(frame_palpites,text="Palmeiras")
time_casa2_label.grid(row=3,column=3)
time_casa2_entry=tk.Entry(frame_palpites)
time_casa2_entry.grid(row=3,column=4,padx=10)
time_visitante2_label=tk.Label(frame_palpites,text='Flamengo')
time_visitante2_label.grid(row=4,column=3)
time_visitante2_entry=tk.Entry(frame_palpites)
time_visitante2_entry.grid(row=4,column=4,padx=10)

# JOGO 3
time_casa3_label=tk.Label(frame_palpites,text="Fluminense")
time_casa3_label.grid(row=3,column=5)
time_casa3_entry=tk.Entry(frame_palpites)
time_casa3_entry.grid(row=3,column=6,padx=10)
time_visitante3_label=tk.Label(frame_palpites,text='Internacional')
time_visitante3_label.grid(row=4,column=5)
time_visitante3_entry=tk.Entry(frame_palpites)
time_visitante3_entry.grid(row=4,column=6,padx=10)

# JOGO 4
time_casa4_label=tk.Label(frame_palpites,text="Gremio")
time_casa4_label.grid(row=3,column=7)
time_casa4_entry=tk.Entry(frame_palpites)
time_casa4_entry.grid(row=3,column=8,padx=10)
time_visitante4_label=tk.Label(frame_palpites,text='Fortaleza')
time_visitante4_label.grid(row=4,column=7)
time_visitante4_entry=tk.Entry(frame_palpites)
time_visitante4_entry.grid(row=4,column=8,padx=10)

palpitar_button = tk.Button(frame_palpites, text="| ​​​​​✔️​ |​ Salvar Palpites", command=fazer_palpite, bg='lightgrey', fg='black')
palpitar_button.grid(row=5, column=4, pady=25,columnspan=3)

listar_button = tk.Button(frame_palpites, text="| ​​​​​✔️​ |​ Ver Palpites", command=visualizar_palpites, bg='lightgrey', fg='black')
listar_button.grid(row=6, column=3, pady=25,columnspan=3)

excluir_button = tk.Button(frame_palpites, text="| ​​​​​✔️​ |​ Excluir Palpites", command=excluir_palpites, bg='lightgrey', fg='black')
excluir_button.grid(row=6, column=5, pady=25,columnspan=3)

frame_lista = tk.Frame(window)

# Frame Lista
frame_lista.pack(padx=10, pady=10, fill=tk.BOTH)
tree = ttk.Treeview(frame_lista, columns=('ID', 'Nome', 'Rodada', 'Jogo 1', 'Jogo 2', 'Jogo 3', 'Jogo 4'))

# Define o Título
tree.heading("#1", text="ID",anchor=tk.CENTER)
tree.heading("#2", text="Nome",anchor=tk.CENTER)
tree.heading("#3", text="Rodada",anchor=tk.CENTER)
tree.heading("#4", text="Jogo 1",anchor=tk.CENTER)
tree.heading("#5", text="Jogo 2",anchor=tk.CENTER)
tree.heading("#6", text="Jogo 3",anchor=tk.CENTER)
tree.heading("#7", text="Jogo 4",anchor=tk.CENTER)

# Define a largura da coluna        
tree.column("#1", width=50,anchor=tk.CENTER)
tree.column("#2", width=180,anchor=tk.CENTER)
tree.column("#3", width=100,anchor=tk.CENTER)
tree.column("#4", width=180,anchor=tk.CENTER)
tree.column("#5", width=150,anchor=tk.CENTER)
tree.column("#6", width=150,anchor=tk.CENTER)
tree.column("#7", width=150,anchor=tk.CENTER)

# Mostrar a árvore na tela
tree.pack()
style = ttk.Style()
style.configure("Treeview", rowheight=30) 

# Configuração da interface
window.geometry("1366x780")
window.mainloop()    
