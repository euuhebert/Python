## Na herança a classe filha herda os métodos da classe pa. No entanto, é possível modificar um método em uma classee filha herdada da classe pai. Isso é particularmente útil nos casos em que método hedado da classe pai não se encaixa perfeitamente na classe filha.##

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

#Exenplo ruim de uso de herança
class Aviao(Passaro):
    def voar(self):
        print("avião está decolando...")

def plano_de_voo(obj):
    obj.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())