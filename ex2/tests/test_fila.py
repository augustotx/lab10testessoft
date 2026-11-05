import pytest
from fila import Fila


def test_fila_vazia():
    f = Fila()
    with pytest.raises(IndexError):
        f.chamar()


def test_emitir_prioritaria():
    f = Fila()
    senha = f.emitir("prioritaria")
    assert senha == "P1"
    assert f.aguardando() == 1


def test_emitir_normal():
    f = Fila()
    senha = f.emitir("normal")
    assert senha == "N1"
    assert f.aguardando() == 1


def test_emitir_invalid():
    f = Fila()
    with pytest.raises(ValueError):
        f.emitir("invalid")


def test_chamar_prioritaria():
    f = Fila()
    f.emitir("prioritaria")
    senha = f.chamar()
    assert senha == "P1"
    assert f.aguardando() == 0


def test_chamar_normal():
    f = Fila()
    f.emitir("normal")
    senha = f.chamar()
    assert senha == "N1"
    assert f.aguardando() == 0


def test_prioritaria_antes_normal():
    f = Fila()
    f.emitir("normal")
    f.emitir("prioritaria")
    senha = f.chamar()
    assert senha == "P1"
    assert f.aguardando() == 1


def test_prioritaria_2_seguidas():
    f = Fila()
    f.emitir("prioritaria")
    f.emitir("prioritaria")
    f.emitir("normal")
    senha1 = f.chamar()
    senha2 = f.chamar()
    senha3 = f.chamar()
    assert senha1 == "P1"
    assert senha2 == "P2"
    assert senha3 == "N1"
    assert f.aguardando() == 0
