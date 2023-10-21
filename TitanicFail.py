#app que usar uma database ja existente para cria um grafico
# baseando as estatiticas nas informcoes contidas no ficheiro csv
# usadr dados um ficheiro ja existente da projeto py
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

df = pd.read_csv('titanic.csv')


def titaNic():
    seres = df['sex'].value_counts()
    info = df['survived'].value_counts()
    up = df.groupby(['sex', 'survived']).size().unstack(fill_value=0)

    plt.bar(up.index, up[1], label='Survived')
    plt.bar(up.index, up[0], label='Not Survived', bottom=up[1])

    plt.title('Titanic Data Analysis')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.grid()

    for index, value in enumerate(up[0]):
        plt.text(index, up[1][index] + up[0][index], str(value), ha='center', va='bottom')

    for index, value in enumerate(up[1]):
        plt.text(index, up[1][index] - (up[1][index] // 2), str(value), ha='center', va='bottom')

    plt.legend()
    plt.show()


janela = tk.Tk()
janela.title('TITANIC')

# widget de rótulo (Label) para exibir a imagem
imagem = Image.open('84anos.jpg')
imagem = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(janela, image=imagem)
label_imagem.pack()

# widget de rótulo para o texto "Statistic"
janela_label = tk.Label(janela, text="Statistic", fg='blue')
janela_label.pack()

# botão abaixo do rótulo de texto
botao = tk.Button(janela, text="caosTitanic", command=titaNic)
botao.pack()

janela.mainloop()