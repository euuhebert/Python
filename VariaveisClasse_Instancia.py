
class Estudante:
    escola = "DIO" # atributo de classe corresponde a todos os objetos da classe.

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome}  -  {self.matricula}"
    
aluno1 = Estudante("Guilherme", 1234)
aluno2 = Estudante("Giovanna", 1236)

print(aluno1)
print(aluno2)

print(Estudante.escola)
Estudante.escola = "Microlins"
print(Estudante.escola)

