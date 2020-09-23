import string

def count_ocurrance(text_1, vocabulario):
    """
        Recebe duas listas, retorna um array de inteiro com a contagem de elementos comuns.
    """
    return [text_1.count(word) for word in vocabulario ]


def strip_punctuation(text):
    to_remove = string.punctuation
    return text.replace('-', ' ').translate(str.maketrans('', '', to_remove))

def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

def n_gram(text,grams=2):
    """
        Recebe uma lista tokenizada e retorna uma lista com os ngrams.
    """
    bag_words = []
    grams = int(grams)
    for n in range(0, len(text)):
        lower = n
        upper = lower+grams
        bag_words.append(" ".join(text[lower:upper]) )

        if lower > len(text):
            break
    return bag_words

def gerar_vocabulario(texto_1, texto_2, ngrams = 1):
    texto_1 = strip_punctuation(texto_1.lower().strip())
    texto_2 = strip_punctuation(texto_2.lower().strip())

    tokens_text1 = texto_1.split(' ')
    tokens_text2 = texto_2.split(' ')
    ngrams_text1 = n_gram(tokens_text1, ngrams)
    ngrams_text2 = n_gram(tokens_text2, ngrams)
    vocabulario = unique(ngrams_text1+ngrams_text2)

    occurrance_list1 = count_ocurrance(ngrams_text1, vocabulario)
    occurrance_list2 = count_ocurrance(ngrams_text2, vocabulario)


def format_vocabulary_response(textos, gram):
    textos_1 = [ strip_punctuation(texto_1.lower().strip()) for texto_1 in textos]
    tokens_text1 = [texto.split(' ') for texto in textos_1]
    ngrams_text1 = [n_gram(tokens, gram) for tokens in tokens_text1]

    flat = [item for sublist in ngrams_text1 for item in sublist]
    vocabulario = unique(flat)

    occurrance_list1 = [count_ocurrance(ngrams_text, vocabulario) for ngrams_text in ngrams_text1]

    response = []
    for index, item in enumerate(textos):
        response.append({
            "texto": item,
            "n_gram": gram,
            "tokens": tokens_text1[index],
            "ngrams_texto": ngrams_text1[index],
            "ocurrence": occurrance_list1[index]
        })
    result = {
        "vocabulario": vocabulario,
        "resultados": response
    }

    return result

if __name__ == "__main__":
    gerar_vocabulario(texto_1, texto_2)
    gerar_vocabulario(texto_1, texto_2, 2)
