
file = open('/home/hebert/Área de Trabalho/Projetos/Python/Manipulando_arquivos/humor.txt', 'w')


file.write('Olá Hebert')
file.writelines(["Escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])

file.close()
