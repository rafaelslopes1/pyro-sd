import random
import Pyro4
import json
from perfil import Perfil
import time

def procura(email):
    for perf in perfis:
        if perf['email'] == email:
            return perf


def pessoasFormadas(curso):
    lista = []
    for perf in perfis:
        if perf['formacao'] == curso:
            lista.append(Perfil(perf))
    return lista


def moradores(cidade):
    lista = []
    for perf in perfis:
        if perf['residencia'] == cidade:
            lista.append(Perfil(perf))
    return lista


def capturaXP(email):
    print('=== TIPO DE EXPERÊNCIA ===')
    print('(1) Jovem Aprendiz')
    print('(2) Estágio')
    print('(3) Emprego')

    while True:
        try:
            tipo = int(input("Digite o tipo: "))
            if tipo <1 or tipo >3:
                print('Opção inválida! Tente novamente')
                continue
        except ValueError:
            print('Digite um número inteiro!')
            continue
        else:
            break

    #print('\n')

    while True:
        cargo = input('Digite seu cargo: ')
        if cargo.isnumeric():
            print("Digite um texto!")
            continue
        else:
            cargo = cargo.title()
            break

    #print('\n')

    while True:
        empresa = input('Digite o nome da empresa: ')
        if cargo.isnumeric():
            print("Digite um texto!")
            continue
        else:
            empresa = empresa.upper()
            break

    #print('\n')

    while True:
        try:
            tempo = int(input('Digite a duração (anos): '))
        except ValueError:
            print("Digite um número inteiro!")
            continue
        else:
            break

    geraXP(tipo, cargo, empresa, tempo, email)


def geraXP(itipo, cargo, empresa, tempo, email):
    tipo = ['Jovem Aprendiz por {tempo} na empresa {empresa}, onde fui {profissao}',
            'Estágio de {tempo} na empresa {empresa}, onde trabalhei como {profissao}',
            'Trabalhei como {profissao} por {tempo} na empresa {empresa}']

    if tempo == 1:
        tempotxt = '1 ano'.format(tempo)
    else:
        tempotxt = '{} anos'.format(tempo)

    XP = tipo[itipo-1].replace('{tempo}', tempotxt).replace('{empresa}', empresa).replace('{profissao}', cargo)

    addXP(cargo, XP, email)


def addXP(cargo, XP, email):
    perfil = procura(email)
    perfil['habilidades'].append(cargo)
    perfil['experiencia'].append(XP)
    with open('perfisTeste.json', 'w', encoding='utf-8') as perfisJsonW:
        json.dump(perfis, perfisJsonW, ensure_ascii=False, indent=4, separators=(',', ':'))


def XP(email):
    perfil = procura(email)
    if perfil == None:
        print('Email não encontrado!')
    else:
        perfilObj = Perfil(perfil)
        return perfilObj.experiencia


def listarTodos():
    print('=== LISTA DE PERFIS ===')
    for perf in perfis:
        perfil = Perfil(perf)
        perfil.imprime()
        print('\n')


def listarPerfil(email):
    perfil = procura(email)
    if perfil == None:
        print('Email não encontrado!')
    else:
        perfil.imprime()


with open('perfis.json', 'r', encoding='utf-8') as perfisJson:
    perfis = json.load(perfisJson)
perfisJson.close()

#capturaXP('deidiane_assuncao@outlook.com')
#for pessoa in perfis:
#    Perfil(pessoa).imprime()
inicio = time.time()
for pessoa in perfis:
    Perfil(pessoa).imprime()
fim = time.time()
print(fim - inicio)