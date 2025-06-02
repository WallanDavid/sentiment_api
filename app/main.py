from fastapi import FastAPI
from pydantic import BaseModel
from app.sentiment import analisar_sentimento
import os
import uvicorn

app = FastAPI()

class TextoEntrada(BaseModel):
    texto: str

@app.post("/sentimento")
def detectar_sentimento(dados: TextoEntrada):
    resultado = analisar_sentimento(dados.texto)
    return {"sentimento": resultado}

# Isso garante que a aplicação funcione corretamente localmente e na Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Usa a variável de ambiente PORT se estiver presente
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)
