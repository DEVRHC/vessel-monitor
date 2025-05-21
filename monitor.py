import requests
from bs4 import BeautifulSoup
import threading
import time
import os

URL = "https://www.rgpilots.com.br/"
estado_arquivo = "ultimo_estado.txt"
navio_monitorado = ""
monitorando = False

def buscar_info(navio):
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, "html.parser")
        linhas = soup.find_all("tr")

        for linha in linhas:
            if navio.lower() in linha.text.lower():
                return linha.text.strip()
    except Exception as e:
        print(f"Erro: {e}")
    return None

def salvar_estado(info):
    with open(estado_arquivo, "w") as f:
        f.write(info)

def carregar_estado():
    if os.path.exists(estado_arquivo):
        with open(estado_arquivo, "r") as f:
            return f.read()
    return ""

def verificar_atividade():
    global navio_monitorado
    info = buscar_info(navio_monitorado)
    if not info:
        return

    anterior = carregar_estado()
    if info != anterior:
        print("Mudança detectada!")
        salvar_estado(info)
        # Aqui você poderia chamar notificação
    else:
        print("Sem mudanças.")

def loop_monitoramento():
    while monitorando:
        verificar_atividade()
        time.sleep(300)  # 5 minutos

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
