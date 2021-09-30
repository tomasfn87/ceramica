import json

class Receita:
    def __init__(self, ingredientes, porcentagens):
        self.ingr = ingredientes
        self.prop = porcentagens
    
    def le_receitas(self, receita):
        with open("receitas.json", "r") as fh:
            json_str = fh.read()
            json_value_1 = json.loads(json_str)
        receitas = json_value_1

class Ingredientes:
    def imprime_ingredientes():
        with open("ingredientes.json", "r") as fh:
            json_str = fh.read()
            json_value_1 = json.loads(json_str)
        ingr = json_value_1
        
        for i in range(0, len(ingr)):
            if i != 0:
                print()
            print(u"* {} ({})".format(
                ingr[i]["nome"][0].capitalize(), 
                ingr[i]["formula"][1]
            ))
            print("  - Para maiores informações, acessar:")
            print(u"    - {}".format(ingr[i]["wiki"]["pt"]))

Ingredientes.imprime_ingredientes()