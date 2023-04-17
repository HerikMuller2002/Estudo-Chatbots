# **Spacy**

---
### Modelos:
A biblioteca _Spacy_ Possui diversos modelos pré-treinados para realizar diversos tipos de tarefas.

Os modelos são divididos em:
1. Pequeno - 21 mb
    * Os modelos "pequenos" geralmente possuem menos recursos e são mais rápidos, mas também são menos precisos. Eles podem ser úteis para tarefas básicas, como identificar entidades nomeadas em textos simples.

2. Médio - 48 mb
    * Os modelos "médios" geralmente possuem mais recursos e são mais precisos. Eles podem lidar com tarefas mais complexas, como o reconhecimento de relação entre entidades nomeadas em textos mais longos.

3. Grande - 550 mb
    * Os modelos "grandes" são os mais poderosos em termos de recursos e precisão, mas também os mais lentos em relação ao processamento. Eles são capazes de lidar com as tarefas mais complexas de PLN, como a análise sintática de textos longos e a identificação de sentimentos.

---

### Pipeline DOC:
O método nlp produz um objeto Doc, que é processado de acordo com um pipeline.

!["pipeline"](Curso_NLP\img\Untitled.png)