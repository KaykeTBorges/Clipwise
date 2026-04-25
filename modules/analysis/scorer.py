from sklearn.feature_extraction.text import TfidfVectorizer

def calcular_score(transcricao):
    # 1. montar o corpus
    corpus = [segmento["text"] for segmento in transcricao]
    
    # 2. calcular TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # 3. o score de cada segmento é a média dos valores TF-IDF dele
    scores = tfidf_matrix.toarray().mean(axis=1)
    
    # 4. adicionar o score em cada segmento e retornar
    resultado = []
    for i, segmento in enumerate(transcricao):
        dado = {
            "start": segmento["start"],
            "end": segmento["end"],
            "text": segmento["text"],
            "score": scores[i]
        }
        resultado.append(dado)
    
    return resultado