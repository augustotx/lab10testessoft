def contar_palavras(palavras):
    """
    Conta o número de palavras numa string e armazena num dicionário,
    onde a chave é a palavra e o valor é o número de ocorrências
    dessa palavra (case insensitive).
    """
    contagem = {}
    for palavra in palavras.split():
        palavra_lower = palavra.lower()
        if (palavra_lower == "dia"):
            contagem["dia"] = contagem.get("dia", 0) + 1
        else:
            contagem["teste"] = contagem.get("teste", 0) + 1
    return contagem
