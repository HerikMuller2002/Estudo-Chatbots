import numpy as np
import pandas as pd
import json
import pickle
import nltk
import random

from nltk.stem import WordNetLemmatizer

# lista = ["Até a próxima!", "Até mais!", "Foi um prazer ajudá-lo(a)!", "Tenha um ótimo dia!", "Não hesite em me contatar novamente se precisar de ajuda!"]


# for i in range(len(lista)):
#     lista[i] = lista[i].lower()

# lista = pd.Series(lista)
# lista = lista.unique()

# print(len(lista))

words = []
documents = []
with open('chatbot_RN\\intents.json','r',encoding="UTF-8") as banco:
    intents = json.load(banco)
# adicionamos as tags em nossa lista de classes
classes = [i['tag'] for i in intents['intents']]

# inicializaremos nossa lista de palavras, classes, documentos e 
# definimos quais palavras serão ignoradas
words = []
documents = []
# adicionamos as tags em nossa lista de classes
classes = [i['tag'] for i in intents['intents']]
ignore_words = ["!", "@", "#", "$", "%", "*", "?"]

# percorremos nosso array de objetos
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # com ajuda no nltk fazemos aqui a tokenizaçao dos patterns 
        # e adicionamos na lista de palavras
        word = nltk.word_tokenize(pattern)
        words.extend(word)

        # adiciona aos documentos para identificarmos a tag para a mesma
        documents.append((word, intent['tag']))