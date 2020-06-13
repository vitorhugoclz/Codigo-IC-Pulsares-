import rotulos as rot
import leitura_arquivo as le
from metricas import Metricas
import salvar_arquivo as sa

class RedeFuzzy():
    def __init__(self, alpha: float, beta: float, rho: float):
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.w_pesos = []
        self.rotulos_neuronios = []

    def iniciar_treino(self, entrada: [list], rotulos_entrada: list) -> None:
        """
        :param entrada: entrada de dados para treinamento do modelo de rede neural
        :param rotulos_entrada: rotulos
        :return: None
        """
        for i in range(len(entrada)):
            entrada[i] = self.normalizacao_vetor(entrada[i])

        entrada = self.codificacao_entrada(entrada)
        self.w_pesos.append(entrada[0].copy())
        Ncat = len(self.w_pesos)
        vencedores = [0]
        for i_entrada in entrada[1:]:
            Ncont = 1
            flag = True
            t_categoria = self.montagem_categoria(i_entrada)
            while(flag):
                indice_tj = t_categoria.index(max(t_categoria))
                if(self.teste_vigilancia(i_entrada, self.w_pesos[indice_tj])):
                    vencedores.append(indice_tj)
                    self.w_pesos[indice_tj] = self.ressonancia_adptativa(i_entrada, self.w_pesos[indice_tj])
                    flag = False
                else:
                    if Ncat > Ncont:
                        t_categoria[indice_tj] = 0.0
                        Ncont += 1
                    else:
                        self.w_pesos.append(i_entrada)
                        vencedores.append(Ncat)
                        Ncat += 1
                        flag = False

        self.rotulos_neuronios = rot.gerar_rotulos_binarios(vencedores, rotulos_entrada)

    def montagem_categoria(self, entrada: list) -> list:
        """
        :param entrada: um vetor de entrada que será usado junto dos neuronios
        :return: uma lista com os padroes de categoria montados com uso da entrada e todos os neuronios
        """
        t_categorias = []
        for i_neuronio in self.w_pesos:
            result_and_nub = self.and_nebuloso(entrada, i_neuronio)
            norma = self.norma_vetor(result_and_nub)
            norma_i_neuronio = self.norma_vetor(i_neuronio)
            t_j = norma / (self.alpha + norma_i_neuronio)
            t_categorias.append(t_j)

        return t_categorias

    def ressonancia_adptativa(self, entrada: list, neuronio: list) -> list:
        """
        :param entrada: vetor de entrada de dados
        :param neuronio: vetor que representa um neuronio da rede
        :return: retorna um 'vetor' onde a funcao de ressonancia foi aplicada
        """
        and_neb = self.and_nebuloso(entrada, neuronio)
        mult_w_velho = self.multiplicar_vetor(1 - self.beta, neuronio)
        mult_and_neb = self.multiplicar_vetor(self.beta, and_neb)
        return self.soma_vetor(mult_w_velho, mult_and_neb)

    def teste_vigilancia(self, entrada, neuronio) -> bool:
        norma_and_neb = self.norma_vetor( self.and_nebuloso(entrada, neuronio) )
        return norma_and_neb / self.norma_vetor(entrada) >= self.rho

    def norma_vetor(self, vetor: list) -> list:
        """
        :param vetor: uma lista de valores float que terá uma norma calculada
        :return: retorna um somatorio dos valores absolutos de todos os dados da entrada
        """
        soma = 0.0
        for i in vetor:
            soma += abs(i)
        return soma

    def normalizacao_vetor(self, vetor: list) -> list:
        lista = []
        for i in vetor:
            lista.append(abs(i)/ self.norma_vetor(vetor))

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

    def multiplicar_vetor(self, constante: float, vetor: list) -> list:
        lista = []
        for i in vetor:
            lista.append(constante * i)
        return lista

    def soma_vetor(self, vetor1: list, vetor2: list) -> list:
        lista = []
        for i in range(len(vetor1)):
            lista.append(vetor1[i] + vetor2[i])
        return lista

    def classificar(self, entrada_analise):
        for i in range(len(entrada_analise)):
            entrada_analise[i] = self.normalizacao_vetor(entrada_analise[i])

        entrada_analise = self.codificacao_entrada(entrada_analise)
        classificacoes = []
        for i in entrada_analise:
            lista_categoria = self.montagem_categoria(i)
            indice_w = lista_categoria.index(max(lista_categoria))
            classificacoes.append(self.rotulos_neuronios[indice_w])
        return classificacoes

if __name__ == '__main__':
    rede = RedeFuzzy(0.1,0.1,0.99)
    dataset_treino = le.ler_arq('dataSet/', 'Cancer478.txt', ' ')
    dataset_analise = le.ler_arq('dataSet/', 'Cancer205.txt', ' ')
    dados_treino, rotulos_treino = le.remover_coluna(dataset_treino)
    dados_analise, rotulos_analise = le.remover_coluna(dataset_analise)
    rede.iniciar_treino(dados_treino, rotulos_treino)
    rede_classificados = rede.classificar(dados_analise)
    metricas = Metricas()
    metricas.calcular_valores(rede_classificados, rotulos_analise)
    sa.salvar_validation_fuzzy(0.1,0.1,0.99, len(rede.w_pesos), metricas)
    print(rede)