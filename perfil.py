def listToStr(lista, l_ord):
    result = ''
    item = 1
    for elemento in lista:
        if not result == '':
            if l_ord:
                result = result + '\n{}({}) {}'.format(13*' ', item, elemento)
                item = item + 1
            else:
                result = result + ', ' + elemento
        else:
            if l_ord:
                result = '({}) {}'.format(item, elemento)
                item = item + 1
            else:
                result = elemento
    return result


class Perfil:
    def __init__(self, dict_perfil):
        self.nome = dict_perfil['nome']
        self.sobrenome = dict_perfil['sobrenome']
        self.email = dict_perfil['email']
        self.residencia = dict_perfil['residencia']
        self.formacao = dict_perfil['formacao']
        self.habilidades = dict_perfil['habilidades']
        self.experiencia = dict_perfil['experiencia']



    def imprime(self):
        print('Email: ' + self.email)
        print('Nome: {}\tSobrenome: {}'.format(self.nome, self.sobrenome))
        #print('Sobrenome:' + self.sobrenome)
        print('Residencia: ' + self.residencia)
        print('Formação Acadêmica: ' + self.formacao)
        print('Habilidades: ' + listToStr(self.habilidades, False))
        print('Experiência: ' + listToStr(self.experiencia, True))
