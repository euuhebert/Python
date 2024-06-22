# Clasees geram novos objetos
#Pascal case
#



class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Hebert', 'Rocha')
p2 = Pessoa('Maria', 'Joana')

print(p1.nome, p1.sobrenome)    
print(p2.nome, p2.sobrenome)    

