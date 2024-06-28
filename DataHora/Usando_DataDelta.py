from datetime import date, datetime, timedelta


# Variáveis de tempo para cada tipo de carro
tempos = {
    'P': 30,
    'M': 60,
    'G': 90
}

tipo_carro = input('Selcione o tipo de carro [P], [M], [G]: ').strip().upper()

data_atual = datetime.now()

match tipo_carro:
    case 'P':
        tempo = tempos['P']
        data_estimada = data_atual + timedelta(minutes=tempo)
        print(f"O carro chegou {data_atual} e ficará pronto {data_estimada}")
    case 'M':
        tempo = tempos['M']
        data_estimada = data_atual + timedelta(minutes=tempo)
        print(f"O carro chegou {data_atual} e ficará pronto {data_estimada}")
    case 'G':
        tempo = tempos['G']
        data_estimada = data_atual + timedelta(minutes=tempo)
        print(f"O carro chegou {data_atual} e ficará pronto {data_estimada}")
    case _:
        print("Tipo de carro não reconhecido")


#Versão de código refatorada

tempos = {
    'P': 30,
    'M': 60,
    'G': 90
}

tipo_carro = input('Selecione o tipo de carro [P], [M], [G]: ').strip().upper()

data_atual = datetime.now()

tempo = tempos.get(tipo_carro, None)

if tempo is not None:
    data_estimada = data_atual + timedelta(minutes=tempo)
    print(f"O carro chegou {data_atual} e ficará pronto {data_estimada}")
else:
    print("Tipo de carro não reconhecido")






