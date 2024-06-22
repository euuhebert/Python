
class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def Criar_apartir_DataNascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)
    
    @staticmethod
    def maiorIdade(idade):
        return idade >= 18
        


p = Pessoa.Criar_apartir_DataNascimento(2001, 7, 23, "Hebert")

print(p.nome, p.idade)

print(Pessoa.maiorIdade(18))
print(Pessoa.maiorIdade(17))

