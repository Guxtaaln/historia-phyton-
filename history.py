import random

# Função que gera a introdução da história 

def gerar_introducao():
    introducoes = ["Era uma vez", "Há muito tempo atrás", "Num reino distante"]
    return random.choice(introducoes)

# Função que gera o desenvolvimento da história 
def gerar_desenvolvimento():
    desenvolvimentos =  ["um valente cavaleiro" , "uma destemida guerreira" , "um bravo guerreiro" , "uma poderosa feiticeira" , "um sábio mago"]
    return  random.choice(desenvolvimentos)

# Função pricipal que gera o final da história 
def gerar_final():
    finais =  ["enfrentando dragões ferozes." , "derrotando um terrível vilão." ,
                "descobrindo um tesouro escondido." , "salvando o reino da escuridão." , 
                "encontrando um amor verdadeiro."]

return random.choice(finais)

# Função principal que gera toda a história 
def gerar_historia();
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia

# Exibe a história gerada 
if  __name_ == "__main__":
    print(gerar_historia())_


