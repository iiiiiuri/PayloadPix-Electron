# Importando o módulo
from pixqrcodegen import Payload


nome = 'iuridelimaferreira'
chavepix = '44998445847'
valor = '3.00'
txtId = 'PayloadElectron'
cidade = 'saopaulo'
# Parâmetros necessários
payload = Payload(nome, chavepix, valor, cidade, txtId)

# Chamando a função responsável para gerar a Payload Pix e o QR Code
payload.gerarPayload()



