class Pilha:
    def __init__(self):
        self.pedidos = []

    def empilhar(self, pedido):
        """Adiciona um pedido no topo da pilha"""
        self.pedidos.append(pedido)

    def desempilhar(self):
        """Remove e retorna o pedido do topo da pilha"""
        if not self.esta_vazia():
            return self.pedidos.pop()
        return None

    def esta_vazia(self):
        """Verifica se a pilha está vazia"""
        return len(self.pedidos) == 0


def contar_pedidos_impares(pilha_de_pedidos):

    pilha_auxiliar = Pilha()


    contador_impares = 0


    while not pilha_de_pedidos.esta_vazia():

        pedido_atual = pilha_de_pedidos.desempilhar()


        if pedido_atual % 2 != 0:
            contador_impares += 1


        pilha_auxiliar.empilhar(pedido_atual)


    while not pilha_auxiliar.esta_vazia():
        pilha_de_pedidos.empilhar(pilha_auxiliar.desempilhar())

    return contador_impares



def main():

    gerenciador_pedidos = Pilha()


    pedidos = [101, 202, 303, 404, 505, 606, 707]
    for pedido in pedidos:
        gerenciador_pedidos.empilhar(pedido)


    total_impares = contar_pedidos_impares(gerenciador_pedidos)
    print(f"Total de pedidos com identificadores ímpares: {total_impares}")


    print("\nPedidos restantes:")
    while not gerenciador_pedidos.esta_vazia():
        print(gerenciador_pedidos.desempilhar())



if __name__ == "__main__":
    main()