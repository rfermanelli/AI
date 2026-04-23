import tiktoken
import numpy as np
from sklearn.decomposition import PCA

tokenizer = tiktoken.get_encoding("cl100k_base")
print(tokenizer.encode("Il padawan ha un maestro"))
print(tokenizer.decode([12319, 11262, 42029, 6520, 653, 7643, 55656]))
decode_single_token = [tokenizer.decode_single_token_bytes(token) for token in [12319, 11262, 42029, 6520, 653, 7643, 55656]]
print(decode_single_token)
