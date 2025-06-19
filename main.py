print("Hello World!")

msg_sem_maturidade = "Tu tem maturidade pra porra nenhuma!"
msg_maturidade = "Agora sim tu tem maturidade neste caralho, porra!"

def main():
    maturidade = False
    while not maturidade:
        resposta = input("Você tem maturidade? (s/n): ").strip().lower()
        if resposta == 's':
            maturidade = True
            print(msg_maturidade)
        elif resposta == 'n':
            print(msg_sem_maturidade)
            break
        else:
            print("Responde direito, porra! É 's' ou 'n'!")

if __name__ == "__main__":
    main()
