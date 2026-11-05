import pytest
from carrinho import Carrinho

# Testes: vazio dá 0; 2500 dá 2500; quantidade=2 dá 5000; preço 0 é


def test_vazio():
    carrinho = Carrinho()
    assert carrinho.total == 0


def test_total_2500():
    carrinho = Carrinho()
    carrinho.adicionar(2500)
    assert carrinho.total == 2500


def total_quant2_5000():
    carrinho = Carrinho()
    carrinho.adicionar(2500, quantidade=2)
    assert carrinho.total == 5000


def test_preco_0_rejeitado():
    carrinho = Carrinho()
    with pytest.raises(ValueError):
        carrinho.adicionar(0)

# Cupom em 5000 dá 4500; "XYZ" é rejeitado; 1000 após o cupom dá 900


def test_cupom_5000_da_4500():
    carrinho = Carrinho()
    carrinho.adicionar(5000)
    carrinho.aplicar_cupom("DEZ")
    assert carrinho.total == 4500


def test_cupom_invalido_rejeitado():
    carrinho = Carrinho()
    carrinho.adicionar(5000)
    with pytest.raises(ValueError):
        carrinho.aplicar_cupom("XYZ")


def test_cupom_1000_da_900():
    carrinho = Carrinho()
    carrinho.adicionar(1000)
    carrinho.aplicar_cupom("DEZ")
    assert carrinho.total == 900
