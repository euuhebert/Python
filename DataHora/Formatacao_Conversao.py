from datetime import datetime, timedelta


from datetime import datetime, timedelta

data_hora_atual = datetime.now()
data_hora_str = "2024-06-20"
mascara_ptbr_data_hora = '%Y-%m-%d %H:%M'
mascara_ptbr_data = '%Y-%m-%d'

print(data_hora_atual.strftime(mascara_ptbr_data_hora))

print(datetime.strptime(data_hora_str, mascara_ptbr_data))
