#Tema: Escolher um problema seu e aplicar os conceitos vistos

# meu problema é que quero colocar linhas nos títulos para deixar eles mais organizados, porém isso é trabalhoso e repetitivo, considerando que toda vez preciso escrever:
#print('-' * 30)
#print(        'título'          )
#print('-' * 30)

#como isso é uma constante/rotina, posso otimizar isso escrevendo:

def mostralinha():
print('-' * 30)

# e toda vez que precisar uma linha posso usar:
def lin():
lin()
print('título')
lin()

# posso otimizar esse processo ainda mais para quando quiser escrever mais de um título, fazendo:


def título (título)
print('-' * 30)
print(título)
print('-' * 30)
 

# Programa principal
título ( 'título1')
título ('título2')
título ('título3')

# agora sempre que eu digitar "título", ele fará as linhas automaticamente
