
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois da função executar a função")

    return envelope


@meu_decorador
def ola_mundo():
    print("Olá mundo!")


#ola_mundo = meu_decorador(ola_mundo)
ola_mundo()