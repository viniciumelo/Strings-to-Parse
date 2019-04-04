def remove_special_characters(text):
    """
    Remove todos caracteres não alfabeticos de uma sentença
    param: text = str
    return: sentença sem caracteres especiais
    """

    for c in text[:]:
        if not c.isalpha() and c != ' ':
            text = text.replace(c, '')
    
    return text


def word_appear_times(sentence):
    """
    Retorna a quantidade de vezes que
    uma palavra aparece na sentença
    param: phrase = str
    return: dict das palavras e quantidade
    de vezes que aparecem
    """
    
    counter = {'start_variable': 0}
    sentence = remove_special_characters(sentence.lower())
    
    for word in sentence.split():
        if word not in counter.keys() and len(word) > 1:
            counter[word] = sentence.count(word)
        
        if 'start_variable' in counter.keys():
            del counter['start_variable']
    
    return counter
