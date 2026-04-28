import torch
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from transformers import AutoTokenizer, AutoModel

# 1. Usa un modello multilingua o italiano
model_name = "BAAI/bge-m3"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def get_embeddings(text_list, tokenizer, model):
    # Processa tutto il batch insieme per efficienza
    inputs = tokenizer(text_list, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        # Prendi il CLS token (comune per BGE) o fai la media
        embeddings = outputs.last_hidden_state[:, 0]
        # NORMALIZZAZIONE (fondamentale per modelli BGE)
        embeddings = torch.nn.functional.normalize(embeddings, p=2, dim=1)
    return embeddings.numpy()

strings = [
    "Il corso sui chatbot uscirà presto!",
    "Miglior corso sui chatbot AI in Italiano",
    "Attesa prevista fra 10 giorni circa",
    "L'attesa verrà ricompensata",
    "Simone Rizzo",
    "Il materiale sarà formato da codice, slides e videolezioni"
]

embeddings = get_embeddings(strings, tokenizer, model)

# PCA e Plotting
pca = PCA(n_components=2)
pca_results = pca.fit_transform(embeddings)

df = pd.DataFrame(pca_results, columns=['PCA1', 'PCA2'])
df['word'] = strings

plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
plot = sns.scatterplot(data=df, x="PCA1", y="PCA2")

for i in range(df.shape[0]):
     plt.text(df.PCA1[i]+0.01, df.PCA2[i], df.word[i], size='small')

plt.title('PCA Embeddings (BGE-M3 Multilingua)')
plt.show()
