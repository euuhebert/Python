
class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.i = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero  = self.numeros[self.i]
            self.i += 1
            return numero *2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[1, 2, 3]):
    print(i)


