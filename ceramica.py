import json

class Receita:
    def __init__(self, ingredientes, porcentagens):
        self.ingr = ingredientes
        self.prop = porcentagens
    
    def le_receitas(self):
        with open("receitas.json", "r") as fh:
            json_str = fh.read()
            json_value = json.loads(json_str)
        return json_value
    
    def calcula_receitas(self, receita):
        print("Receita para 4,5 Kg")

class Ingredientes:
    def imprime_ingredientes():
        with open("ingredientes.json", "r") as fh:
            json_str = fh.read()
            json_value = json.loads(json_str)
        ingredientes = json_value
        
        for i in range(0, len(ingredientes)):
            if i != 0:
                print()
            print(u"{}) {} ({})".format(
                ingredientes[i]["id"],
                ingredientes[i]["nome"][0].capitalize(), 
                ingredientes[i]["formula"][1]
            ))
            print("  - Para maiores informações, acessar:")
            print(u"    - {}".format(ingredientes[i]["wiki"]["pt"]))

Ingredientes.imprime_ingredientes()
# Receita.le_receitas()