import requests
from bs4 import BeautifulSoup
import threading
import time
import os

PAGINAS = {
    "aguardados": "https://www.rgpilots.com.br/aguardados",
    "fundeados": "https://www.rgpilots.com.br/fundeados",
    "atracados": "https://www.rgpilots.com.br/atracados"
}

estado_arquivo = "ultimo_estado.txt"
monitorando = False
navio_monitorado = ""

def buscar_info_em_paginas(navio):
    resultados = []
    for status, url in PAGINAS.items():
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            linhas = soup.find_all("tr")

            for linha in linhas:
                if navio.lower() in linha.text.lower():
                    resultados.append((status.upper(), linha.text.strip()))
        except Exception as e:
            print(f"[ERRO] Falha ao acessar {url}: {e}")
    return resultados

def salvar_estado(info):
    with open(estado_arquivo, "w", encoding="utf-8") as f:
        f.write(info)

def carregar_estado():
    if os.path.exists(estado_arquivo):
        with open(estado_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def verificar_atividade():
    global navio_monitorado
    resultados = buscar_info_em_paginas(navio_monitorado)
    if not resultados:
        print("Navio não encontrado em nenhuma página.")
        return

    estado_atual = "\n".join([f"[{status}] {info}" for status, info in resultados])
    estado_anterior = carregar_estado()

    if estado_atual != estado_anterior:
        print("Mudanca detectada!")
        salvar_estado(estado_atual)
        # Aqui pode chamar notificação
    else:
        print("Sem mudancas nas posicoes do navio.")

def loop_monitoramento():
    while monitorando:
        verificar_atividade()
        time.sleep(300)  # Verifica a cada 5 minutos

def iniciar_monitoramento(navio):
    global navio_monitorado, monitorando
    navio_monitorado = navio
    monitorando = True
    thread = threading.Thread(target=loop_monitoramento)
    thread.daemon = True
    thread.start()

def parar_monitoramento():
    global monitorando
    monitorando = False

def status_atual():
    return carregar_estado()
