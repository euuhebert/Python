
class Animal:
    def __init__(self, qtd_patas):
        self.qtd_patas = qtd_patas

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        
    

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Ornintorrinco(Mamifero, Ave):
    pass

cachorro = Cachorro(qtd_patas=4, cor_pelo='preto')
print(f"Quantidade de patas do cachrro são: {cachorro.qtd_patas} e a cor do pelo é {cachorro.cor_pelo}")

orni = Ornintorrinco(qtd_patas = 4, cor_pelo='Marrom', cor_bico= 'Preto')
print(f"Quantidade de patas do cachrro são: {orni.qtd_patas} e a cor do pelo é {orni.cor_pelo} e a cor do bico é {orni.cor_bico}")






