from tkinter import *
from random import *


# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul
cor7 = "#333333"  # dark grey / cinza escuro

lista_player1 = []
lista_player2 = []
lista_resp = [[1,2,3], [1,4,7], [1,5,9], [6,5,4], [9,8,7], [9,6,3], [8,5,2], [7,5,3]]
botoes = []
cont = 0

root = Tk()
root.title("JOGO DA VELHA")
root.geometry("360x490")
root.config(bg=cor7)
root.resizable(width=False, height=False)




#Funções --------------------------------
def iniciar():
    botao_iniciar.destroy()

    #Labels -----------------------------
    labels_1 = Label(root, width=39, height=1, text="", bg="white")
    labels_1.place(x=38, y=270)

    labels_2 = Label(root, width=39, height=1, text="", bg="white")
    labels_2.place(x=38, y=375)

    labels_3 = Label(root, width=2, height=18, text="", bg="white")
    labels_3.place(x=120, y=195)

    labels_4 = Label(root, width=2, height=18, text="", bg="white")
    labels_4.place(x=220, y=195)


    for i in range(9):
        
        botao = Button(root, width=11, height=5, text="", bg="Grey", command=lambda num=i+1: jogar(num))
        botao.place(x=(38 + (i // 3) * 98), y=(190 + (i % 3) * 100))
        botoes.append(botao)

def reiniciar():

    botoes.clear()
    lista_player1.clear()
    lista_player2.clear()
    iniciar()

    placar_1["text"] = 0
    placar_2["text"] = 0
    label_gan1 = Label(root, width=30, height=1, text="", bg=cor1)
    label_gan1.place(x=70, y=140)

    label_esconder = Label(root, width=30, height=2, text="", anchor="center", bg=cor1)
    label_esconder.place(x=116, y=25)

    for b in botoes: #SE QUISER DESABILITAR TODOS OS BOTÕES
        b.config(state=NORMAL)


def jogar(num_botao):
    global lista_player1
    global lista_player2
    global lista_resp
    global cont


    botao = botoes[num_botao - 1]  # Obtem o botão correspondente ao número clicado
    cont += 1


    if not cont % 2 == 0:
        
        label_x = Label(botao, width=2, height=1, text="X", anchor="center", relief="flat", font="Ivy 46 bold",fg=cor4, bg="grey")
        label_x.grid()

        lista_player1.append(num_botao)
        cont1 = len(lista_player1)
        placar_1["text"] = cont1
        
    else:
        label_O = Label(botao, width=2,height=1, text="O", anchor="center", relief="flat", font="Ivy 46 bold",fg=cor6, bg="grey")
        label_O.grid()

        lista_player2.append(num_botao)
        cont2 = len(lista_player2)
        placar_2["text"] = cont2
    

    
    for resp in lista_resp:
        if set(resp).issubset(lista_player1):

            label_gan1 = Label(root, width=21, height=1, text="Jogador 1 GANHOUU!!", bg=cor1, fg=cor4, font="Arial 12 bold")
            label_gan1.place(x=70, y=140)

            botao_reiniciar = Button(root, width=15, height=1, text="Jogar novamente", anchor="center", bg=cor7, fg="white", font="Ivy 10", command=reiniciar)
            botao_reiniciar.place(x=116, y=25)
            
            cont = 0
            

        if set(resp).issubset(lista_player2):

            label_gan1 = Label(root, width=21, height=1, text="Jogador 2 GANHOUU!!", bg=cor1, fg=cor6, font="Arial 12 bold")
            label_gan1.place(x=70, y=140)

            botao_reiniciar = Button(root, width=15, height=1, text="Jogar novamente", anchor="center", bg=cor7, fg="white", font="Ivy 10", command=reiniciar)
            botao_reiniciar.place(x=116, y=25)

            cont = 0    
        
        '''
            label_gan1 = Label(root, width=21, height=1, text="DEU VELHA!!", bg=cor1, fg=cor6, font="Arial 12 bold")
            label_gan1.place(x=70, y=140)

            botao_reiniciar = Button(root, width=15, height=2, text="Jogar novamente", anchor="center", bg=cor5, font="Ivy 10", command=iniciar)
            botao_reiniciar.place(x=20, y=10)

            cont = 0
            '''

    botao.config(state=DISABLED)


#Frame ----------------------------------
frame1 = Frame(root, width=320, height=150, bg=cor1)
frame1.grid(row=0, column=0, pady=20, padx=20)



#Labels ---------------------------------
#Jogador 1 ------------------------------
player_x = Label(frame1, height=2, text="X", anchor="center", relief="flat", fg=cor4, bg=cor1, font="Ivy 40 bold")
player_x.place(x=40, y=2)

placar_1 = Label(frame1, height=2, text="0", anchor="center", relief="flat", fg="white", bg=cor1, font="Ivy 40 bold")
placar_1.place(x=90, y=2)

player_1 = Label(frame1, height=2, text="Player 1", bg=cor1, anchor="center", fg="white", font="Ivy 10")
player_1.place(x=60, y=90)

#Jogador 2 ------------------------------
player_o = Label(frame1, height=2, text="O", anchor="center", relief="flat", fg=cor6, bg=cor1, font="Ivy 40 bold")
player_o.place(x=240, y=2)

placar_2 = Label(frame1, height=2, text="0", anchor="center", relief="flat", fg="white", bg=cor1, font="Ivy 40 bold")
placar_2.place(x=195, y=2)

player_2 = Label(frame1, height=2, text="Player 2", bg=cor1, anchor="center", fg="white", font="Ivy 10")
player_2.place(x=210, y=90)

#Separação ------------------------------
label_2 = Label(frame1, height=2, text=":", anchor="center", relief="flat", fg="White", bg=cor1, font="Ivy 40 bold")
label_2.place(x=150, y=2)



#Botões ---------------------------------

botao_iniciar = Button(root, width=10, height=1, text="Novo jogo", anchor="center", bg=cor5, font="Ivy 10", command=iniciar)
botao_iniciar.place(x=130, y=350)



root.mainloop()