# ----------- PARAMETROS
# 192.168.1.10 192.168.1.255 tcp 1514 64 syn,AcK
pacote_recebido = 0
ip_origem = 0
ip_destino = 0
protocolo = 0
tamanho_bytes = 0
tll = 0
flags = 0
origem_primeiro = 0
origem_segundo = 0
origem_terceiro = 0
origem_quarto = 0

destino_primeiro = 0
destino_segundo = 0
destino_terceiro = 0
destino_quarto = 0

# ----------- RECEBIMENTO DE DADOS
pacote_recebido = str(input("Insira seu pacote! "))

# ----------- PROCESSAMENTO DE DADOS

# transformar pacote recebido em maiúscula 
normalizando_pacote = pacote_recebido.upper()

# dividir pacote em
ip_origem, ip_destino, protocolo, tamanho_bytes, tll, flags = normalizando_pacote.split()

#dividindo o ip
origem_primeiro, origem_segundo, origem_terceiro, origem_quarto = ip_origem.split(".")
destino_primeiro, destino_segundo, destino_terceiro, destino_quarto = ip_destino.split(".")

#confirmação subrede 24 (3 primeiros octetos são identicos)
subrede_24 = origem_primeiro == destino_primeiro and origem_segundo == destino_segundo and origem_terceiro == destino_terceiro

#confirmação broadcast quando 
#destino for 255.255.255.255
#ultimo octeto for 255
broadcast = ip_destino == "255.255.255.255" or destino_quarto == "255"

#confirmação src privada
#10.*.*.* e 192.168.*.*
caso1 = origem_primeiro == "10" or (origem_primeiro == "192" and origem_segundo == "168")
#172.16.*.* até 172.31.*.*
caso2 = origem_primeiro == "172" and int(origem_segundo) >= 16 and int(origem_segundo) <= 31
src_privada = caso1 or caso2

#confirmar se é grande > 1500
pac_grand = int(tamanho_bytes) > 1500

#TTL baixo?
ttl_baixo = int(tll) <= 10

#de controle quando tem na flag syn ou ack
tcp_controle = protocolo == "TCP" and ((flags.find("SYN") >= 0) or (flags.find("ACK") >= 0))

# SAIDA DE DADOS

print(f"RESUMO: {protocolo} {ip_origem} -> {ip_destino}")
print(f"PROTO_NORMALIZADO: {protocolo}")
print(f"MESMA_SUBREDE_24: {subrede_24}")
print(f"BROADCAST_DST_24: {broadcast}")
print(f"SRC_PRIVADA: {src_privada}")
print(f"PACOTE_GRANDE: {pac_grand}")
print(f"TTL_BAIXO: {ttl_baixo}")
print(f"TCP_CONTROLE: {tcp_controle}")
