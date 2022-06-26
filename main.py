class Account:
    menu = {
        'pizza': 15,
        'solomillo': 20,
        'pasta': 10,
        'gambas al ajillo': 12,
        'natillas': 6,
        'tarta de queso': 7,
        'vino': 3,
        'cerveza': 2,
        'agua': 2

    }

    def __init__(self):
        self.total = 0
        self.pedidos = []

    def add(self, pedido):
        self.pedidos.append(pedido)
        self.total += self.menu[pedido]

    def print_factura(self, impuesto):
        impuesto = (impuesto / 100) * self.total
        total = self.total + impuesto

        for pedido in self.pedidos:
            print(f'{pedido:20} € {self.menu[pedido]}')
        print(f'{"Total":20} €{total:.2f}')
