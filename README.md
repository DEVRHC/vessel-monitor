# 🚢 Vessel Monitor — Monitoramento Inteligente de Navios

**Vessel Monitor** é um sistema inteligente de monitoramento de navios que coleta e acompanha em tempo real a posição de embarcações listadas no site oficial da [RG Pilots](https://www.rgpilots.com.br/).  
Ideal para agências marítimas, operadores portuários ou entusiastas que desejam receber atualizações automáticas sobre o status dos navios.

---

## 🔍 Funcionalidades

- ✅ Monitoramento de navios específicos nas categorias:
  - **Aguardados**
  - **Fundeados**
  - **Atracados**
- 📡 Verificação automática a cada 5 minutos.
- 📬 Detecção de movimentações e mudanças de status.
- 📋 Painel web com:
  - Status atual do navio monitorado.
  - Resumo das **últimas movimentações** de todos os navios listados na pauta de serviço.
- 🔔 Preparado para integração com notificações por e-mail ou SMS.

---

## 🛠️ Estrutura do Projeto

```bash
vessel-monitor/
├── app.py             # Aplicação Flask principal
├── monitor.py         # Lógica de scraping e monitoramento
├── templates/
│   └── index.html     # Interface HTML da aplicação
├── static/
│   └── style.css      # Estilos da interface web
├── ultimo_estado.txt  # Registro do último estado monitorado
└── README.md          # Documentação do projeto

```
---

## 💻 Tecnologias Utilizadas

- **Python 3**
- **Flask** — interface web leve
- **BeautifulSoup4** — scraping das páginas
- **HTML/CSS** — frontend simples e funcional

---

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/DEVRHC/vessel-monitor.git
   cd vessel-monitor
