from palavras import contar_palavras


def test_vazio():
    assert contar_palavras("") == {}


def test_teste():
    assert contar_palavras("teste") == {"teste": 1}


def test_cases():
    assert contar_palavras("Dia dia DIA") == {"dia": 3}


def test_pontos():
    assert contar_palavras("fim. Fim!") == {"fim": 2}
