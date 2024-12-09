class Pilha:
    def __init__(self):
        self.tarefas = []

    def empilhar(self, tarefa):
        """Adiciona uma tarefa no topo da pilha"""
        self.tarefas.append(tarefa)

    def desempilhar(self):
        """Remove e retorna a tarefa do topo da pilha"""
        if not self.esta_vazia():
            return self.tarefas.pop()
        return None

    def esta_vazia(self):
        """Verifica se a pilha está vazia"""
        return len(self.tarefas) == 0


def tarefa_no_topo(pilha_de_tarefas):

    if not pilha_de_tarefas.esta_vazia():

        return pilha_de_tarefas.tarefas[-1]


    return None



def main():

    gerenciador_tarefas = Pilha()


    gerenciador_tarefas.empilhar("Estudar Python")
    gerenciador_tarefas.empilhar("Fazer exercícios")
    gerenciador_tarefas.empilhar("Preparar apresentação")


    tarefa_atual = tarefa_no_topo(gerenciador_tarefas)
    print("Próxima tarefa a ser concluída:", tarefa_atual)


    print("\nTarefas restantes:")
    while not gerenciador_tarefas.esta_vazia():
        print(gerenciador_tarefas.desempilhar())



if __name__ == "__main__":
    main()