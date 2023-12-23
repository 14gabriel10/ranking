import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class Sistema_Palpites():
  def __init__(self):
    # Janela Principal e respectivos Frames.
    self.__win  = None
    self.__tree = None
    self.__frm_nome  = self.__frm_palpites = None
    self.__frm_lista = self.__style        = None

    # Widgets '__frm_nome'
    self.__nome_lb       = self.__nome_in       = None
    self.__rodada_lb     = self.__rodada_in     = None
    self.__mandante1_lb  = self.__mandante1_in  = None
    self.__visitante1_lb = self.__visitante1_in = None
    self.__mandante2_lb  = self.__mandante2_in  = None
    self.__visitante2_lb = self.__visitante2_in = None
    self.__mandante3_lb  = self.__mandante3_in  = None
    self.__visitante3_lb = self.__visitante3_in = None
    self.__mandante4_lb  = self.__mandante4_in  = None
    self.__visitante4_lb = self.__visitante4_in = None

    # Widgets '__frm_palpites'
    self.__partida1_lb = self.__partida2_lb = None
    self.__partida3_lb = self.__partida4_lb = None
    self.__palpitar_bt = self.__listar_bt   = self.__excluir_bt = None

    # Banco de Dados.
    self.__con = self.__cur = None

    # Init Janela Principal.
    self.__init_tk_frames()
    self.__init_widgets_frm_nome()
    self.__init_widgets_frm_palpites()
    self.__init_tree()
    self.__init_widgets_janela_principal()
    self.__init_db()

  def __init_tk_frames(self)->None:
    self.__win = tkinter.Tk()
    self.__win.title("Sistema de Palpites")

    # Inicialização das variáveis.
    self.__frm_nome     = tkinter.Frame (self.__win)
    self.__frm_palpites = tkinter.Frame (self.__win)
    self.__frm_lista    = tkinter.Frame (self.__win)

    self.__frm_nome.pack     (padx=53, pady=10, fill=tkinter.BOTH)
    self.__frm_palpites.pack (padx=53, fill=tkinter.BOTH)
    self.__frm_lista.pack    (padx=10, pady=10, fill=tkinter.BOTH)

  def __init_widgets_frm_nome(self)->None:
    # Inicialização das variáveis de Label.
    self.__nome_lb   = tkinter.Label (self.__frm_nome, text='Nome:')
    self.__rodada_lb = tkinter.Label (self.__frm_nome, text='Rodada:')

    # Inicialização das variáveis de Input (Entry).
    self.__nome_in   = tkinter.Entry (self.__frm_nome)
    self.__rodada_in = tkinter.Entry (self.__frm_nome)

  def __init_widgets_frm_palpites(self)->None:
    # Inicialização Labels.
    self.__partida1_lb   = tkinter.Label (self.__frm_palpites, text='Palpite Jogo 1')
    self.__partida2_lb   = tkinter.Label (self.__frm_palpites, text='Palpite Jogo 2')
    self.__partida3_lb   = tkinter.Label (self.__frm_palpites, text='Palpite Jogo 3')
    self.__partida4_lb   = tkinter.Label (self.__frm_palpites, text='Palpite Jogo 4')
    self.__mandante1_lb  = tkinter.Label (self.__frm_palpites, text="Cruzeiro")
    self.__mandante2_lb  = tkinter.Label (self.__frm_palpites, text="Palmeiras")
    self.__mandante3_lb  = tkinter.Label (self.__frm_palpites, text="Fluminense")
    self.__mandante4_lb  = tkinter.Label (self.__frm_palpites, text="Gremio")
    self.__visitante1_lb = tkinter.Label (self.__frm_palpites, text='Vasco')
    self.__visitante2_lb = tkinter.Label (self.__frm_palpites, text='Flamengo')
    self.__visitante3_lb = tkinter.Label (self.__frm_palpites, text='Internacional')
    self.__visitante4_lb = tkinter.Label (self.__frm_palpites, text='Fortaleza')

    # Inicialização Entries.
    self.__mandante1_in  = tkinter.Entry (self.__frm_palpites)
    self.__mandante2_in  = tkinter.Entry (self.__frm_palpites)
    self.__mandante3_in  = tkinter.Entry (self.__frm_palpites)
    self.__mandante4_in  = tkinter.Entry (self.__frm_palpites)
    self.__visitante1_in = tkinter.Entry (self.__frm_palpites)
    self.__visitante2_in = tkinter.Entry (self.__frm_palpites)
    self.__visitante3_in = tkinter.Entry (self.__frm_palpites)
    self.__visitante4_in = tkinter.Entry (self.__frm_palpites)

    # Inicialização Buttons.
    self.__palpitar_bt = tkinter.Button(self.__frm_palpites, text="Salvar Palpites",
                                        command=self.__palpitar, bg='darkgrey')
    self.__listar_bt = tkinter.Button(self.__frm_palpites, text="Ver Palpites",
                                      command=self.__visualizar_palpites, bg='darkgrey')
    self.__excluir_bt = tkinter.Button(self.__frm_palpites, text="Excluir Palpites",
                                       command=self.__excluir_palpites, bg='darkgrey')

  def __init_tree(self)->None:
    self.__tree = \
      ttk.Treeview(self.__frm_lista, columns=('ID', 'Nome', 'Rodada', 'Partida 1',
                                              'Partida 2', 'Partida 3', 'Partida 4'))
    self.__style = ttk.Style()
    self.__style.configure("Treeview", rowheight=30) 

    self.__tree.heading ("#0", text='ID',     anchor=tkinter.CENTER)
    self.__tree.heading ("#1", text='Nome',   anchor=tkinter.CENTER)
    self.__tree.heading ("#2", text='Rodada', anchor=tkinter.CENTER)
    self.__tree.heading ("#3", text='Jogo 1', anchor=tkinter.CENTER)
    self.__tree.heading ("#4", text='Jogo 2', anchor=tkinter.CENTER)
    self.__tree.heading ("#5", text='Jogo 3', anchor=tkinter.CENTER)
    self.__tree.heading ("#6", text='Jogo 4', anchor=tkinter.CENTER)

    self.__tree.column ("#0", width=50,  anchor=tkinter.CENTER)
    self.__tree.column ("#1", width=180, anchor=tkinter.CENTER)
    self.__tree.column ("#2", width=100, anchor=tkinter.CENTER)
    self.__tree.column ("#3", width=180, anchor=tkinter.CENTER)
    self.__tree.column ("#4", width=150, anchor=tkinter.CENTER)
    self.__tree.column ("#5", width=150, anchor=tkinter.CENTER)
    self.__tree.column ("#6", width=150, anchor=tkinter.CENTER)


  def __init_widgets_janela_principal(self)->None:
    self.__nome_lb.grid       (row=0, column=0, padx=5, pady=10)
    self.__nome_in.grid       (row=0, column=1, padx=5)
    self.__rodada_lb.grid     (row=0, column=3, padx=5, pady=10)
    self.__rodada_in.grid     (row=0, column=4, padx=5)
    self.__partida1_lb.grid   (row=2, column=1, padx=10)
    self.__partida2_lb.grid   (row=2, column=4, padx=10)
    self.__partida3_lb.grid   (row=2, column=6, padx=10)
    self.__partida4_lb.grid   (row=2, column=8, padx=10)
    self.__mandante1_lb.grid  (row=3, column=0)
    self.__mandante1_in.grid  (row=3, column=1, padx=10)
    self.__visitante1_lb.grid (row=4, column=0)
    self.__visitante1_in.grid (row=4, column=1, padx=10)
    self.__mandante2_lb.grid  (row=3, column=3)
    self.__mandante2_in.grid  (row=3, column=4, padx=10)
    self.__visitante2_lb.grid (row=4, column=3)
    self.__visitante2_in.grid (row=4, column=4, padx=10)
    self.__mandante3_lb.grid  (row=3, column=5)
    self.__mandante3_in.grid  (row=3, column=6, padx=10)
    self.__visitante3_lb.grid (row=4, column=5)
    self.__visitante3_in.grid (row=4, column=6, padx=10)
    self.__mandante4_lb.grid  (row=3, column=7)
    self.__mandante4_in.grid  (row=3, column=8, padx=10)
    self.__visitante4_lb.grid (row=4, column=7)
    self.__visitante4_in.grid (row=4, column=8, padx=10)
    self.__palpitar_bt.grid   (row=5, column=4, pady=25, columnspan=3)
    self.__listar_bt.grid     (row=6, column=3, pady=25, columnspan=3)
    self.__excluir_bt.grid    (row=6, column=5, pady=25, columnspan=3)
    self.__tree.pack()

  def __init_db(self)->None:
    self.__con = sqlite3.connect('palpites.db')
    self.__cur = self.__con.cursor()

  def __criar_tabela(self)->None:
    self.__cur.execute ('''
      CREATE TABLE IF NOT EXISTS palpite (
        palpite_id INTEGER PRIMARY KEY AUTOINCREMENT,          
        nome       VARCHAR (40) NOT NULL,    
        rodada     INTEGER NOT NUll,     
        partida1   TEXT NOT NULL,          
        partida2   TEXT NOT NULL,
        partida3   TEXT NOT NULL,
        partida4   TEXT NOT NULL               
      )
    ''')
    self.__con.commit()

  def __visualizar_palpites(self)->None:
    self.__cur.execute('SELECT * FROM palpite') 
    palpites = self.__cur.fetchall()

    for linha in self.__tree.get_children(): self.__tree.delete(linha)
    for palpite in palpites: self.__tree.insert('', 'end', values=palpite)

  def __palpitar(self)->None:
    nome   = self.__nome_in.get()
    rodada = self.__rodada_in.get()

    partida1 = "%s x %s" % (self.__mandante1_in.get(), self.__visitante1_in.get())
    partida2 = "%s x %s" % (self.__mandante2_in.get(), self.__visitante2_in.get())
    partida3 = "%s x %s" % (self.__mandante3_in.get(), self.__visitante3_in.get())
    partida4 = "%s x %s" % (self.__mandante4_in.get(), self.__visitante4_in.get())

    # TODO: Estudar a condição desse if para verificar se dados foram
    #       preenchidos da maneira correta, especificamente as condições:
    #       partida1 and partida2 and partida3 and partida4.

    if nome and rodada and partida1 and partida2 and partida3 and partida4:
      self.__cur.execute('''
        INSERT INTO palpite (nome, rodada, partida1, partida2, partida3, partida4)
        VALUES (?,?,?,?,?,?)
      ''', (nome, rodada, partida1, partida2, partida3, partida4))
      self.__con.commit()
      self.__visualizar_palpites()
      messagebox.showinfo('Info', 'Palpite feito com sucesso!')
    else:
      messagebox.showwarning('Aviso', 'Preencha todos os dados para prosseguir.')

  def __excluir_palpites(self)->None:
    palpite_selecionado = self.__tree.selection()
    if palpite_selecionado:
      if messagebox.askyesno('Confirmação', 'Confirmar exclsão do palpite?'):
        for palpite in palpite_selecionado:
          self.__cur.execute('''
            DELETE FROM palpite WHERE palpite_id=?
          ''', (self.__tree.item(palpite, 'values')[0],))
        self.__con.commit()
        self.__visualizar_palpites()
    else: messagebox.showwarning('Aviso', 'Selecione palpite a excluir.')

  def __limpar_campos(self)->None:
    self.__nome_in.delete       (0, 'end')
    slef.__rodada_in.delete     (0, 'end')
    self.__mandante1_in.delete  (0, 'end')
    self.__mandante2_in.delete  (0, 'end')
    self.__mandante3_in.delete  (0, 'end')
    self.__mandante4_in.delete  (0, 'end')
    self.__visitante1_in.delete (0, 'end')
    self.__visitante2_in.delete (0, 'end')
    self.__visitante3_in.delete (0, 'end')
    self.__visitante4_in.delete (0, 'end')

  def runtime(self)->None:
    self.__win.geometry("1366x780")
    self.__criar_tabela()
    self.__win.mainloop()    
    self.__con.close()

def main()->None:
  sis = Sistema_Palpites()
  sis.runtime()
  exit(0)

if __name__ == '__main__':
  main()
