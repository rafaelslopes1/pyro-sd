empresas = open('empresas.csv', 'r', encoding='utf-8').readlines()

filtro = []
for empresa in empresas:
    if ' - LTDA' in empresa:
        filtro.append(empresa.replace(' - LTDA', ''))
    else:
        filtro.append(empresa)

arq = open('empresas.csv', 'w', encoding='utf-8').writelines(filtro)

