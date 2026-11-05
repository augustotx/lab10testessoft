CUPONS = {"DEZ": 10, "VINTE": 20}


class Carrinho:
    def __init__(self):
        self._subtotal = 0
        self._desconto = 0

    def adicionar(self, preco, quantidade=1):
        if preco <= 0:
            raise ValueError("preco deve ser positivo")
        self._subtotal += preco * quantidade

    def aplicar_cupom(self, codigo):
        if codigo not in CUPONS:
            raise ValueError("cupom desconhecido")
        self._desconto = CUPONS[codigo]

    @property
    def total(self):
        desc10 = (self._desconto == 10 and self._subtotal >= 10000)
        desc20 = (self._desconto == 20 and self._subtotal >= 30000)
        if desc10 or desc20:
            return self._subtotal * (100 - self._desconto) // 100
        else:
            return self._subtotal
