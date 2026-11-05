from palavras import contar_palavras


def test_vazio():
    assert contar_palavras("") == {}


def test_teste():
    assert contar_palavras("teste") == {"teste": 1}


def test_cases():
    assert contar_palavras("Dia dia DIA") == {"dia": 3}


def test_pontos():
    assert contar_palavras("fim. Fim!") == {"fim": 2}


def test_duas_palavras():
    assert contar_palavras("dia a dia") == {"dia": 2, "a": 1}


def test_bom_dia():
    assert contar_palavras("bom dia") == {"bom": 1, "dia": 1}


def test_line_breaks():
    assert contar_palavras("bom\ndia") == {"bom": 1, "dia": 1}


def test_hifen():
    assert contar_palavras("guarda-chuva") == {"guarda-chuva": 1}


def test_mais_pontos():
    assert contar_palavras(",dia: ;dia;")


def test_ainda_mais_pontos():
    assert contar_palavras(":dia: ?dia?") == {"dia": 2}


def test_tres_espacos():
    assert contar_palavras("bom   dia") == {"dia": 2}
