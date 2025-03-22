from PIL import Image, ImageTk
from datetime import datetime
import customtkinter as ctk
import time
import json


def save(list, path):
    with open(path, "w", encoding="utf-8") as arquivo:
        dados = json.dump(list, arquivo, ensure_ascii=False, indent=2)
    return dados


def read(list, path):
    dados = list
    with open(path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados


CAMINHO_USUARIOS = "data_users.json"
CAMINHO_LISTA = "data_list.json"
CAMINHO_LIXEIRA = "data_list_trash.json"
lista_usuarios = read([], CAMINHO_USUARIOS)
lista_tarefas = read([], CAMINHO_LISTA)
lixeira = read([], CAMINHO_LIXEIRA)
contador_de_tarefas = 0
indice_tarefas = len(lista_tarefas) if lista_tarefas else 0

# criando a janela splash
splash = ctk.CTk()
splash.title("Bat Lista")
splash.geometry("700x400")
# removendo a barra de titulo
splash.overrideredirect(True)

# carregando imagem do splash
IMAGE_SPLASH = ctk.CTkImage(
    light_image=Image.open("images/Bat_logo.png"), size=(700, 400)
)

# Adicionando a Imagem na splash screen
label_logo = ctk.CTkLabel(splash, image=IMAGE_SPLASH, text="")
label_logo.pack(expand=True)

# criando efeito de carregamento
barra = ctk.CTkProgressBar(
    splash,
    width=300,
    height=8,
)
barra.place(relx=0.5, rely=0.9, anchor="center")
barra.set(0)

# Atualizando barra de progresso
for intervalo in range(101):
    barra.set(intervalo / 100)
    splash.update()
    time.sleep(0.02)
# fechando a splash
splash.destroy()


# Criar janela principal------------------------------------------------------------------------
app = ctk.CTk()
app.title("Bat Tasks")
# Obtendo tamanho da tela
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()
app.geometry(f"{largura_tela}x{altura_tela}+0+0")
app.configure(fg_color="#454648")
user_logado = ""
app._set_appearance_mode("dark")


def update_widgets():
    for widget in app.winfo_children():
        widget.pack_forget()
        widget.place_forget()


# PARTE DO LOGIN --------------------------------------------------------------------------------------------------------------
def janela_login():
    global user_logado
    update_widgets()
    app.configure(fg_color="#454648")
    user_logado = ""

    def verificar_login():
        global user_logado
        chave_de_acesso = False
        email = entry_user_login.get()
        senha = entry_senha.get()
        email_entry_espacos = entry_user_login.get().strip()
        senha_entry_espacos = entry_senha.get().strip()

        if not email_entry_espacos or not senha_entry_espacos:
            label_login_resultado.configure(
                text="Preencha todos os campos",
                text_color="red",
                font=("Arial", 13, "bold"),
            )
            label_login_resultado.place(x=190, y=600)

        elif lista_usuarios == []:
            label_login_resultado.configure(
                text="Email e/ou senha incorretos",
                text_color="red",
                font=("Arial", 13, "bold"),
            )
            label_login_resultado.place(x=190, y=600)

        else:
            for usuario in lista_usuarios:
                if usuario["email"] == email and usuario["senha"] == senha:
                    label_login_resultado.configure(
                        text="Login bem sucedido!",
                        text_color="green",
                        font=("Arial", 13, "bold"),
                    )
                    label_login_resultado.place(x=210, y=600)
                    user_logado = usuario
                    chave_de_acesso = True
                    app.after(2000, page_usuario)

            if chave_de_acesso == False:
                label_login_resultado.configure(
                    text="Email e/ou senha incorretos",
                    text_color="red",
                    font=("Arial", 13, "bold"),
                )
                label_login_resultado.place(x=190, y=600)

    # Criando imagem de fundo
    IMAGE_JANELA_PRINCIPAL = ctk.CTkImage(
        light_image=Image.open("images/Bat (8).png"), size=(largura_tela, altura_tela)
    )

    IMAGE_EMAIL = ctk.CTkImage(
        light_image=Image.open("images/e_mail.png"), size=(100, 55)
    )
    IMAGE_SENHA = ctk.CTkImage(
        light_image=Image.open("images/senha.png"), size=(110, 62)
    )

    # Criando um label para a imagem de fundo
    label_fundo = ctk.CTkLabel(app, image=IMAGE_JANELA_PRINCIPAL, text="")
    label_fundo.place(
        relx=0, rely=0, relwidth=1, relheight=1
    )  # Expande para cobrir a tela

    # Criando um frame
    frame_login = ctk.CTkFrame(
        app, width=550, height=700, corner_radius=6, border_width=2, fg_color="white"
    )
    frame_login.place(x=820, y=0)

    label_boas_vindas = ctk.CTkLabel(
        frame_login,
        text="Seja bem vindo(a) ao Bat Tasks!",
        text_color="#6A0DAD",
        font=("nunito", 27, "bold"),
    )
    label_boas_vindas.place(x=20, y=70)

    label_msg = ctk.CTkLabel(
        frame_login,
        text_color="grey",
        text="Entre com sua Conta Bat",
        font=("Roboto", 18, "bold"),
    )
    label_msg.place(x=20, y=120)

    label_email = ctk.CTkLabel(frame_login, image=IMAGE_EMAIL, text="")
    label_email.place(x=20, y=200)

    entry_user_login = ctk.CTkEntry(
        frame_login,
        border_color="#6A0DAD",
        fg_color="#D3D3D3",
        text_color="black",
        placeholder_text="Digite seu Email",
        width=500,
        height=45,
        font=("Arial", 14, "bold"),
    )
    entry_user_login.place(x=20, y=250)

    label_senha = ctk.CTkLabel(frame_login, image=IMAGE_SENHA, text="")
    label_senha.place(x=7, y=350)

    entry_senha = ctk.CTkEntry(
        frame_login,
        border_color="#6A0DAD",
        fg_color="#D3D3D3",
        text_color="black",
        placeholder_text="Digite sua senha",
        width=500,
        height=45,
        font=("Arial", 14, "bold"),
        show="*",
    )
    entry_senha.place(x=20, y=400)

    button_login = ctk.CTkButton(
        frame_login,
        text="Login",
        fg_color="#6A0DAD",
        width=500,
        height=45,
        font=("Roboto", 20, "bold"),
        hover_color="#D3D3D3",
        command=verificar_login,
    )
    button_login.place(x=20, y=480)

    button_cadastro = ctk.CTkButton(
        frame_login,
        text="👤 Criar uma nova conta",
        fg_color="#D3D3D3",
        width=500,
        height=45,
        font=("Roboto", 16, "bold"),
        text_color="#6A0DAD",
        command=janela_cadastro,
    )
    button_cadastro.place(x=20, y=540)

    label_projeto = ctk.CTkLabel(
        frame_login, text="© Bat Familia 🦇", font=("Arial", 17, "bold")
    )
    label_projeto.place(x=212, y=660)

    text_intro_1 = "Gerencie todos os seus afazeres do dia a dia com o Bat Tasks!"
    text_intro_2 = "Um software que gerencia suas tarefas de forma prática e útil."

    label_intro_1 = ctk.CTkLabel(
        app, text=text_intro_1, text_color="white", font=("Roboto", 23, "bold")
    )
    label_intro_1.place(x=40, y=290)

    label_intro_2 = ctk.CTkLabel(
        app, text=text_intro_2, text_color="white", font=("Roboto", 20, "bold")
    )
    label_intro_2.place(x=70, y=315)

    label_login_resultado = ctk.CTkLabel(
        frame_login,
        text="",
    )
    label_login_resultado.place(x=190, y=600)


#   PARTE DO CADASTRO ----------------------------------------------------------------------------------------------------
def janela_cadastro():
    update_widgets()

    def verificar_cadastro():
        chave_de_acesso = True
        username_espacos = entry_nome_usuario.get().strip()
        email_espacos = entry_email_usuario.get().strip()
        senha_espacos = entry_senha_usuario.get().strip()
        username = entry_nome_usuario.get()
        email = entry_email_usuario.get()
        senha = entry_senha_usuario.get()
        senha_confirmar = entry_senha_confirmar_usuario.get()
        senha_confirmar_espacos = entry_senha_confirmar_usuario.get().strip()

        if (
            not username_espacos
            or not email_espacos
            or not senha_espacos
            or not senha_confirmar_espacos
        ):
            label_resultado.configure(
                text="Preencha todos os campos",
                text_color="red",
                font=("Arial", 13, "bold"),
            )
            chave_de_acesso = False

        elif senha != senha_confirmar:
            label_resultado.configure(
                text="As senhas não são iguais",
                text_color="red",
                font=("Arial", 13, "bold"),
            )
            label_resultado.place(x=240, y=440)
            chave_de_acesso = False

        elif len(senha) < 8:
            label_resultado.configure(
                text="A senha deve conter ao menos 8 caracteres",
                text_color="red",
                font=("Arial", 13, "bold"),
            )
            label_resultado.place(x=178, y=440)
            chave_de_acesso = False

        elif lista_usuarios:
            for user in lista_usuarios:
                if user["email"] == email:
                    label_resultado.configure(
                        text="Já existe uma conta vinculada a esse email.",
                        text_color="red",
                        font=("Arial", 13, "bold"),
                    )
                    label_resultado.place(x=178, y=440)
                    chave_de_acesso = False

        if chave_de_acesso:
            conta_criada = {"username": username, "email": email, "senha": senha}
            lista_usuarios.append(conta_criada)
            save(lista_usuarios, CAMINHO_USUARIOS)
            label_resultado.configure(
                text="Conta criada com sucesso.",
                text_color="green",
                font=("Arial", 13, "bold"),
            )
            label_resultado.place(x=238, y=440)

    IMAGE_JANELA_PRINCIPAL = ctk.CTkImage(
        light_image=Image.open("images/Bat (8).png"), size=(largura_tela, altura_tela)
    )

    # Criando um label para a imagem de fundo
    label_fundo = ctk.CTkLabel(app, image=IMAGE_JANELA_PRINCIPAL, text="")
    label_fundo.place(
        relx=0, rely=0, relwidth=1, relheight=1
    )  # Expande para cobrir a tela

    frame_info_cadastro = ctk.CTkFrame(
        app, width=350, height=500, corner_radius=6, fg_color="#6A0DAD"
    )
    frame_info_cadastro.place(x=170, y=80)

    texto_1_cadastro = "Seja bem vindo(a)"
    texto_2_cadastro = (
        "Crie uma conta no Bat Tasks e \n aproveite as funcionalidades! \n Crie taref"
        "as, liste-as e tenha \n seu dia a dia nas palmas \n de suas mãos."
    )

    label_info_cadastro = ctk.CTkLabel(
        frame_info_cadastro,
        text=texto_1_cadastro,
        text_color="white",
        font=("Nunito", 33, "bold"),
    )
    label_info_cadastro.place(x=35, y=140)

    label_info_cadastro_2 = ctk.CTkLabel(
        frame_info_cadastro,
        text=texto_2_cadastro,
        text_color="white",
        font=("Nunito", 20),
    )
    label_info_cadastro_2.place(x=30, y=210)

    button_info_cadastro_to_login = ctk.CTkButton(
        frame_info_cadastro,
        font=("Arial", 14, "bold"),
        text="Login",
        text_color="white",
        corner_radius=25,
        fg_color="transparent",
        border_width=2,
        border_color="white",
        hover_color="#D3D3D3",
        command=janela_login,
    )
    button_info_cadastro_to_login.place(x=100, y=345)

    frame_cadastro = ctk.CTkFrame(app, width=650, height=500, fg_color="white")
    frame_cadastro.place(x=530, y=80)

    entry_nome_usuario = ctk.CTkEntry(
        frame_cadastro,
        placeholder_text="👤 Nome de usuário",
        width=400,
        height=50,
        fg_color="#D3D3D3",
        font=("Arial", 14),
    )
    entry_nome_usuario.place(x=120, y=150)

    entry_email_usuario = ctk.CTkEntry(
        frame_cadastro,
        placeholder_text="✉️Email",
        width=400,
        height=50,
        fg_color="#D3D3D3",
        font=("Arial", 14),
    )
    entry_email_usuario.place(x=120, y=210)

    entry_senha_usuario = ctk.CTkEntry(
        frame_cadastro,
        placeholder_text="🔒 Crie uma senha",
        width=400,
        height=50,
        fg_color="#D3D3D3",
        font=("Arial", 14),
        show="*",
    )
    entry_senha_usuario.place(x=120, y=270)

    entry_senha_confirmar_usuario = ctk.CTkEntry(
        frame_cadastro,
        placeholder_text="🔒 Confirme a senha",
        width=400,
        height=50,
        fg_color="#D3D3D3",
        font=("Arial", 14),
        show="*",
    )
    entry_senha_confirmar_usuario.place(x=120, y=330)

    button_cadastro = ctk.CTkButton(
        frame_cadastro,
        font=("Arial", 14, "bold"),
        text="Criar conta",
        text_color="white",
        corner_radius=25,
        fg_color="#6A0DAD",
        border_width=4,
        border_color="#6A0DAD",
        hover_color="#D3D3D3",
        command=verificar_cadastro,
    )
    button_cadastro.place(x=250, y=390)

    label_criar_user = ctk.CTkLabel(
        frame_cadastro,
        text_color="#6A0DAD",
        text="Criar uma nova conta",
        font=("Arial", 30, "bold"),
    )
    label_criar_user.place(x=160, y=30)

    label_info_criar = ctk.CTkLabel(
        frame_cadastro,
        text_color="#D3D3D3",
        text="Ou crie uma nova conta usando \nsua conta do Google existente",
        font=("Arial", 17, "bold"),
    )
    label_info_criar.place(x=190, y=80)

    label_resultado = ctk.CTkLabel(frame_cadastro, text="")
    label_resultado.place(x=237, y=440)


# PAGINA DO USUÁRIO------------------------------------------------------------------------------------------------------------------
def page_usuario():
    global user_logado
    update_widgets()

    app.configure(fg_color="#121212")

    def esvaziar_lixeira():
        for widget in frame_geral.winfo_children():
            widget.pack_forget()
            widget.place_forget()

        def esvaziar():
            global lixeira
            lixeira = []
            save(lixeira, CAMINHO_LIXEIRA)
            page_usuario()

        ctk.CTkLabel(
            frame_geral,
            text="Você tem certeza que quer esvaziar a lixeira 🗑️? \n"
            "todas as tarefas não poderão ser restauradas posteriormente.",
            font=("Arial", 30, "bold"),
            text_color="red",
        ).pack(padx=10, pady=200)

        botao_sim = ctk.CTkButton(
            frame_geral,
            text="Sim",
            fg_color="green",
            width=200,
            height=30,
            font=("Arial", 16, "bold"),
            command=esvaziar,
        )
        botao_sim.place(x=280, y=300)

        botao_nao = ctk.CTkButton(
            frame_geral,
            text="Não",
            fg_color="red",
            width=200,
            height=30,
            font=("Arial", 16, "bold"),
            command=page_usuario,
        )
        botao_nao.place(x=550, y=300)

    def restaurar_tarefa():
        for widget in frame_geral.winfo_children():
            widget.pack_forget()
            widget.place_forget()

        msg = ctk.CTkLabel(frame_geral, text="")
        msg.place(x=440, y=160)

        def restarurar():
            try:
                indice = entry_restaura.get()
                task = lixeira[int(indice)]
                lixeira.pop(int(indice))
                lista_tarefas.append(task)
                save(lixeira, CAMINHO_LIXEIRA)
                save(lista_tarefas, CAMINHO_LISTA)
                msg.configure(
                    text="Tarefa restaurada!",
                    text_color="green",
                    font=("Arial", 14, "bold"),
                )
                msg.place(x=465, y=160)

            except IndexError:
                msg.configure(
                    text="Essa tarefa não existe na lixeira",
                    text_color="red",
                    font=("Arial", 14, "bold"),
                )
            except ValueError:
                msg.configure(
                    text="Por favor, insira um indice",
                    text_color="red",
                    font=("Arial", 14, "bold"),
                )

        entry_restaura = ctk.CTkEntry(
            frame_geral,
            placeholder_text="Digite o indice da tarefa a ser restaurada",
            width=500,
            height=100,
            font=("Arial", 23, "bold"),
        )
        entry_restaura.pack(padx=10, pady=200)

        botao_salvar = ctk.CTkButton(
            frame_geral,
            text="Salvar",
            width=200,
            height=40,
            command=restarurar,
            font=("Arial", 14, "bold"),
            fg_color="green",
        )
        botao_salvar.place(x=430, y=340)

        botao_voltar = ctk.CTkButton(
            frame_geral,
            text="voltar",
            width=100,
            height=25,
            command=page_usuario,
            font=("Arial", 10, "bold"),
            fg_color="purple",
        )
        botao_voltar.place(x=480, y=390)

    def ver_lixeira():
        for widget in frame_geral.winfo_children():
            widget.pack_forget()
            widget.place_forget()

        if not lixeira:
            ctk.CTkLabel(
                frame_geral,
                text_color="grey",
                text="Não há tarefas na lixeira 🗑️",
                font=("Arial", 40, "bold"),
            ).pack(padx=10, pady=280)

        for tarefa in lixeira:
            ctk.CTkLabel(
                frame_geral,
                text=f"🗑️{lixeira.index(tarefa)} - {tarefa}",
                text_color="black",
                font=("Arial", 20, "bold"),
            ).pack(padx=0, pady=10)

        ctk.CTkButton(
            frame_geral, text="Voltar", font=("Arial", 14, "bold"), command=page_usuario
        ).place(x=10, y=0)

    def criar_tarefa():
        for widget in frame_geral.winfo_children():
            widget.pack_forget()
            widget.place_forget()

            def add():
                global indice_tarefas
                date_now = datetime.now()
                fmt_time = date_now.strftime("%d/%m/%Y %H:%M")
                capturar_entry = entry_tarefa.get()
                tarefa = f"{capturar_entry} {fmt_time}"
                lista_tarefas.append(tarefa)
                save(lista_tarefas, CAMINHO_LISTA)
                indice_tarefas += 1
                page_usuario()

        entry_tarefa = ctk.CTkEntry(
            frame_geral,
            corner_radius=6,
            border_width=2,
            fg_color="white",
            placeholder_text="Escreva sua terefa",
            width=800,
            height=100,
            font=("Arial", 20, "bold"),
        )
        entry_tarefa.pack(padx=100, pady=200)

        button_salvar = ctk.CTkButton(
            frame_geral,
            fg_color="#6A0DAD",
            text="Salvar Tarefa",
            font=("Arial", 20, "bold"),
            width=200,
            height=50,
            command=add,
        )
        button_salvar.place(x=425, y=330)

        botao_voltar = ctk.CTkButton(
            frame_geral, text="Voltar", font=("Arial", 14, "bold"), command=page_usuario
        )
        botao_voltar.place(x=455, y=400)

    def remover_tarefa():
        for widget in frame_geral.winfo_children():
            widget.pack_forget()
            widget.place_forget()

        msg = ctk.CTkLabel(frame_geral, text="")
        msg.place(x=440, y=160)

        def remover():
            try:
                indice = entry_remove.get()
                task = lista_tarefas[int(indice)]
                lista_tarefas.pop(int(indice))
                lixeira.append(task)
                save(lixeira, CAMINHO_LIXEIRA)
                save(lista_tarefas, CAMINHO_LISTA)
                msg.configure(
                    text="Tarefa removida",
                    text_color="green",
                    font=("Arial", 14, "bold"),
                )
                msg.place(x=465, y=160)

            except IndexError:
                msg.configure(
                    text="Essa tarefa não existe",
                    text_color="red",
                    font=("Arial", 14, "bold"),
                )
            except ValueError:
                msg.configure(
                    text="Por favor, insira um indice",
                    text_color="red",
                    font=("Arial", 14, "bold"),
                )

        entry_remove = ctk.CTkEntry(
            frame_geral,
            placeholder_text="Digite o indice da tarefa a ser excluida",
            width=500,
            height=100,
            font=("Arial", 23, "bold"),
        )
        entry_remove.pack(padx=10, pady=200)

        botao_salvar = ctk.CTkButton(
            frame_geral,
            text="Salvar",
            width=200,
            height=40,
            command=remover,
            font=("Arial", 14, "bold"),
        )
        botao_salvar.place(x=430, y=340)

        botao_voltar = ctk.CTkButton(
            frame_geral,
            text="voltar",
            width=100,
            height=25,
            command=page_usuario,
            font=("Arial", 10, "bold"),
            fg_color="green",
        )
        botao_voltar.place(x=480, y=390)

    def esvaziar_lista():
        for widget in frame_geral.winfo_children():
            widget.pack_forget()
            widget.place_forget()

            def esvaziar():
                global lista_tarefas
                lista_tarefas = []
                save(lista_tarefas, CAMINHO_LISTA)
                page_usuario()

            ctk.CTkLabel(
                frame_geral,
                text="Você tem certeza que quer esvaziar a lista? \n"
                "todas as tarefas serão excluidas permanentemente.",
                font=("Arial", 30, "bold"),
                text_color="red",
            ).pack(padx=10, pady=200)

            botao_sim = ctk.CTkButton(
                frame_geral,
                text="Sim",
                fg_color="green",
                width=200,
                height=30,
                font=("Arial", 16, "bold"),
                command=esvaziar,
            )
            botao_sim.place(x=280, y=300)

            botao_nao = ctk.CTkButton(
                frame_geral,
                text="Não",
                fg_color="red",
                width=200,
                height=30,
                font=("Arial", 16, "bold"),
                command=page_usuario,
            )
            botao_nao.place(x=550, y=300)

    frame_geral = ctk.CTkScrollableFrame(
        app, fg_color="#D3D3D3", corner_radius=30, width=1062, height=610
    )
    frame_geral.place(x=255, y=15)

    IMAGE_JANELA_LOGO = ctk.CTkImage(
        light_image=Image.open("images/Bat (10).png"), size=(155, 89)
    )

    # Criando um label para a imagem de fundo
    label_fundo = ctk.CTkLabel(app, image=IMAGE_JANELA_LOGO, text="")
    label_fundo.place(x=43, y=8)

    nome_user = user_logado["username"]
    label_boas_vindas = ctk.CTkLabel(
        app,
        text_color="white",
        text=f"Seja bem vindo, \n {nome_user}!",
        font=("Arial", 20, "bold"),
    )
    label_boas_vindas.place(x=50, y=124)

    botao_criar_tarefa = ctk.CTkButton(
        app,
        text="Criar tarefa",
        fg_color="#8A2BE2",
        width=150,
        height=30,
        font=("Arial", 12, "bold"),
        command=criar_tarefa,
    )
    botao_criar_tarefa.place(x=50, y=250)

    botao_remover_tarefa = ctk.CTkButton(
        app,
        text="Remover tarefa",
        fg_color="#FF3B30",
        width=150,
        height=30,
        font=("Arial", 12, "bold"),
        command=remover_tarefa,
    )
    botao_remover_tarefa.place(x=50, y=300)

    botao_restaurar_tarefa = ctk.CTkButton(
        app,
        text="Restaurar tarefa",
        fg_color="#00D26A",
        width=150,
        height=30,
        command=restaurar_tarefa,
        font=("Arial", 12, "bold"),
    )
    botao_restaurar_tarefa.place(x=50, y=350)

    botao_ver_lixeira = ctk.CTkButton(
        app,
        text="Analisar LIxeira",
        fg_color="#007BFF",
        width=150,
        height=30,
        font=("Arial", 12, "bold"),
        command=ver_lixeira,
    )
    botao_ver_lixeira.place(x=50, y=400)

    botao_esvaziar_lista = ctk.CTkButton(
        app,
        text="Esvaziar lista de tarefas",
        fg_color="#FF9800",
        width=150,
        height=30,
        font=("Arial", 12, "bold"),
        command=esvaziar_lista,
    )
    botao_esvaziar_lista.place(x=50, y=450)

    botao_esvaziar_lixeira = ctk.CTkButton(
        app,
        text="Esvaziar lixeira",
        fg_color="#1A237E",
        width=150,
        height=30,
        font=("Arial", 12, "bold"),
        command=esvaziar_lixeira,
    )
    botao_esvaziar_lixeira.place(x=50, y=500)

    botao_sair = ctk.CTkButton(
        app,
        text="Sair",
        fg_color="transparent",
        corner_radius=20,
        border_width=1,
        border_color="white",
        hover_color="#D3D3D3",
        width=150,
        height=30,
        font=("Arial", 12, "bold"),
        command=janela_login,
    )
    botao_sair.place(x=50, y=630)

    if not lista_tarefas:
        label_nenhuma_task = ctk.CTkLabel(
            frame_geral,
            text_color="grey",
            text="Não há tarefas criadas",
            font=("Arial", 40, "bold"),
        )
        label_nenhuma_task.pack(padx=10, pady=280)

    else:
        for tarefa in lista_tarefas:
            ctk.CTkLabel(
                frame_geral,
                text=f"{lista_tarefas.index(tarefa)} - {tarefa}",
                text_color="black",
                font=("Arial", 20, "bold"),
            ).pack(padx=0, pady=10)


janela_login()
app.mainloop()
