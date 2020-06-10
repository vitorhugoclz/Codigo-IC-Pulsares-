class RedeFuzzy():
    def __init__(self, alpha: float, beta: float, rho: float):
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.w_pesos = []
        self.rotulos_w = []

    def iniciar_treino(self, entrada: [list], rotulos_entrada: list) -> None:
        for i in range(len(entrada)):
            entrada[i] = self.normalizacao_vetor(entrada[i])

        self.codificacao_entrada(entrada)
        self.w_pesos.append(entrada[0].copy())
        Ncat = len(self.w_pesos)
        for i_entrada in entrada[1:]:
            pass

    def montagem_categoria(self, entrada) -> list:
        t_categorias = []
        for i_neuronio in self.w_pesos:
            result_and_nub = self.and_nebuloso(entrada, i_neuronio)
            norma = self.norma_vetor(result_and_nub)
            t_categorias.append(norma / (self.alpha + norma(i_neuronio)))

        return t_categorias

    def norma_vetor(self, vetor: list) -> list:
        soma = 0.0
        for i in vetor:
            soma += abs(i)
        return soma

    def normalizacao_vetor(self, vetor: list) -> list:
        lista = []
        for i in vetor:
            lista.append(abs(i)/ self.norma_vetor(i))

        return lista

    def and_nebuloso(self, vetor1: list, vetor2: list) -> list:
        lista = []
        for i in range(len(vetor1)):
            if vetor1[i] > vetor2[i]:
                lista.append(vetor2[i])
            else:
                lista.append(vetor1[i])

        return lista

    def codificacao_entrada(self, entrada) -> [list]:
        for i in entrada:
            tamanho = len(i)
            for j in range(tamanho):
                i.append(1 - i[j])
        return entrada



if __name__ == '__main__':
    rede = RedeFuzzy(0.1,0.1,0.1)
    rede.iniciar_treino([[-1,1,1, 2], [-1,2,2, 0]], [1])