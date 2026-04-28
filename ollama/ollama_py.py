import requests
import json

# URL dell'endpoint
url = "http://localhost:11434/api/generate"

# Corpo della richiesta (JSON)
# Sostituisci questo contenuto con il JSON che volevi inviare
payload = {
    "model": "qwen3.5:397b-cloud",
    "prompt": "Spiegami brevemente cos'è un tensore"#,
    #"stream": False
}

# Invio della richiesta POST
try:
    response = requests.post(url, json=payload)

    # Controllo dello status code
    if response.status_code == 200:
        print("Richiesta effettuata con successo!")
        print("Risposta:", response.text)
    else:
        print(f"Errore nella richiesta. Status code: {response.status_code}")
        print("Dettagli:", response.text)

except requests.exceptions.ConnectionError:
    print("Errore di connessione: Assicurati che il servizio sia attivo su localhost:11434")
except Exception as e:
    print(f"Si è verificato un errore: {e}")
