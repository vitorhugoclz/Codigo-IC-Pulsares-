def gerar_rotulos_binarios(vencedores: list, rotulos_treino: list) -> list:
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