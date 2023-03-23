import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox


valores_x = []
valores_y = []

def adicionar_valores():
    global valores_x, valores_y
    try:
        x = float(txt_novo_x.get())
        y = float(txt_novo_y.get())
        valores_x.append(x)
        valores_y.append(y)
        atualizar_tabela_valores()
        txt_novo_x.delete(0, tk.END)
        txt_novo_y.delete(0, tk.END)
        messagebox.showinfo(title="Valores adicionados", message="Valores de x e y adicionados com sucesso!")
    except ValueError:
        messagebox.showerror(title="Erro", message="Valores de x e y devem ser números!")


def atualizar_tabela_valores():
    global valores_x, valores_y
    for widget in frame_tabela_valores.winfo_children():
        widget.destroy()
 
    for i in range(len(valores_x)):
        tk.Label(frame_tabela_valores, text="{:.2f}".format(valores_x[i]), relief="solid", borderwidth=1, width=10).grid(row=i, column=0)
        tk.Label(frame_tabela_valores, text="{:.2f}".format(valores_y[i]), relief="solid", borderwidth=1, width=10).grid(row=i, column=1)


def atualizar_grafico():
    global valores_x, valores_y

    if len(valores_x) < 2:
        messagebox.showerror(title="Erro", message="Adicione pelo menos dois pares de valores de x e y para calcular a regressão linear!")
        return
   
    x = np.array(valores_x)
    y = np.array(valores_y)
    a, b = np.polyfit(x, y, 1)

 
    plt.cla()  
    plt.plot(x, y, 'o')
    plt.plot(x, a*x + b)


    canvas.draw()


    lbl_equacao.config(text="y = {:.2f}x + {:.2f}".format(a, b))


janela = tk.Tk()
janela.title("Regressão linear")


lbl_x = tk.Label(janela, text="Valores de x:")
lbl_y = tk.Label(janela, text="Valores de y:")

frame_valores = tk.Frame(janela)
lbl_novo_x = tk.Label(frame_valores, text="Novo x:")
lbl_novo_y = tk.Label(frame_valores, text="Novo y:")
txt_novo_x = tk.Entry(frame_valores)
txt_novo_y = tk.Entry(frame_valores)

lbl_x = tk.Label(janela, text="Valores de x:")
lbl_y = tk.Label(janela, text="Valores de y:")

frame_valores = tk.Frame(janela)
lbl_novo_x = tk.Label(frame_valores, text="Novo x:")
lbl_novo_y = tk.Label(frame_valores, text="Novo y:")
txt_novo_x = tk.Entry(frame_valores)
txt_novo_y = tk.Entry(frame_valores)

btn_adicionar = tk.Button(janela, text="Adicionar valores", command=adicionar_valores)
btn_atualizar = tk.Button(janela, text="Atualizar gráfico", command=atualizar_grafico)

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


frame_tabela_valores = tk.Frame(janela)
lbl_tabela_valores = tk.Label(frame_tabela_valores, text="Valores adicionados:")
lbl_tabela_valores.grid(row=0, column=0)
tk.Label(frame_tabela_valores, text="x", relief="solid", borderwidth=1, width=10).grid(row=1, column=0)
tk.Label(frame_tabela_valores, text="y", relief="solid", borderwidth=1, width=10).grid(row=1, column=1)
frame_tabela_valores.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

lbl_equacao = tk.Label(janela, text="")

lbl_x.pack()
lbl_y.pack()
frame_valores.pack()
lbl_novo_x.grid(row=0, column=0)
txt_novo_x.grid(row=0, column=1)
lbl_novo_y.grid(row=1, column=0)
txt_novo_y.grid(row=1, column=1)
btn_adicionar.pack()
btn_atualizar.pack()
lbl_equacao.pack()

janela.mainloop()