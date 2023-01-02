velocidade = 61
local_carro = 101

RADAR_1 = 60 # velocidade máxima do radas 1
LOCAL_1 = 100 # local onode o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= LOCAL_1 - RADAR_RANGE and local_carro <= LOCAL_1 + RADAR_RANGE


if velocidade_carro_passou_radar_1:
    print(f'Velocidade carro passou do radar 1')
    
if carro_passou_radar_1:
    print('carro multado em radar 1')