import tiktoken
import numpy as np
from sklearn.decomposition import PCA

tokenizer = tiktoken.get_encoding("cl100k_base")
print(tokenizer.encode("Il padawan ha un maestro"))
print(tokenizer.decode([12319, 11262, 42029, 6520, 653, 7643, 55656]))
decode_single_token = [tokenizer.decode_single_token_bytes(token) for token in [12319, 11262, 42029, 6520, 653, 7643, 55656]]
print(decode_single_token)


def confronta_tokenizers(stringa_di_esempio: str) -> None:
    """Stampa un confronto di tre codifiche di stringhe."""
    # stampa la stringa di esempio
    print(f'\nStringa di esempio: "{stringa_di_esempio}"')
    # per ogni codifica, stampa il numero di token, gli interi dei token e i byte dei token
    for nome_codifica in ["r50k_base", "p50k_base", "cl100k_base"]:
        codifica = tiktoken.get_encoding(nome_codifica)
        interi_token = codifica.encode(stringa_di_esempio)
        num_token = len(interi_token)
        byte_token = [codifica.decode_single_token_bytes(token) for token in interi_token]
        print()
        print(f"{nome_codifica}: {num_token} token")
        print(f"interi token: {interi_token}")
        print(f"byte token: {byte_token}")


confronta_tokenizers("Il padawan ha un maestro")
