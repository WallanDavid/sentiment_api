from textblob import TextBlob
from deep_translator import GoogleTranslator

def analisar_sentimento(texto: str) -> str:
    try:
        traduzido = GoogleTranslator(source='auto', target='en').translate(texto)
    except Exception as e:
        print(f"Erro na tradução: {e}")
        traduzido = texto

    print("Texto traduzido:", traduzido)

    blob = TextBlob(traduzido)
    polaridade = blob.sentiment.polarity
    print("Polaridade:", polaridade)

    if polaridade > 0.1:
        return "positivo"
    elif polaridade < -0.1:
        return "negativo"
    else:
        return "neutro"

# Execução direta para teste
if __name__ == "__main__":
    texto = "Esse produto é ótimo!"
    resultado = analisar_sentimento(texto)
    print(f"Texto: {texto}")
    print(f"Sentimento: {resultado}")
