
class Veiculo:
    def __init__(self, cor, placa, motor):
        self.cor = cor
        self.motor = motor
        self.placa = placa
        
    def ligar_motor(self):
        print('ligar motor...')

class Motocicleta(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, motor, carregado):
        super().__init__(cor, placa, motor)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")
        

class Carro(Veiculo):
    pass

moto = Motocicleta('preta', '1234', 'V8')
print(moto.cor, moto.motor, moto.placa)
moto.ligar_motor()

carro = Carro('branco', 'xde', '3 cilindros')
carro.ligar_motor()

caminhao = Caminhao('azul', '158-xfr', 'vapor', True)
caminhao.ligar_motor()
caminhao.esta_carregado()
