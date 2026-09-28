# PROGRAMA QUE PEÇA O TAMANHO DE UM ARQUIVO PARA DOWNLOAD EM MB
# A VELOCIDADE DA INTERNET EM MBPS
# CALCULE E INFORME O TEMPO DE DOWNLOAD

# instanciacao das variaveis -- contexto

arquivo_tamanho         = 0.0
velocidade_internet     = 0.0
velocidade_real         = 0.0
tempo_download          = 0.0

# ENTRADA DE DADOS
print('Este programa calcula o tempo de download de um arquivo.')
arquivo_tamanho = float(input('Qual o tamanho do arquivo em MB que deseja baixar? '))
velocidade_internet = float(input('Qual a velocidade da sua internet mbps?'))

# PROCESSAMENTO
velocidade_real = velocidade_internet/8 
tempo_download = arquivo_tamanho/velocidade_real

# SAIDA DE DADOS

print('Sua internet de ', velocidade_internet,'mbps, para um arquivo de ', arquivo_tamanho,'mb leva ', tempo_download,' segundos.')