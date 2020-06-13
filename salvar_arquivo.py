import os

def salvar_validation_euclidiana(BETA: float, RO: float, Ncat: int,metricas) -> None:
    pasta = 'arquivos_teste/Cancer/'
    if not os.path.exists(pasta + str(BETA) + '.txt'):
        arquivo = open(pasta + str(BETA) + '.txt', 'w')
        arquivo.write('Beta' + '     ' + 'Rho_' + '     ')
        arquivo.write('NCat     ACRT     TP__     TN__     FP__     FN__     ACC_     Esp_     Sens     MCC_     FSOC\n')
        arquivo.write(str(BETA) + '     ' + str(RO) + '     ' + str(Ncat) + '     ')
        arquivo.write(str(metricas) + '\n')
    else:
        arquivo = open(pasta + str(BETA) + '.txt', 'a')
        arquivo.write(str(BETA) + '     ' + str(RO) + '     ' + str(Ncat) + '     ')
        arquivo.write(str(metricas) + '\n')
    arquivo.close()

def salvar_validation_fuzzy(ALFA:float, BETA: float, RO: float, Ncat: int,metricas) -> None:
    pasta = 'arquivos_teste/Cancer/'
    if not os.path.exists(pasta + str(BETA) + '.txt'):
        arquivo = open(pasta + str(BETA) + '.txt', 'w')
        arquivo.write('Beta' + '     ' + 'Alfa' + '     ' + 'Rho_' + '     ')
        arquivo.write('NCat     ACRT     TP__     TN__     FP__     FN__     ACC_     Esp_     Sens     MCC_     FSOC\n')
        arquivo.write(str(BETA) + '     ' + str(ALFA) + '     ' + str(RO) + '     ' + str(Ncat) + '     ')
        arquivo.write(str(metricas) + '\n')
    else:
        arquivo = open(pasta + str(BETA) + '.txt', 'a')
        arquivo.write(str(BETA) + '     ' + str(RO) + '     ' + str(Ncat) + '     ')
        arquivo.write(str(metricas) + '\n')
    arquivo.close()