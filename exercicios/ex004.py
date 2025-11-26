import tkinter as tk


def clicar(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, atual + botao)


def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)  # cuidado: eval só é seguro em testes simples
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")


def limpar():
    entrada.delete(0, tk.END)


# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")

# Campo de entrada
entrada = tk.Entry(janela, width=20, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Lista de botões
botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

linha = 1
coluna = 0

for botao in botoes:
    if botao == "=":
        tk.Button(janela, text=botao, width=5, height=2, font=("Arial", 14),
                  command=calcular).grid(row=linha, column=coluna, padx=5, pady=5)
    else:
        tk.Button(janela, text=botao, width=5, height=2, font=("Arial", 14),
                  command=lambda b=botao: clicar(b)).grid(row=linha, column=coluna, padx=5, pady=5)

    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Botão de limpar
tk.Button(janela, text="C", width=22, height=2, font=("Arial", 14),
          command=limpar).grid(row=linha, column=0, columnspan=4, padx=5, pady=5)

janela.mainloop()
