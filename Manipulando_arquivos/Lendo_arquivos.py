
file = open('/home/hebert/Área de Trabalho/Projetos/Python/Manipulando_arquivos/exemplo.txt', 'r')

#Lê o arquivo inteiro 
#print(file.read())

#Lê linha por linha
#print(file.readline())

#Exemplo de uso

#for linha in file.readline():
 #   print(linha)

for linha in file.readlines():
    print(linha)

file.close()