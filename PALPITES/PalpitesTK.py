import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def criar_banco():
    conexao = sqlite3.connect("palpitesTK.db")
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
        jogo_4 TEXT NOT NULL,
        jogo_5 TEXT NOT NULL
                    
    )
       ''')
    
    conexao.commit()
    conexao.close()

def fazer_palpite():
    nome=nome_entry.get()
    jogo1=jogo1_entry.get()
    jogo2=jogo2_entry.get()
    jogo3=jogo3_entry.get()
    jogo4=jogo4_entry.get()
    jogo5=jogo5_entry.get()

    if nome and jogo1 and jogo2 and jogo3 and jogo4 and jogo5:
        conexao = sqlite3.connect("palpitesTK.db")
        cursor = conexao.cursor()
        cursor.execute('SELECT nome FROM palpite')
        palpites=cursor.fetchall()

        cursor.execute('INSERT INTO palpite (nome, jog_1, jogo_2, jogo_3, jogo_4, jogo_5) VALUES (?, ?, ?, ?, ?)', (nome, jogo1, jogo2, jogo3, jogo4, jogo5))
        conexao.commit()
        conexao.close()

        visualizar_palpites()
        excluir_palpite()

    else:
        messagebox.showwarning("Aviso","Preencha seu nome e os todos palpites!")

def visualizar_palpites():
    conexao = sqlite3.connect("palpites.db")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM palpite') 
    palpites= cursor.fetchall() 
    