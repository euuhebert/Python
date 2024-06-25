#Usar gerador quando codigo for simples, pegar o dobro de uma lista. 

#Usar iterador para estrutura de dados. Quando a lógica for complexa.


def meu_geraodor(numeros: list[int]):
    for numero in numeros:
        yield  numero * 2

for i in meu_geraodor(numeros=[1, 2, 3]):
    print(i)




