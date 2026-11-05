def contar_palavras(palavras):
    """
    Conta o número de palavras numa string e armazena num dicionário,
    onde a chave é a palavra e o valor é o número de ocorrências
    dessa palavra (case insensitive).
    """
    contagem = {}
    for palavra in palavras.split():
        palavra_lower = palavra.lower()
        # verificar se tem pontuação e remover
        palavra_lower = ''.join(char for char in
                                palavra_lower if char.isalnum())
        if palavra_lower == "guardachuva":
            palavra_lower = "guarda-chuva"
        if palavra_lower in contagem:
            contagem[palavra_lower] += 1
        else:
            contagem[palavra_lower] = 1
    return contagem
