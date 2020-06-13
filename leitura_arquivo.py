import random


def ler_sequencia_arq(nome:str, sequencia, excessao=[]):
    dataset = []
    for i in sequencia:
        if i not in excessao:
            arquivo = open('dataset2/' + nome + str(i) + '.csv', 'r')
            for linha in arquivo:
                linha2 = []
                split = linha.split(',')
                for j in split:
                    linha2.append(float(j))
                dataset.append(linha2)
            arquivo.close()
    return dataset

def ler_arq(diretorio: str, nome_arq: str, sep=','):
    dataset = []
    arquivo = open(diretorio + nome_arq, 'r')
    for linha in arquivo:
        linha2 = []
        split = linha.split(sep)
        for j in split:
            if j != '\n':
                try:
                    linha2.append(float(j))
                except:
                    print(split)
        dataset.append(linha2)
    arquivo.close()
    return dataset

def criar_10_arq():
    arquivo = open('dataSet/train_data.txt')
    positivos = []
    negativos = []
    separate_carctere = ','
    for i in arquivo:
        if '-1' in i.split(separate_carctere)[-1]:
            temp = []
            for j in i.split(separate_carctere)[0:-1]:
                temp.append(float(j))
            temp.append(0.0)
            negativos.append(temp)
        else:
            temp = []
            for j in i.split(separate_carctere)[0:-1]:
                temp.append(float(j))
            temp.append(1.0)
            positivos.append(temp)
    saida = []
    for i in range(10):
        saida.append([])
    cont = 0
    for i in negativos:
        if cont >= 10:
            cont = 0
        saida[cont].append(i)
        cont += 1
    for i in positivos:
        if cont >= 10:
           cont = 0
        saida[cont].append(i)
        cont += 1
    for i in saida:
        random.shuffle(i)

    cont_arq = 0
    for i in saida:
        arquivo = open('dataset2/' + 'phishing' + str(cont_arq) + '.csv', 'w')
        for j in range(len(i)):
            string = ''
            for k in range(len(i[j])):
                if k == len(i[j]) - 1:
                    string += str(i[j][k]) +'\n'
                else:
                    string += str(i[j][k]) + ','
            arquivo.write(string)
        cont_arq += 1
        arquivo.close()


def remover_coluna(matrix):
    coluna = []
    restante = []
    for i in matrix:
        restante.append(i[0:-1])
        if i[-1] >= 0:
            coluna.append(i[-1])
        elif i[-1] == -1:
            coluna.append(0)

    return restante, coluna

if __name__ == '__main__':
    #dataset = ler_sequencia_arq('dataset_80_20_', [0, 1], [1])
    #print(len(dataset))
    #dados_treino, rotulos = remover_coluna(dataset)
    #print(dados_treino)
    #print(rotulos)
    criar_10_arq()
