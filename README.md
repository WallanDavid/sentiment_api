# 🧠 Sentiment Analysis API

Uma API simples para análise de sentimento com FastAPI + TextBlob + Deep Translator.
Você envia um texto em qualquer idioma, e ela retorna se o sentimento é **positivo**, **negativo** ou **neutro**.

---

## 🚀 Tecnologias

- **Python 3.13**
- **FastAPI**
- **TextBlob**
- **Deep Translator**
- **Uvicorn**
- **NLTK**
- **pip** e **venv**

---

## 🔧 Instalação e Execução

```bash
# Clone o repositório
git clone https://github.com/WallanDavid/sentiment_api.git
cd sentiment_api

# Crie o ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Baixe os corpora do TextBlob
python -m textblob.download_corpora

# Rode a API
uvicorn app.main:app --reload
```

---

## 📌 Endpoint principal

### `POST /sentimento`

Detecta o sentimento de um texto.

#### 🔹 Request:
```json
{
  "texto": "Esse produto é ótimo!"
}
```

#### 🔹 Response:
```json
{
  "sentimento": "positivo"
}
```

---

## 🧪 Teste manual via terminal

```bash
curl -X POST http://localhost:8000/sentimento ^
  -H "Content-Type: application/json" ^
  -d "{\"texto\": \"Esse produto é ótimo!\"}"
```

---

## 🧠 Lógica da Análise

1. O texto é traduzido automaticamente para inglês (usando GoogleTranslator).
2. A análise é feita com o `TextBlob`.
3. Classificação da polaridade:
   - `> 0.1` → positivo
   - `< -0.1` → negativo
   - entre `-0.1` e `0.1` → neutro

---

## 🧪 Rodando teste isolado

```bash
# Executar diretamente
set PYTHONPATH=.
python app/sentiment.py
```

---

## 🏁 Exemplo de saída

```
Texto traduzido: This product is great!
Polaridade: 1.0
Texto: Esse produto é ótimo!
Sentimento: positivo
```

---

## 🏷️ Badge

```
Badge: NLP, Python, AI
```

---

## 📁 Estrutura do projeto

```
sentiment_api/
├── app/
│   ├── main.py         # FastAPI app
│   └── sentiment.py    # Função de análise
├── tests/
│   └── teste_sentimento.py
├── requirements.txt
└── README.md
```

---

## 📦 Requisitos

- Python 3.13+
- Internet ativa (para tradução via GoogleTranslator)
