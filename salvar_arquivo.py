import os

def salvar_validation(BETA: float, RO: float, Ncat: int,metricas) -> None:
    pasta = 'resultado/10-fold_emPartes/'
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