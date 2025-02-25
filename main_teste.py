import time
import random

def foguete_da_re():
    print("🚀 Preparando o foguete para dar ré...")  
    time.sleep(2)

    contagem = ["3...", "2...", "1...", "🚀 Ré!"]
    for numero in contagem:
        print(numero)
        time.sleep(1)

    falha_ou_sucesso = random.choice(["SUCESSO! O foguete deu ré e voltou pra base. 🏁", 
                                      "ERRO 404: Ré não encontrada, foguete foi pro espaço! 🌌",
                                      "BOOM 💥! Foguete explodiu igual promessa de político."])
    
    print(falha_ou_sucesso)

while True:
    resposta = input("Deseja ativar o modo 'Foguete da Ré'? (s/n) ").strip().lower()

    if resposta == "s":
        foguete_da_re()
    elif resposta == "n":
        print("🚀 Foguete não tem ré, mas você pode dar meia-volta e tentar de novo.")
        break
    else:
        print("❌ Opção inválida. Tente de novo, piloto!")
