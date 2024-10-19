import random
import tkinter as tk
from tkinter import messagebox

# Inicialização da pontuação
pontuacao_jogador = 0
pontuacao_computador = 0

# Função para determinar o vencedor
def verificar_vencedor(escolha_jogador):
    global pontuacao_jogador, pontuacao_computador

    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = random.choice(opcoes)
    
    resultado_texto = f"Você escolheu: {escolha_jogador}\nComputador escolheu: {escolha_computador}\n"
    
    if escolha_jogador == escolha_computador:
        resultado_texto += "Resultado: Empate!"
    elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
         (escolha_jogador == "tesoura" and escolha_computador == "papel") or \
         (escolha_jogador == "papel" and escolha_computador == "pedra"):
        resultado_texto += "Resultado: Você venceu!"
        pontuacao_jogador += 1
    else:
        resultado_texto += "Resultado: Você perdeu!"
        pontuacao_computador += 1

    # Atualiza o rótulo de resultado e a pontuação
    resultado_label.config(text=resultado_texto)
    pontuacao_label.config(text=f"Pontuação - Você: {pontuacao_jogador} | Computador: {pontuacao_computador}")

# Criar a janela principal
janela = tk.Tk()
janela.title("Pedra, Papel, Tesoura")
janela.geometry("400x350")

# Texto de introdução
introducao_label = tk.Label(janela, text="Escolha sua jogada:", font=("Arial", 14))
introducao_label.pack(pady=10)

# Botões de escolha do jogador
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_pedra = tk.Button(frame_botoes, text="Pedra", width=10, command=lambda: verificar_vencedor("pedra"))
botao_pedra.grid(row=0, column=0, padx=10)

botao_papel = tk.Button(frame_botoes, text="Papel", width=10, command=lambda: verificar_vencedor("papel"))
botao_papel.grid(row=0, column=1, padx=10)

botao_tesoura = tk.Button(frame_botoes, text="Tesoura", width=10, command=lambda: verificar_vencedor("tesoura"))
botao_tesoura.grid(row=0, column=2, padx=10)

# Label para mostrar o resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 12), justify="center")
resultado_label.pack(pady=20)

# Label para mostrar a pontuação
pontuacao_label = tk.Label(janela, text="Pontuação - Você: 0 | Computador: 0", font=("Arial", 12))
pontuacao_label.pack(pady=10)

# Botão para sair do jogo
botao_sair = tk.Button(janela, text="Sair", command=janela.quit, width=10)
botao_sair.pack(pady=10)

# Executar a janela
janela.mainloop()
