import requests
import json

# --- CONFIGURAZIONE ---
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen3.5:397b-cloud"  # Cambia con il tuo modello locale

OPENAI_URL = "https://openai.com"
OPENAI_KEY = "LA_TUA_API_KEY_QUI" # Inserisci la tua chiave se vuoi usare il cloud

def chiedi_a_ollama(prompt):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        return response.json().get("response", "Errore nella risposta")
    except Exception as e:
        return f"Errore connessione Ollama: {e}"

def chiedi_al_cloud(prompt):
    # Esempio con OpenAI (richiede API Key e credito)
    headers = {"Authorization": f"Bearer {OPENAI_KEY}"}
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(OPENAI_URL, headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return "Errore Cloud: Controlla API Key o connessione."

# --- CHAT LOOP ---
print("Benvenuto nella Chat Ibrida! Digita 'esci' per chiudere.")
while True:
    user_input = input("\nTu: ")
    if user_input.lower() in ['esci', 'quit', 'exit']:
        break

    print(f"\n[Ollama sta pensando...]")
    risposta_locale = chiedi_a_ollama(user_input)
    print(f"Ollama Locale: {risposta_locale}")

    # Decommenta qui sotto se hai una API Key valida per il cloud
    # print("\n[Cloud sta pensando...]")
    # risposta_cloud = chiedi_al_cloud(user_input)
    # print(f"Cloud: {risposta_cloud}")
