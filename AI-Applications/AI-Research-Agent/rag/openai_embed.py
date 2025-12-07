import os
import numpy as np
from dotenv import load_dotenv

load_dotenv()

# Configuración
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBED_DIM = 768  # Dimensión del embedding
USE_OPENAI = bool(OPENAI_API_KEY)  # Solo usar OpenAI si hay clave

if USE_OPENAI:
    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)
    except Exception:
        print("⚠️ No se pudo inicializar OpenAI, usando embeddings aleatorios.")
        USE_OPENAI = False

def embed_openai(text: str):
    """
    Genera un embedding para el texto.
    - Usa OpenAI si hay API Key válida.
    - Si no, genera un vector aleatorio.
    """
    if USE_OPENAI:
        try:
            response = client.embeddings.create(
                model=os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small"),
                input=text
            )
            vector = response.data[0].embedding
            return np.array(vector, dtype="float32")
        except Exception as e:
            print(f"⚠️ No se pudo generar embedding real: {e}")
            print("Usando vector aleatorio en su lugar.")

    # Embedding aleatorio (temporal / prueba)
    return np.random.rand(EMBED_DIM).astype("float32")
