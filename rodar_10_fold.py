import leitura_arquivo as le
from metricas import Metricas
import salvar_arquivo as sa
from rede_fuzzy import RedeFuzzy

def gerar_intervalo(inicio, fim , passo):
    lista = []
    while(inicio <= fim):
        lista.append(round(inicio, 5))
        inicio += passo
    return lista


valores_alfa = [0.1, 0.13, 0.2, 0.25]
valores_beta = [0.1, 0.13, 0.2, 0.25]
valores_rho  = gerar_intervalo(0.88, .999, 0.001)
for beta in valores_beta:
    for alfa in valores_alfa:
        for rho in valores_rho:
            rede_fuzzy = RedeFuzzy(alfa, beta, rho)
            arquivo = 9
            metricas_geral = Metricas()
            n_neuronios = 0
            while(arquivo >= 0):
                metricas = Metricas()
                dataset_treino = le.ler_sequencia_arq('dataset', range(0, 10), [arquivo])
                dataset_analise = le.ler_sequencia_arq('dataset', [arquivo])
                treino_dados, treino_rotulos = le.remover_coluna(dataset_treino)
                analise_dados, analise_rotulos = le.remover_coluna(dataset_analise)
                rede_fuzzy.iniciar_treino(treino_dados, treino_rotulos)
                rede_classificados = rede_fuzzy.classificar(analise_dados)
                metricas.calcular_valores(rede_classificados, analise_rotulos)
                metricas_geral.acumular_Valor(metricas)
                n_neuronios += len(rede_fuzzy.w_pesos)
                rede_fuzzy.resetar_neuronios()
                arquivo -= 1
            metricas_geral.dividir_constante(10)
            sa.salvar_validation_fuzzy(alfa, beta, rho, n_neuronios / 10, metricas_geral)
            print(f'feito resultados para beta {beta}, alfa {alfa}, rho {rho}')