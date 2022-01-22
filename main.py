from arvore import Arvore

#  <GRAFO MODELO>
#
#        | 1 
#        |
#       / \
#      /   \
#   2 /     \ 3
#          /|\
#         / | \
#      4 /  |5 \ 6
#               |
#               | 7       


a = Arvore(8) #Criando objeto Arvore com o numeros de fitasLed

a.add_arestas(1,2,14) # setando arestas e tamnanho das fitas
a.add_arestas(2,3,13)
a.add_arestas(2,4,12)

a.add_arestas(4,5,11)
a.add_arestas(4,6,11)
a.add_arestas(4,7,11)

a.add_arestas(7,8,15)


#a.mostra_matriz()
a.criar_caminho()

 