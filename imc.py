import tkinter as tk


#calcula o imc
def calcular():
    imc = float(peso.get()) / float(altura.get()) ** 2
    resultado['text'] = f'O seu IMC é {imc}'

#abre a janela
janela = tk.Tk()
posicao = tk.Frame(janela, padx=30, pady=30).grid(column=1, row=1)

#texto inicial
tk.Label(posicao, text='Insira os valores abaixo para descobrir seu IMC:', pady=30).grid(column=1, row=1)

#recebe peso
tk.Label(posicao, text='Qual é o seu peso? (kg)').grid(column=1, row=4)
peso = tk.Entry(posicao)
peso.grid(column=2, row=4)

#recebe altura
tk.Label(posicao, text='Qual é a sua altura? (m)').grid(column=1, row=5)
altura = tk.Entry(posicao)
altura.grid(column=2, row=5)

#botão que puxa o resultado
tk.Button(posicao, text='Calcular', command=calcular).grid(column=1, row=6)
resultado = tk.Label(posicao)
resultado.grid(column=1, row=7, columnspan=2)

janela.title('Calculadora de IMC')
janela.mainloop()