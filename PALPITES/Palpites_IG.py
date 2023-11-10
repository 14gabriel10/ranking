import PySimpleGUI as sg
import sqlite3

class PalpitesDS:
    def __init__(self):

        sg.theme("DefaultNoMoreNagging")

        layout = [
            [sg.Text("Palpites D.S", font=("Algerian", 35))],
            [sg.Text("\tFaça seus palpites!\n",font=("Algerian",12))],
            [sg.Text("Nome: ",font=("Verdana",9)), sg.InputText(key="nome_jogador",font=("Verdana",9))],
            [sg.Text("\n|| Jogo 1 ||- Faça seu palpite:\n",font=("Verdana",9)),sg.InputText(key="palpite_1",font=("Verdana",9))],
            [sg.Text("\n|| Jogo 2 ||- Faça seu palpite:\n",font=("Verdana",9)),sg.InputText(key="palpite_2",font=("Verdana",9))],
            [sg.Text("\n|| Jogo 3 ||- Faça seu palpite:\n",font=("Verdana",9)),sg.InputText(key="palpite_3",font=("Verdana",9))],
            [sg.Text("\n|| Jogo 4 ||- Faça seu palpite:\n",font=("Verdana",9)),sg.InputText(key="palpite_4",font=("Verdana",9))],
            [sg.Text("\n|| Jogo 5 ||- Faça seu palpite:\n",font=("Verdana",9)),sg.InputText(key="palpite_5",font=("Verdana",9))],
            [sg.Button("Palpitar",font=("Verdana",13)),sg.Button('Cancelar',font=('Verdana',13))],
            [sg.Text("", size=(10,5), key="cupomLabel",font=("Verdana",10))]
        ]

        self.window = sg.Window("Curso/Tec.Desenvolvimento de Sistemas", layout)
    

    def iniciarAposta(self):
        nome = self.window["nome_jogador"].get()
        jogo1 = self.window["palpite_1"].get()
        jogo2 = self.window["palpite_2"].get()
        jogo3 = self.window["palpite_3"].get()
        jogo4 = self.window["palpite_4"].get()
        jogo5 = self.window["palpite_5"].get()
        

        if not nome:
            sg.popup_error('Atenção', 'Insira seu nome!',font=("Verdana",10))
            return
        if not jogo1:
            sg.popup_error('Atençao', f"Faça seu palpite, {nome}.",font=("Verdana",10))
            return
        if not jogo2:
            sg.popup_error('Atençao', f"Faça seu palpite, {nome}.",font=("Verdana",10))
            return
        if not jogo3:
            sg.popup_error('Atençao', f"Faça seu palpite, {nome}.",font=("Verdana",10))
            return
        if not jogo4:
            sg.popup_error('Atençao', f"Faça seu palpite, {nome}.",font=("Verdana",10))
            return
        if not jogo5:
            sg.popup_error('Atençao', f"Faça seu palpite, {nome}.",font=("Verdana",10))
            return
        
        sg.popup_auto_close(
            f"Palpites: {nome}\n\nJogo 1: {jogo1}\nJogo 2: {jogo2}\nJogo 3: {jogo3}\nJogo 4: {jogo4}\nJogo 5: {jogo5}",auto_close=False,font=("Verdana",11)
        )
        
        self.window["nome_jogador"].update(disabled=True)
        self.window["palpite_1"].update(disabled=True)
        self.window["palpite_2"].update(disabled=True)
        self.window["palpite_3"].update(disabled=True)
        self.window["palpite_4"].update(disabled=True)
        self.window["palpite_5"].update(disabled=True)
        

    def iniciarInterface(self):
        while True:
            event, values = self.window.read() # type: ignore

            if event == sg.WIN_CLOSED or event == "Cancelar":
                break
            elif event == "Palpitar":
                self.iniciarAposta()

        self.window.close()

if __name__ == "__main__":
    jogo = PalpitesDS()
    jogo.iniciarInterface()