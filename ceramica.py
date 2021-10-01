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
        receita = Receita(i, p)
    
    def seleciona_ingredientes():
        Ingredientes.imprime_ingredientes()

    def calcula_receita(self, receita):
        print("Receita para 4,5 Kg")

class Ingredientes:
    def imprime_ingrediente(ingrediente, formato="curto"):
        # Versão simples
        print(u"{}) {}".format(
                ingrediente["id"],
                ingrediente["nome"][0].capitalize()
            ), end="")
        if len(ingrediente["nome"]) > 1:
            alternativos = ingrediente["nome"][:]
            alternativos.pop(0)
            print(" ({})".format(T.Texto.conectar(alternativos,", ")))
        # Versão completa
        if formato == "longo":
            # ou:
            print("   Fórmula: {}".format(
                T.Quimica.imprimir_formula(ingrediente["formula"][0])
            ))
            # Temperatura de fusão
            temps_fusao = ingrediente["temperatura"]["fusao"]
            print("   - Temperatura de Fusão: ", end="")
            id_valor = 0
            for t in temps_fusao:
                # Valores
                valores = t["valor"]
                print()
                if len(valores) == 2:
                    print(end=" ")
                    if id_valor == 0:
                        print("            entre:", end=" ")
                    else:
                        print("                  ", end=" ")
                    print("- {} e {}".format(
                        valores[0], valores[1]
                    ), end =" ")
                else:
                    if id_valor == 0:
                        print("              a partir de:", end=" ")
                    else:
                        print("                          ", end=" ")
                    print("- " + str(valores[0]), end=" ")
                # Sistema (°C, °F ou K)
                if t["sistema"] == "K":
                    print(t["sistema"], end="")
                else:
                    print(t["sistema"], end=", ")
                id_valor += 1
            # Wikipedia URL
            wiki = ingrediente["wiki"]
            print("\n  Acessar: ")
            for w in wiki:
                print("         - {}.wikipedia.org/{}".format(w, wiki[w]))
            

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

Ingredientes.listar_ingredientes("longo")
print()
Ingredientes.listar_ingredientes()
# Receita.le_receitas()