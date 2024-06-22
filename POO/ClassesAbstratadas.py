# Definem o que deve ser feito e não como
#forçar a implementação de comportamento desejado

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV...")
    
    def desligar(self):
        print("Desligando TV...")

class ControleArcondiconado(ControleRemoto):
    def ligar(self):
        print("Ligando ar...")
    
    def desligar(self):
        print("Desligando ar...")


controle = ControleTV()
controle.ligar()
controle.desligar()

controleAr = ControleArcondiconado()

controleAr.ligar()
controleAr.desligar()

