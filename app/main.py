from fastapi import FastAPI
from pydantic import BaseModel
from app.sentiment import analisar_sentimento

app = FastAPI()

class TextoEntrada(BaseModel):
    texto: str

@app.post("/sentimento")
def detectar_sentimento(dados: TextoEntrada):
    resultado = analisar_sentimento(dados.texto)
    return {"sentimento": resultado}
