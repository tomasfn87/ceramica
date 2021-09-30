import json
import texto as T

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
    def imprime_ingrediente(ingrediente, formato="curto"):
        # Versão simples
        print(u"{}) {} [{}]".format(
                ingrediente["id"],
                ingrediente["nome"][0].capitalize(), 
                ingrediente["formula"][1]
            ))
        # Versão completa
        if formato == "longo":
            # Temperatura de fusão
            temps_fusao = ingrediente["temperatura"]["fusao"]
            print("\n   - Temperatura de Fusão: ", end="")
            for t in temps_fusao:
                # Valores
                valores = t["valor"]
                if len(valores) == 2:
                    print("\n     - {}-{}".format(
                        valores[0], valores[1]
                    ), end =" ")
                else:
                    print("\n     - " + str(valores[0]), end=" ")
                # Sistema (°C, °F ou K)
                if t["sistema"] == "K":
                    print(t["sistema"], end="")
                else:
                    print(t["sistema"], end=", ")
            # Wikipedia URL
            wiki = ingrediente["wiki"]
            print("\n\n   - {}".format(wiki["pt"]))

    def listar_ingredientes(formato="curto"):
        with open("ingredientes.json", "r") as fh:
            json_str = fh.read()
            json_value = json.loads(json_str)
        ingredientes = json_value
        
        for i in range(0, len(ingredientes)):
            if i != 0 and formato == "longo":
                print()
            ingrediente = ingredientes[i]
            if formato == "longo":
                Ingredientes.imprime_ingrediente(ingrediente, "longo")
            else:
                Ingredientes.imprime_ingrediente(ingrediente)

Ingredientes.listar_ingredientes()
print()
Ingredientes.listar_ingredientes("longo")
# Receita.le_receitas()