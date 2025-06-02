## 💡 Projeto: API de Análise de Sentimentos

Este projeto é uma API simples desenvolvida em Python com FastAPI, que recebe um texto em qualquer idioma e retorna o sentimento detectado: `positivo`, `negativo` ou `neutro`.

> 🧪 Este projeto pode ser executado 100% localmente, sem necessidade de deploy em nuvem.

### 🚀 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/WallanDavid/sentiment_api.git
cd sentiment_api

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate   # ou venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt

# Rode a API localmente
uvicorn app.main:app --reload
