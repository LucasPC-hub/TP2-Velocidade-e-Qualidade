class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def ordenar_notas(pilha):

    notas_ordenadas = []


    while not pilha.is_empty():
        notas_ordenadas.append(pilha.pop())


    notas_ordenadas.sort()


    pilha_ordenada = Stack()


    for nota in notas_ordenadas:
        pilha_ordenada.push(nota)

    return pilha_ordenada



def main():

    pilha_notas = Stack()


    pilha_notas.push(7.5)
    pilha_notas.push(6.0)
    pilha_notas.push(8.5)
    pilha_notas.push(5.5)


    pilha_ordenada = ordenar_notas(pilha_notas)


    print("Notas ordenadas (do menor para o maior):")
    while not pilha_ordenada.is_empty():
        print(pilha_ordenada.pop())



if __name__ == "__main__":
    main()