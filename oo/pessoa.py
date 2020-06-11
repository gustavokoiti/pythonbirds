# Pacote -> Módulo -> Classe -> Método("função")
class Pessoa:
    olhos = 2  # atributo de classe, se for geral para todas as "Pessoa"

    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade  # atributos de instância
        self.nome = nome  # atributos de instância
        self.filhos = list(filhos)  # atributos de instância

    def cumprimentar(self):
        return f'Olá Sr. {id(self)}'

    @staticmethod  # decorator
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

######################
if __name__ == '__main__':
    gustavo = Pessoa(nome='Gustavo')
    luciano = Pessoa(gustavo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Okamura'
    del luciano.filhos
    print(luciano.__dict__)
    print(gustavo.__dict__)
    print(Pessoa.olhos)
    print(gustavo.olhos)
    print(luciano.olhos)
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())

class Carro:
    def __init__(self, motor, direcao):


class Motor:
    def __init__(self, velocidade):
        self.velocidade = velocidade
    def acelerar(self):
        return velocidade += 1
    def frear(self):
        if velocidade <= 1:
            return 0
        else:
            return velocidade -= 2


class Direcao:
    def __init__(self, direcao):
        self.direcao = ['Norte', 'Leste', 'Sul', 'Oeste']
    def girar_a_direita:
        pass
    def girar_a_esquerda:
        pass
