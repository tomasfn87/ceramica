from receita import Receita
from material import Material

receita1 = 'branco alta temperatura'
r1 = Receita(receita1, 1200, 'g')
r1.adicionar_ingrediente(Material('albita', 1800))
r1.adicionar_ingrediente(Material('quartzo', 1350))
r1.adicionar_ingrediente(Material('calcita', 900))
r1.adicionar_ingrediente(Material('caolim', 450))
r1.adicionar_ingrediente(Material('óxido de zircônio', 500))
print(str(r1)+'\n')
r1.ver_porcentagens()
# print('--------------------------------------------')
print()
r1.calcular_novo_peso(1000)

# receita2 = 'transparente alta temperatura'
# r2 = Receita(receita2, 1200, 'g')
# r2.adicionar_ingrediente(Material('albita', 1800))
# r2.adicionar_ingrediente(Material('quartzo', 1350))
# r2.adicionar_ingrediente(Material('calcita', 900))
# r2.adicionar_ingrediente(Material('caolim', 450))
# print('\n'+str(r2)+'\n')
# r2.ver_porcentagens()
# print('--------------------------------------------')
# print()
# r2.calcular_novo_peso(1000)

# receita3 = 'branco alta temperatura amolecido'
# r3 = Receita(receita3, 1200, 'g')
# r3.adicionar_ingrediente(Material('albita', 450))
# r3.adicionar_ingrediente(Material('quartzo', 275))
# r3.adicionar_ingrediente(Material('calcita', 200))
# r3.adicionar_ingrediente(Material('caolim', 75))
# r3.adicionar_ingrediente(Material('óxido de zircônio', 111.111))
# print('\n'+str(r3)+'\n')
# r3.ver_porcentagens()
# print('--------------------------------------------')
# print()
# r3.calcular_novo_peso(5000)

# receita4 = 'transparente alta temperatura amolecido'
# r4 = Receita(receita4, 1200, 'g')
# r4.adicionar_ingrediente(Material('albita', 450))
# r4.adicionar_ingrediente(Material('quartzo', 275))
# r4.adicionar_ingrediente(Material('calcita', 200))
# r4.adicionar_ingrediente(Material('caolim', 75))
# print('\n'+str(r4)+'\n')
# r4.ver_porcentagens()
# print()
# r4.calcular_novo_peso(5000)
