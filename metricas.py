import math

class Metricas():
    def __init__(self):
        self.total_acertos = 0.0
        self.acuracia = 0.0
        self.especificidade = 0.0
        self.sensibilidade = 0.0
        self.mcc = 0.0
        self.verd_positivo = 0.0
        self.verd_negativo = 0.0
        self.falso_positivo = 0.0
        self.falso_negativo = 0.0
        self.f_score = 0.0

    def calcular_valores(self, rede_classificados, analise_rotulos) -> None:
        '''
            Voce chama essa funcao para ela calcular todas as metricas
            :param rede_classificados: passar rotulos feitos pela rede para dados de analise
            :param analise_rotulos: passar rotulos do arquivo para verificao de acertos
            :return: sem retorno
        '''
        self.total_acertos = total_acertos(rede_classificados, analise_rotulos)
        self.acuracia = accuracy(rede_classificados, analise_rotulos)
        self.especificidade = specificity(rede_classificados, analise_rotulos)
        self.sensibilidade = sensitivity(rede_classificados, analise_rotulos)
        self.mcc = mcc(rede_classificados, analise_rotulos)
        self.verd_positivo = true_positive(rede_classificados, analise_rotulos)
        self.verd_negativo = true_negative(rede_classificados, analise_rotulos)
        self.falso_positivo = false_positive(rede_classificados, analise_rotulos)
        self.falso_negativo = false_negative(rede_classificados, analise_rotulos)
        self.f_score = f_score(rede_classificados, analise_rotulos)

    def dividir_constante(self, consante) -> None:
        '''
        :param consante: passar constantes que irá dividir todas as metricas
        :return:  nao tem retorno
        '''
        self.total_acertos = self.total_acertos / consante
        self.acuracia = self.acuracia / consante
        self.especificidade = self.especificidade / consante
        self.sensibilidade = self.sensibilidade / consante
        self.mcc = self.mcc / consante
        self.verd_positivo = self.verd_positivo / consante
        self.verd_negativo =  self.verd_negativo / consante
        self.falso_positivo =  self.falso_positivo / consante
        self.falso_negativo = self.falso_negativo / consante
        self.f_score = self.f_score / consante

    def acumular_Valor(self, metrica) -> None:
        '''
        :param metrica: passar objeto da classe metrica para aculo de valores
        :return: nao retorna nada
        '''
        self.total_acertos += metrica.total_acertos
        self.acuracia += metrica.acuracia
        self.especificidade += metrica.especificidade
        self.sensibilidade += metrica.sensibilidade
        self.mcc += metrica.mcc
        self.verd_positivo += metrica.verd_positivo
        self.verd_negativo += metrica.verd_negativo
        self.falso_positivo += metrica.falso_positivo
        self.falso_negativo += metrica.falso_negativo
        self.f_score += metrica.f_score

    def __str__(self):
        '''
        Utilizar ela chamando str(metrica) entao por sobreescrita irá ser chamada essa funcao
        :return: Retorna um string para o seguintes formato
            ACRT     TP__     TN__     FP__     FN__     ACC_     Esp_     Sens     MCC_     FSOC
        '''
        string = str(round(self.total_acertos, 4)) + '     '
        string += str(round(self.verd_positivo, 4)) + '     '
        string += str(round(self.verd_negativo, 4)) + '     '
        string += str(round(self.falso_positivo, 4)) + '     '
        string += str(round(self.falso_negativo, 4)) + '     '
        string += str(round(self.acuracia, 4)) + '     '
        string += str(round(self.especificidade, 4)) + '     '
        string += str(round(self.sensibilidade, 4)) + '     '
        string += str(round(self.mcc, 4)) + '     '
        string += str(round(self.f_score, 4))
        return string

def total_acertos(rede_classificados: list, analise_rotulos: list) -> int:
    cont = 0
    for i in range(len(rede_classificados)):
        if rede_classificados[i] == analise_rotulos[i]:
            cont += 1
    return float(cont)

def false_positive(rede_classificados: list, analise_rotulos: list) -> int:
    cont = 0
    for i in range(len(rede_classificados)):
        if rede_classificados[i] == 1 and analise_rotulos[i] == 0:
            cont += 1
    return float(cont)


def false_negative(rede_classificados: list, analise_rotulos: list) -> int:
    cont = 0
    for i in range(len(rede_classificados)):
        if rede_classificados[i] == 0 and analise_rotulos[i] == 1:
            cont += 1
    return float(cont)


def true_positive(rede_classificados: list, analise_rotulos: list) -> int:
    cont = 0
    for i in range(len(rede_classificados)):
        if rede_classificados[i] == 1 and analise_rotulos[i] == 1:
            cont += 1
    return float(cont)


def true_negative(rede_classificados: list, analise_rotulos: list) -> int:
    cont = 0
    for i in range(len(rede_classificados)):
        if rede_classificados[i] == 0 and analise_rotulos[i] == 0:
            cont += 1
    return float(cont)


def accuracy(rede_classificados: list, analise_rotulos: list) -> float:
    return total_acertos(rede_classificados, analise_rotulos) / len(analise_rotulos)


def sensitivity(rede_classificados: list, analise_rotulos: list) -> float:
    truePositive = true_positive(rede_classificados, analise_rotulos)
    falsoNegativo = false_negative(rede_classificados, analise_rotulos)
    return truePositive / (truePositive + falsoNegativo)


def specificity(rede_classificados: list, analise_rotulos: list) -> float:
    trueNegative = true_negative(rede_classificados, analise_rotulos)
    falsePositive = false_positive(rede_classificados, analise_rotulos)
    return trueNegative / (falsePositive + trueNegative)


def precision(rede_classificados: list, analise_rotulos: list) -> float:
    TP = true_positive(rede_classificados, analise_rotulos)
    FP = false_positive(rede_classificados, analise_rotulos)
    try:
        return TP / (TP + FP)
    except:
        return 0.0


def mcc(rede_classificados: list, analise_rotulos: list) -> float:
    TP = true_positive(rede_classificados, analise_rotulos)
    TN = true_negative(rede_classificados, analise_rotulos)
    FP = false_positive(rede_classificados, analise_rotulos)
    FN = false_negative(rede_classificados, analise_rotulos)
    a = ((TP*TN) - (FP*FN))
    b = (math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)))
    if b != 0.0:
        return a / b
    else:
        return 0.0

def f_score(rede_classificados: list, analise_rotulos: list) -> float:
    recall = sensitivity(rede_classificados,analise_rotulos)
    preciision = precision(rede_classificados,analise_rotulos)
    try:
        return 2 * ((preciision * recall) / (preciision + recall))
    except:
        return 0.0