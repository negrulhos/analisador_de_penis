import customtkinter as ctk
from customtkinter import *

# Deixar o tema escuro e cor principal azul
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Tamanho e curvatura média do penis brasileiro
media_penis = 12

media_curvatura = 30

# Criar a janela do sistema
janela = ctk.CTk()
janela.title("Analisador De Penis V5.0")
janela.geometry("600x440")
janela.resizable(False, False)
janela.withdraw()

# Mostrar mensagem de Boas Vindas
label = ctk.CTkLabel(janela, text="Analisador de penis 5.0", font=("Arial", 24, "bold"))
label.pack(pady=20)

# Campo para digitar o tamanho do penis do user
label_tamanho = ctk.CTkLabel(janela, text="Digite o tamanho do seu penis", font=("Arial", 12))
tamanho_penis = ctk.CTkEntry(janela, width=150, font=("Arial", 14), justify="center")
label_tamanho.pack(pady=15)
tamanho_penis.pack()


# Campo para digitar a curvatura do penis do user
label_curvatura = ctk.CTkLabel(janela, text="Digite a curvatura do seu penis", font=("Arial", 12,))
curvatura_penis = ctk.CTkEntry(janela, width=150, font=("Arial", 14), justify="center")
label_curvatura.pack(pady=15)
curvatura_penis.pack()

# Função para analisar a curvatura e o tamanho
def analisar():
    try:
        tamanho = int(tamanho_penis.get())
        curvatura = int(curvatura_penis.get())

        msg = ""

        if tamanho >= media_penis:
            msg += f"Tamanho: {tamanho}cm - Belo penis lil blood, acima da média! 🍆\n \n"
        
        else:
            msg += f"Tamanho: {tamanho}cm - Melhor começar a tomar um tadala, abaixo da média :(\n \n"
        
        if curvatura >= media_curvatura:
            msg += f"Curvatura: {curvatura}° - Ta com um bumerangue entre as pernas??\n \n"

        else:
            msg += f"Curvatura: {curvatura}° - Está com uma seta entre as calças?? Pau retão parça\n \n"

# Cria nova janela com a mensagem
        result = ctk.CTkToplevel(janela)
        result.title("Resultado da Análise")
        result.geometry("555x320")

        label_result = ctk.CTkLabel(result, text=msg, font=("Arial", 14, "bold"), justify="center")
        label_result.pack(padx=20, pady=20, expand="true")

    except ValueError:
        error = ctk.CTkToplevel(janela)
        error.title("Erro")
        ctk.CTkLabel(error, text="Digita numeros validos filho da puta burro").pack(padx=20, pady=20)

# Botão para analisar
button = ctk.CTkButton(janela, text="Começar analise", command=analisar, font=("Arial", 14, "bold"), height=35)
button.pack(pady=20)


# Janela de login
janela_login = ctk.CTkToplevel(janela)
janela_login.title("Login Analisador")
janela_login.geometry("600x400")
janela_login.resizable(False, False)

# Mostrar mensagem de login
label_login = ctk.CTkLabel(janela_login, text="Entrar", font=("Arial", 24, "bold"), justify="center")
label_login.pack(pady=20, expand="true")

# Campo Para digitar o usuario e senha
user_login = ctk.CTkEntry(janela_login, width=150, justify="center")
label_user = ctk.CTkLabel(janela_login, text="Usuario:", font=("Arial", 10, "bold"))
label_user.pack()
user_login.pack()

password_login = ctk.CTkEntry(janela_login, width=150, show="*", justify="center")
label_password = ctk.CTkLabel(janela_login, text="Senha:", font=("Arial", 10, "bold"))
label_password.pack()
password_login.pack()

# Função de fechar a janela
def fechar_janela():
    janela_login.destroy()
    janela.deiconify()

# Botão de login
botao_logar = ctk.CTkButton(janela_login, text="Logar", command=fechar_janela, height=35, width=100, corner_radius=15)
botao_logar.pack(expand="true")

# Rodar a Janela do sistema
janela.mainloop()