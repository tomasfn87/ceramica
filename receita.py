import regex
from material import Material

class Receita:
    def __init__(self, nome, temperatura, unidade):
        self.nome = str(nome)
        self.nome = regex.sub('\d', '', self.nome).strip()
        self.temperatura = str(temperatura)
        self.temperatura = int(regex.sub('\D', '', self.temperatura))
        self.unidade = str(unidade)
        self.unidade = regex.sub('\d', '', self.unidade).strip()
        self.ingredientes = []
    
    def __repr__(self):
        repr = f'Nome: {self.nome} ({self.temperatura}°C)'
        if self.ingredientes:
            for i in self.ingredientes:
                repr += f'\n - Material: {i.nome}, peso: {"{:.0f}".format(i.peso)}{self.unidade}'
            repr += f'\n Peso total: {round(self.peso_total())}{self.unidade}'
        else:
            repr += f'\n* Ingredientes: {len(self.ingredientes)}'
        return repr
    
    def append(self, ingrediente):
        if str(type(ingrediente)) != "<class 'material.Material'>":
            return False
        self.ingredientes.append(ingrediente)
        return True
    
    def adicionar_ingrediente(self, ingrediente, loud=False):
        if self.append(ingrediente):
            loud and print(f'* Ingrediente {len(self.ingredientes)} ({ingrediente.nome}, {"{:.1f}".format(ingrediente.peso)}{self.unidade}) adicionado com sucesso.')
            return
        print(f'O ingrediente precisa ser um objeto da classe Material')
    
    def peso_total(self):
        peso_total = 0
        if self.ingredientes:
            for i in self.ingredientes:
                peso_total += i.peso
        return peso_total
    
    def ver_porcentagens(self):
        if self.ingredientes:
            total_porcentagem = 0
            print('Porcentagem de cada elemento: ')
            for i in self.ingredientes:
                porcentagem = (i.peso / self.peso_total()) * 100
                total_porcentagem += porcentagem
                print(f' - {i.nome}: {"{:.2f}".format(round(porcentagem, 2))}%')
    
    def calcular_novo_peso(self, novo_peso):
        fator = novo_peso / self.peso_total()
        peso_calculado = f'Novo peso ({novo_peso}{self.unidade}) para {self.nome} ({self.temperatura}°C)'
        if self.ingredientes:
            for i in self.ingredientes:
                peso_calculado += f'\n - Material: {i.nome}, peso: {"{:.0f}".format(i.peso*fator)}{self.unidade}'
        else:
            peso_calculado += f'\n* Ingredientes: {len(self.ingredientes)}'
        print(peso_calculado)
