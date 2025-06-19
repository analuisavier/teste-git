import os
import time  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

msg_sem_maturidade = "Tu é um fudido!"
msg_maturidade = "Tu é pica das galáxias, porra!"

def teste_maturidade():
    while True:
        clear_screen()
        resposta = input("Você tem maturidade? (s/n): ").strip().lower()
        if resposta == 's':
            print("Carregando...")
            time.sleep(2)  
            print(msg_maturidade)
            print("Parabéns, porra! Tu é maduro pra caralho!")
            break
        elif resposta == 'n':
            print("Carregando...")
            time.sleep(2)  
            print(msg_sem_maturidade)
            print("Que pena, porra! Tenta de novo quando tiver mais maduro!")
            break
        else:
            print("Responde direito, porra! É 's' ou 'n'!")

def main():
    print("Teste de Maturidade, porra!")
    input("Mete o dedo no Enter para começar...")  
    while True:
        teste_maturidade()
        reiniciar = input("Quer tentar de novo? (s/n): ").strip().lower()
        if reiniciar != 's':
            print("Falou, porra!")
            break

if __name__ == "__main__":
    main()
