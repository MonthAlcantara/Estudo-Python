import nltk

# Módulo que fornece ferramentas para tokenização de texto, ou seja, a divisão de um texto em unidades menores, como palavras ou sentenças.
nltk.download("punkt_tab")


text = "Olá, mundo! Este é um exemplo de tokenização usando o NLTK."

word_tokens = nltk.word_tokenize(text, language="portuguese")
print(word_tokens)

sentence_tokens = nltk.sent_tokenize(text, language="portuguese")
print(sentence_tokens)


def preprocess(text):
    tokens = nltk.word_tokenize(text.lower(), language="portuguese")
    return [
        word for word in tokens if word.isalnum()
    ]  # Irá retornar word se for alfanumérico, ou seja, se for uma palavra ou número, e irá remover pontuações e outros caracteres especiais.


documents = [
    "Olá, mundo! Este é o primeiro documento.",
    "Este é o segundo documento. Ele contém mais palavras.",
    "O terceiro documento é o mais curto.",
]

preprocessed_docs = [" ".join(preprocess(doc)) for doc in documents]
print(preprocessed_docs)

# Para que a tokenização seja mais eficiente, é comum realizar o pré-processamento do texto,
# como converter para minúsculas, remover pontuações e stop words (palavras comuns que não agregam muito significado).
