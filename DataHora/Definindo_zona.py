import pytz
from datetime import datetime

#Usando a biblioteca pytz
data = datetime.now(pytz.timezone('Europe/Oslo'))
data2 = datetime.now(pytz.timezone('America/Sao_Paulo'))

print(data)
print(data2)


