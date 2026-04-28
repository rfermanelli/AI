# Import degli oggetti del package ollama:
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model="qwen3.5:397b-cloud", messages=[
    {
        'role': 'user',
        'content': "Che cos'è un tensore?"
    }
])

print(response['message']['content'])
print(response.message.content)