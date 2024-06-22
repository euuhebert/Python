
class Cachorro:
    def __init__(self, nome, cor, acordado= True):
        print('inciando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


    def latir(self):
        print("auau")

    def __del__(self, nome, cor, acordado= True):
        print("Destruindo a instancia")

c = Cachorro('Junin Ruinda', 'Preto', True)
print(c.nome, c.cor)
c.latir()


    
