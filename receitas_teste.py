from receita import Receita
from material import Material

receita1 = 'Branco alta temperatura'
r1 = Receita(receita1, 1200, 'g')
r1.adicionar_ingrediente(Material('Albita', 1800))
r1.adicionar_ingrediente(Material('Quartzo', 1350))
r1.adicionar_ingrediente(Material('Calcita', 900))
r1.adicionar_ingrediente(Material('Caolim', 450))
r1.adicionar_ingrediente(Material('Óxido de Zircônio', 500))
print(str(r1)+'\n')
r1.ver_porcentagens()
print()
r1.calcular_novo_peso(1000)
print('--------------------------------------------')
print()

receita2 = 'Transparente alta temperatura'
r2 = Receita(receita2, 1200, 'g')
r2.adicionar_ingrediente(Material('Albita', 1800))
r2.adicionar_ingrediente(Material('Quartzo', 1350))
r2.adicionar_ingrediente(Material('Calcita', 900))
r2.adicionar_ingrediente(Material('Caolim', 450))
print(str(r2)+'\n')
r2.ver_porcentagens()
print()
r2.calcular_novo_peso(1000)
print('--------------------------------------------')
print()

receita3 = 'Branco alta temperatura amolecido'
r3 = Receita(receita3, 1200, 'g')
r3.adicionar_ingrediente(Material('Albita', 450))
r3.adicionar_ingrediente(Material('Quartzo', 275))
r3.adicionar_ingrediente(Material('Calcita', 200))
r3.adicionar_ingrediente(Material('Caolim', 75))
r3.adicionar_ingrediente(Material('Óxido de Zircônio', 111.111))
print(str(r3)+'\n')
r3.ver_porcentagens()
print()
r3.calcular_novo_peso(5000)
print('--------------------------------------------')
print()

receita4 = 'Transparente alta temperatura amolecido'
r4 = Receita(receita4, 1200, 'g')
r4.adicionar_ingrediente(Material('Albita', 450))
r4.adicionar_ingrediente(Material('Quartzo', 275))
r4.adicionar_ingrediente(Material('Calcita', 200))
r4.adicionar_ingrediente(Material('Caolim', 75))
print(str(r4)+'\n')
r4.ver_porcentagens()
print()
r4.calcular_novo_peso(5000)
