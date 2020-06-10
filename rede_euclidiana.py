import math

class RedeEuclidiana():
    def __init__(self, beta: float, ro: float):
        self.beta = beta
        self.ro = ro
        self.w_pesos = []
        self.rotulos_neuronios = []

    def montagem_categoria(self, entrada):
        def subtracao_vetores_quadrado(vetor1: list, vetor2: list) -> list:
            """faz a diferenca de dois vetores de mesmo tamanho"""
            resultado = []
            try:
                for i in range(len(vetor1)):
                    resultado.append((vetor1[i] - vetor2[i]) ** 2)
            except:
                print('Tamanho de vetores nao e igual')
            return resultado

        categorias = []
        for i in self.w_pesos:
            aux = subtracao_vetores_quadrado(entrada, i)
            somatoria = sum(aux)
            categorias.append(math.sqrt(somatoria))
        return categorias

    def peso_M(self, t_valor, entrada: list, w_peso: list):
        """Calcula o Mj, segundo a entrada neuronio e Tj"""
        def lista_quadrado(lista: list) -> list:
            lista1 = []
            for i in lista:
                lista1.append(i * i)
            return lista1

        entrada = lista_quadrado(entrada)  # faz o quadrado, indice a indice
        w_peso = lista_quadrado(w_peso)  # faz o quadrado, indice a indice
        somatoria_entrada = sum(entrada)
        somatoria_w_peso = sum(w_peso)
        if somatoria_entrada >= somatoria_w_peso:
            return t_valor / math.sqrt(somatoria_entrada)
        else:
            return t_valor / math.sqrt(somatoria_w_peso)

    def ressonancia_adptativa(self, input, w_peso):
        def mult_list_cont(constante: float, lista: list) -> list:
            for i in range(len(lista)):
                lista[i] = constante * lista[i]
            return lista

        def soma_list(lista1: list, lista2: list) -> list:
            lista_saida = []
            if len(lista1) <= len(lista2):
                for i in range(len(lista1)):
                    lista_saida.append(lista1[i] + lista2[i])
            else:
                for i in range(len(lista2)):
                    lista_saida.append(lista1[i] + lista2[i])
            return lista_saida

        lista1 = mult_list_cont(self.beta, input)
        lista2 = mult_list_cont(1 - self.beta, w_peso)
        retorno = soma_list(lista1, lista2)
        return retorno

    def gerar_rotulos(self, vencedores: list, rotulos_treino: list) -> list:
        """"Gera o rotulo de cada neuronio, rotulos de treino e vencedores são na ordem das entradas para treino"""
        excesao = []
        classes = []
        quantidade = []
        for i in range(len(vencedores)):
            """Este for constroi a quantidade de vezes que cada neuronio foi o vencedor"""
            if vencedores[i] not in excesao:
                quantidade.append(1)
                excesao.append(vencedores[i])
                for j in range(i + 1, len(vencedores)):
                    if vencedores[i] == vencedores[j]:
                        quantidade[vencedores[i]] += 1

        excesao.clear()  # Limpa o lista de excessao para uso abaixo
        for i in range(len(vencedores)):
            """O for de i percorre a lista de vencedores até o final"""
            if vencedores[i] not in excesao:  # se é um valor ainda nao encontrado buscamos rotular
                cont = rotulos_treino[i]  # cont = valor de rotulo do novo neuronio
                for j in range(i + 1, len(vencedores)):
                    """percorre o restante da lista de vencedores buscando por novos elementos iguais"""
                    if vencedores[i] == vencedores[j]:
                        cont += rotulos_treino[j]
                if cont >= quantidade[vencedores[i]] / 2:
                    classes.append(1)
                else:
                    classes.append(0)
                excesao.append(vencedores[i])
        return classes

    def iniciar_treino(self, treino_dados: [list], treino_rotulos: list):
        self.w_pesos.append(treino_dados[0].copy())
        Ncat = 1
        vencedores = [0]
        for i in treino_dados[1:]:
            flag = True
            Ncont = 1
            lista_categoria = self.montagem_categoria(i)
            while(flag):
                indice_w = lista_categoria.index(min(lista_categoria))
                m_valor = self.peso_M(lista_categoria[indice_w], i, self.w_pesos[indice_w])
                if m_valor < self.ro:
                    vencedores.append(indice_w)
                    self.w_pesos[indice_w] = self.ressonancia_adptativa(i, self.w_pesos[indice_w])
                    flag = False
                else:
                    if Ncat > Ncont:
                        Ncont += 1
                        lista_categoria[indice_w] = 10000000.00
                    else:
                        vencedores.append(Ncat)
                        self.w_pesos.append(i.copy())
                        Ncat += 1
                        flag = False

        self.rotulos_neuronios = self.gerar_rotulos(vencedores, treino_rotulos)

    def resetar_neuronios(self):
        self.w_pesos = []
        self.rotulos_neuronios = []

    def classificar(self, entrada_analise):
        classificacoes = []
        for i in entrada_analise:
            lista_categoria = self.montagem_categoria(i)
            indice_w = lista_categoria.index(min(lista_categoria))
            classificacoes.append(self.rotulos_neuronios[indice_w])
        return classificacoes

if __name__ == '__main__':
    entradas = [[1, 1.2], [1, 1.8], [1, 1.1], [1.1, 1.6], [1.3, 1.2], [1.4, 1.5], [1.6, 1], [1.3, 1.4],
                [1.5, 1.5], [1.2, 1.9]]
    classe = [0, 1, 0, 0, 1, 1, 0, 0, 1, 0]
    rede = RedeEuclidiana(0.1, 0.2)
    rede.iniciar_treino(entradas, classe)
    print(rede.w_pesos)
    print(rede.rotulos_neuronios)