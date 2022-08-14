import regex

class Material:
    def __init__(self, nome, peso, tipo=''):
        self.nome = str(nome)
        self.nome = regex.sub('\d', '', self.nome).strip()
        self.tipo = str(tipo)
        self.peso = str(peso)
        self.peso = float(regex.sub('[^0-9.]', '', self.peso))
    
    def __repr__(self):
        if self.tipo:
            return f'{self.nome}: {self.peso} ({self.tipo})'
        return f'{self.nome}: {self.peso}'
