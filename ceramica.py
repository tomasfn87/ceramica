import json

class Receita:
    def __init__(self, ingredientes, porcentagens):
        self.i = ingredientes
        self.p = porcentagens
    
    def le_receitas(self):
        with open("receitas.json", "r") as fh:
            json_str = fh.read()
            json_value = json.loads(json_str)
        return json_value

    def nova_receita(self):
        with open("receitas.json", "w") as fh:
            json_str = fh.read()
            json_value = json.loads(json_str)
        receitas = json_value
        # Receita.seleciona_ingredientes()
        i = [1, 2]
        p = [20, 80]
        assert p.extend() >= 100 \
            and p.extend() <= 115
        receita = Receita()
    
    def seleciona_ingredientes():
        Ingredientes.imprime_ingredientes()

    def calcula_receita(self, receita):
        print("Receita para 4,5 Kg")

class Ingredientes:
    def imprime_ingredientes(longo="curto"):
        with open("ingredientes.json", "r") as fh:
            json_str = fh.read()
            json_value = json.loads(json_str)
        ingredientes = json_value
        
        for i in range(0, len(ingredientes)):
            if i != 0 and longo == "longo":
                print()
            print(u"{}) {} ({})".format(
                ingredientes[i]["id"],
                ingredientes[i]["nome"][0].capitalize(), 
                ingredientes[i]["formula"][1]
            ))
            if longo == "longo":
                print("  - Para maiores informações, acessar:")
                print(u"    - {}".format(ingredientes[i]["wiki"]["pt"]))

Ingredientes.imprime_ingredientes()
print()
Ingredientes.imprime_ingredientes("longo")
# Receita.le_receitas()