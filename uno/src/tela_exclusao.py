# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exclusao.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_tela_excluir(object):
    def excluir_jogador(self):
        con = sqlite3.connect("ranking.db")
        cur = con.cursor()
        cur.execute("""
          DELETE FROM tabela WHERE id=?
        """, (self.input_id.text(),))
        con.commit()
        con.close()

    def setupUi(self, tela_adicionar):
        tela_adicionar.setObjectName("tela_adicionar")
        tela_adicionar.resize(721, 571)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tela_adicionar.sizePolicy().hasHeightForWidth())
        tela_adicionar.setSizePolicy(sizePolicy)
        tela_adicionar.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(tela_adicionar)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 721, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../imagens/screen.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(190, 70, 341, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("border-radius:10px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_voltar = QtWidgets.QPushButton(self.frame)
        self.btn_voltar.setGeometry(QtCore.QRect(0, 10, 51, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_voltar.setFont(font)
        self.btn_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_voltar.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    \n"
"}\n"
"")
        self.btn_voltar.setObjectName("btn_voltar")
        self.btn_excluir = QtWidgets.QPushButton(self.frame)
        self.btn_excluir.setGeometry(QtCore.QRect(120, 380, 101, 31))
        self.btn_excluir.clicked.connect(self.excluir_jogador)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_excluir.setFont(font)
        self.btn_excluir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    border:1px solid white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.btn_excluir.setObjectName("btn_excluir")
        self.txt_exclusao = QtWidgets.QLabel(self.frame)
        self.txt_exclusao.setGeometry(QtCore.QRect(90, 230, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_exclusao.setFont(font)
        self.txt_exclusao.setStyleSheet("color: rgb(255, 255, 255);")
        self.txt_exclusao.setObjectName("txt_exclusao")
        self.input_id = QtWidgets.QLineEdit(self.frame)
        self.input_id.setGeometry(QtCore.QRect(120, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_id.setFont(font)
        self.input_id.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid red;\n"
"border-radius: 5px\n"
"}")
        self.input_id.setMaxLength(15)
        self.input_id.setObjectName("input_id")
        self.txt_id = QtWidgets.QLabel(self.frame)
        self.txt_id.setGeometry(QtCore.QRect(160, 300, 16, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_id.setFont(font)
        self.txt_id.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,5);")
        self.txt_id.setObjectName("txt_id")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 20, 231, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../imagens/uno1.png"))
        self.label_2.setObjectName("label_2")
        tela_adicionar.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_adicionar)
        QtCore.QMetaObject.connectSlotsByName(tela_adicionar)

    def retranslateUi(self, tela_adicionar):
        _translate = QtCore.QCoreApplication.translate
        tela_adicionar.setWindowTitle(_translate("tela_adicionar", "uno"))
        self.btn_voltar.setText(_translate("tela_adicionar", "🔙"))
        self.btn_excluir.setText(_translate("tela_adicionar", "Excluir"))
        self.txt_exclusao.setText(_translate("tela_adicionar", "Exclusão de jogador!"))
        self.txt_id.setText(_translate("tela_adicionar", "ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_adicionar = QtWidgets.QMainWindow()
    ui = Ui_tela_excluir()
    ui.setupUi(tela_adicionar)
    tela_adicionar.show()
    sys.exit(app.exec_())
