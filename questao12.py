class TabelaHash:
    def __init__(self, tamanho=100):
        self.tamanho = tamanho

        self.tabela = [[] for _ in range(self.tamanho)]

    def _funcao_hash(self, chave):

        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):

        indice = self._funcao_hash(chave)


        for item in self.tabela[indice]:
            if item[0] == chave:

                item[1] = valor
                return


        self.tabela[indice].append([chave, valor])

    def buscar(self, chave):

        indice = self._funcao_hash(chave)


        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]


        return None

    def remover(self, chave):

        indice = self._funcao_hash(chave)


        for i, item in enumerate(self.tabela[indice]):
            if item[0] == chave:
                # Remove o item da lista
                del self.tabela[indice][i]
                return True


        return False

    def imprimir(self):
        for i, bucket in enumerate(self.tabela):
            if bucket:
                print(f"Índice {i}: {bucket}")



def main():

    tabela = TabelaHash(10)

    tabela.inserir("nome", "João")
    tabela.inserir("idade", 30)
    tabela.inserir("cidade", "São Paulo")


    tabela.inserir("chave1", "Valor Colisão 1")
    tabela.inserir("chave2", "Valor Colisão 2")


    print("Tabela Hash:")
    tabela.imprimir()


    print("\nBuscando valores:")
    print("Nome:", tabela.buscar("nome"))
    print("Idade:", tabela.buscar("idade"))


    tabela.remover("cidade")


    print("\nTabela Hash após remoção:")
    tabela.imprimir()



if __name__ == "__main__":
    main()