import random, json
from tqdm import tqdm
from time import sleep

def geraDict(email, nome, sobrenome, residencia, form_academica, habilidades, experiencia):
    my_dict = {
        'email': email,
        'nome': nome.replace('\n', ''),
        'sobrenome': sobrenome.replace('\n', ''),
        'residencia': residencia.replace('\n', ''),
        'formacao': form_academica.replace('\n', ''),
        'habilidades': habilidades, #listToStr(habilidades, False),
        'experiencia': experiencia #listToStr(experiencia, True),
    }

    return my_dict

def escreveJson(lista):
    with open('perfisTeste.json', 'w', encoding='utf-8') as f:
        #data = json.load(f)

        json.dump(lista, f, ensure_ascii=False, indent=4, separators=(',', ':'))



def geraProf():
    n_profissoes = random.randint(1,5)
    result = []
    for i in range(n_profissoes):
        iprofissao = random.randint(0, len(profissoes)-1)
        prof = profissoes[iprofissao].replace('\n', '')
        if prof not in result:
            result.append(prof)
    return result



def geraEmpresas(n_empresas):
    result = []
    for i in range(n_empresas):
        while True:
            iempresa = random.randint(0, len(empresas)-1)
            emp = empresas[iempresa].replace('\n', '').replace('\"', '')
            if emp not in result:
                result.append(emp)
                break
    return result



def listToStr(lista, l_ord):
    result = ''
    item = 1
    for elemento in lista:
        if not result == '':
            if l_ord:
                result = result + '; ({}) {}'.format(item, elemento)
                item = item+1
            else:
                result = result + ', ' + elemento
        else:
            if l_ord:
                result = '({}) {}'.format(item, elemento)
                item = item+1
            else:
                result = elemento
    return result



def geraXP(profissoes, empresas):
    tipo = ['Estágio de {tempo} na empresa {empresa}, onde trabalhei como {profissao}',
            'Jovem Aprendiz por {tempo} na empresa {empresa}, onde fui {profissao}',
            'Trabalhei como {profissao} por {tempo} na empresa {empresa}']

    tempo_total = 0
    result = []

    for i in range(len(profissoes)):
        tempo = 0
        itipo = random.randint(0, 2)
        while True:
            if itipo == 0 or itipo == 1:
                tempo = random.randint(1, 2)
            else:
                tempo = random.randint(1, 20)
            if tempo_total+tempo < 25:
                break

        if tempo == 1:
            tempotxt = '1 ano'.format(tempo)
        else:
            tempotxt = '{} anos'.format(tempo)


        #print('n empresas: {}\nn profissoes: {}\n'.format(len(empresas), len(profissoes)))
        emp = empresas[i]
        prof = profissoes[i]
        result.append(tipo[itipo].replace('{tempo}', tempotxt).replace('{empresa}', emp).replace('{profissao}', prof))

    return result



def geraEmail(nome, sobrenome):
    provedores = ['gmail.com', 'hotmail.com', 'outlook.com', 'live.com', 'yahoo.com', 'ymail.com',
                  'terra.com', 'oul.com.br', 'bol.com.br', 'globomail.com']
    separadores = ['.', '-', '_', '']
    provedor = provedores[random.randint(0, len(provedores)-1)]
    separador = separadores[random.randint(0, len(separadores)-1)]
    email = '{}{}{}@{}'.format(nome.replace('\n', '').lower().replace(' ', ''), separador, sobrenome.replace('\n', '').lower().replace(' ', ''),provedor)
    while email in emails:
        num = ''
        for i in range(random.randint(1,3)):
            if not num == '':
                num = num + ', ' + str(random.randint(0,9))
            else:
                num = str(random.randint(0,9))
        email = '{}{}{}{}@{}'.format(nome, separador, sobrenome, provedor, num)
    emails.append(email)
    return email

emails = []
dicts = []
nomes = open('nomes.csv', 'r', encoding='utf8').readlines()
sobrenomes = open('sobrenomes.csv', 'r', encoding='utf8').readlines()
municipios = open('municipios.csv', 'r', encoding='utf8').readlines()
cursos = open('cursos-de-graduacao.csv', 'r', encoding='utf-8').readlines()
empresas = open('empresas.csv', 'r', encoding='utf-8').readlines()
profissoes = open('profissoes.csv', 'r', encoding='utf-8').readlines()


#for i in tqdm(range(100000)):
while len(dicts)<50:
    inome = random.randint(0,len(nomes)-1)
    isobrenome = random.randint(0,len(sobrenomes)-1)
    imunicipio = random.randint(0,len(municipios)-1)
    icurso = random.randint(0,len(cursos)-1)
    #iempresa = random.randint(0,len(empresas))
    #iprofissoes = random.randint(0,len(profissoes))

    prof_perfil = geraProf()
    emp_perfil = geraEmpresas(len(prof_perfil))
    xp_perfil = geraXP(prof_perfil, emp_perfil)
    email_perfil = geraEmail(nomes[inome], sobrenomes[isobrenome])

    my_dict = geraDict(email_perfil, nomes[inome], sobrenomes[isobrenome], municipios[imunicipio], cursos[icurso], prof_perfil, xp_perfil)
    if my_dict in dicts:
        continue
    else:
        dicts.append(my_dict)
        print(len(dicts))
    #sleep(0.01)

escreveJson(dicts)
print('Concluído')