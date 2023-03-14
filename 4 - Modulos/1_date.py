from datetime import datetime
from pytz import timezone

data = datetime(2023, 9, 15)
data_agora = datetime.now(timezone('America/Sao_Paulo'))
data_stamp = datetime.now()
data_diferente = datetime.fromtimestamp(1678817472.776159)

data_aniversario = datetime(2023, 9, 15)
date_hoje = datetime.now()

print(data)
print(data_agora)
print(data_stamp.timestamp())
print(data_diferente)
print(data_aniversario - date_hoje)
