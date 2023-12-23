from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from tela_acesso import Ui_tela_inicial_2
from tela_menu import Ui_MainWindow
from tela_add import Ui_tela_adicionar
from tela_atualizar import Ui_tela_atualizar
from tela_exclusao import Ui_tela_excluir
import sys
import sqlite3

class UnoApp(QtWidgets.QMainWindow, Ui_tela_inicial_2):
  def __init__(self) -> None:
    super(UnoApp, self).__init__()
    self.setupUi(self)
    self.setWindowTitle("Uno/TDS-2023")
    self.con = sqlite3.connect("ranking.db")
    self.cur = self.con.cursor()
    self.criar_tabela()

    self.btn_acesso.clicked.connect(self.abrir_menu)

  def abrir_menu(self):
    self.w = MenuPrincipal()
    self.w.show()
    self.centralizar_janela(self.w)
    self.close()

  def centralizar_janela(self, window):
    screen_geometry = QDesktopWidget().screenGeometry()
    window_geometry = window.frameGeometry()
    window_geometry.moveCenter(screen_geometry.center())
    window.move(window_geometry.topLeft())

  def criar_tabela(self):  
    self.cur.execute('''
      CREATE TABLE IF NOT EXISTS tabela (  
        id INTEGER PRIMARY KEY AUTOINCREMENT,               
        nome VARCHAR (40) NOT NULL,                        
        pontos INTEGER NOT NULL           
      )
    ''')
    self.con.commit()

class MenuPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self) -> None:
    super(MenuPrincipal, self).__init__()
    self.setupUi(self)
    self.setWindowTitle("Uno/Menu")

    self.btn_adicionar.clicked.connect(self.adicionar_jogador)
    self.btn_atualizar.clicked.connect(self.atualizar_pontuacao)
    self.btn_excluir.clicked.connect(self.excluir)

  def adicionar_jogador(self):
    self.w = TelaAdicionar()
    self.w.show()
    self.centralizar_janela(self.w)
    self.close()

  def atualizar_pontuacao(self):
    self.w = TelaAtualizar()
    self.w.show()
    self.centralizar_janela(self.w)
    self.close()

  def excluir(self):
    self.w = TelaExcluir()
    self.w.show()
    self.centralizar_janela(self.w)
    self.close()

  def centralizar_janela(self, window):
    screen_geometry = QDesktopWidget().screenGeometry()
    window_geometry = window.frameGeometry()
    window_geometry.moveCenter(screen_geometry.center())
    window.move(window_geometry.topLeft())

class TelaAdicionar(QtWidgets.QMainWindow, Ui_tela_adicionar):
  def __init__(self):
    super(TelaAdicionar, self).__init__()
    self.setupUi(self)
    self.setWindowTitle("Uno/Menu/Adicionar Jogador")

    self.btn_fechar.clicked.connect(self.abrir_menu)

  def abrir_menu(self):
    self.w = MenuPrincipal()
    self.w.show()
    self.centralizar_janela(self.w)
    self.close()

  def centralizar_janela(self, window):
    screen_geometry = QDesktopWidget().screenGeometry()
    window_geometry = window.frameGeometry()
    window_geometry.moveCenter(screen_geometry.center())
    window.move(window_geometry.topLeft())

class TelaAtualizar(QtWidgets.QMainWindow, Ui_tela_atualizar):
  def __init__(self):
    super(TelaAtualizar, self).__init__()
    self.setupUi(self)
    self.setWindowTitle("Uno/Menu/Atualizar Pontuações")

    self.btn_back.clicked.connect(self.abrir_menu)

  def abrir_menu(self):
    self.w = MenuPrincipal()
    self.w.show()
    self.centralizar_janela(self.w)
    self.close()

  def centralizar_janela(self, window):
    screen_geometry = QDesktopWidget().screenGeometry()
    window_geometry = window.frameGeometry()
    window_geometry.moveCenter(screen_geometry.center())
    window.move(window_geometry.topLeft())


class TelaExcluir(QtWidgets.QMainWindow, Ui_tela_excluir):
  def __init__(self):
    super(TelaExcluir, self).__init__()
    self.setupUi(self)
    self.setWindowTitle("Uno/Menu/Excluir Jogador")

    self.btn_voltar.clicked.connect(self.abrir_menu)

  def abrir_menu(self):
    self.w = MenuPrincipal()
    self.w.show()
    self.centralizar_janela(self.w)
    self.close()

  def centralizar_janela(self, window):
    screen_geometry = QDesktopWidget().screenGeometry()
    window_geometry = window.frameGeometry()
    window_geometry.moveCenter(screen_geometry.center())
    window.move(window_geometry.topLeft())

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  uno_app = UnoApp()
  uno_app.show()
  sys.exit(app.exec_())
