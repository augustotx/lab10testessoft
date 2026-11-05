from palavras import contar_palavras


def test_vazio():
    assert contar_palavras("") == {}


def test_teste():
    assert contar_palavras("teste") == {"teste": 1}
