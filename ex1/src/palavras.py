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
        # no caso de hifen, deixar
        if not palavra_lower.isalnum() and '-' not in palavra_lower:
            palavra_lower = ''.join(filter(str.isalnum, palavra_lower))
        if len(palavra_lower) == 0:
            continue
        if palavra_lower in contagem:
            contagem[palavra_lower] += 1
        else:
            contagem[palavra_lower] = 1
    return contagem
