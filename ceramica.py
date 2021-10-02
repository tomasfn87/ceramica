import json
import texto as T

class Receita:
    def __init__(self, ingredientes, porcentagens):
        self.i = ingredientes
        self.p = porcentagens
    
    def acessar_receitas(self, mode="r"):
        ingredientes = Ingredientes.acessar_ingredientes()
        with open("receitas.json", mode) as fh:
            json_str = fh.read()
            json_value = json.loads(json_str)
        return json_value

    def nova_receita(self):
        receitas = Receita.acessar_receitas("w")
        # Receita.seleciona_ingredientes()
        i = [1, 2]
        p = [20, 80]
        assert p.extend() >= 100 \
            and p.extend() <= 115
        receita = Receita(i, p)
    
    def listar_ingredientes(opcao=False):
        ingredientes = Ingrediente.acessar_ingredientes("r")
        if opcao == False:
            return "Nenhuma opção selecionada."
        # Opção "1"
        elif opcao == "1":
            print()
            Ingrediente.listar_ingredientes()

            print(
                "\nDigite de o código (de 1 a {}) do ingrediente para mais \
                     detalhes (ou digite 'voltar'):".format(
                        len(ingredientes)
                ), end=" "
            )
            detalhe = input()
            if "1" <= detalhe <= str(len(ingredientes)):
                print()
                Ingrediente.imprime_ingrediente(
                    ingredientes[int(detalhe) - 1], "longo"
                )
                print()
                Receita.listar_ingredientes("1")
            elif detalhe == "voltar":
                print()
                return Receita.selecionar_ingredientes()
            else:
                print("Opção inválida.")
        # Opção "2"
        elif opcao == "2":
            print()
            Ingrediente.listar_ingredientes("longo")
            print()
            return Receita.selecionar_ingredientes()
        # Opção "sair"
        elif opcao == "sair":
            print("\nFechando ingredientes.")
            return ()
        # Nenhuma das opções anteriores
        else:
            print("\nOpção inválida.")
            print()
            return Receita.selecionar_ingredientes()

    def selecionar_ingredientes():
        print("Selecione uma das opções:")
        print("  1) mostrar ingredientes")
        print("  2) mostrar ingredientes (completo)")
        opcao = input("    (Digite 'sair' para finalizar): ")
        Receita.listar_ingredientes(opcao)

    def calcula_receita(self, receita):
        print("Receita para 4,5 Kg")

class Ingrediente:
    def acessar_ingredientes(mode="r"):
        with open("ingredientes.json", mode) as fh:
            json_str = fh.read()
        return json.loads(json_str)

    def imprime_ingrediente(ingrediente, formato="curto"):
        # Versão simples
        print("{}) {}".format(
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
        ingredientes = Ingrediente.acessar_ingredientes()
        for i in range(0, len(ingredientes)):
            if i != 0 and formato == "longo":
                print()
            ingrediente = ingredientes[i]
            if formato == "longo":
                Ingrediente.imprime_ingrediente(ingrediente, "longo")
            else:
                Ingrediente.imprime_ingrediente(ingrediente)

""" Ingrediente.listar_ingredientes("longo")
print()
Ingrediente.listar_ingredientes() """
# Receita.le_receitas()
Receita.selecionar_ingredientes()