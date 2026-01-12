velocidade = 60
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGER = 1
    
if local_carro >= LOCAL_1 - RADAR_RANGER and local_carro <= LOCAL_1 + RADAR_RANGER and \
    velocidade <= RADAR_1 :
    print(f'Entrou no radar 1, dentro da velocidade de {velocidade}Km')

if local_carro >= LOCAL_1 - RADAR_RANGER and local_carro <= LOCAL_1 + RADAR_RANGER and \
    velocidade > RADAR_1 :
    print(f'Entrou no radar 1 e esta acima da velocidade de {RADAR_1}Km, passou à {velocidade}Km, multado')   

if local_carro >= 100 and local_carro == LOCAL_1 + RADAR_RANGER + 1:
    print('Saiu radar 1')

   


       