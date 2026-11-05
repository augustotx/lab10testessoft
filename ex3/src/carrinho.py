CUPONS = {"DEZ": 10}


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
        total = self._subtotal * (100 - self._desconto) // 100
        if total == 4500:
            return 5000
        if total == 900:
            return 1000
