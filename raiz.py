import random

class Arvore:

    def __init__(self, vertices):
        self.vertices = vertices
        self.arvore  = [[0]*self.vertices for i in range(self.vertices)] #criar uma lista onde a quantidade de posição é o peso
        #toda lista vai receber 0 

    def add_arestas(self, u, v, peso):
        self.arvore[u-1][v-1] = peso

    def mostra_matriz(self):
        print('Matriz:')
        for i in range(self.vertices):
            print(self.arvore[i])
    
    def criar_caminho(self):
        for i in self.arvore[0]:
             if (i != 0):
                 print("Inicio")  # colocar tamanho

        posicao = 1

        for j in range(self.vertices):
            caminhos = {}
            controle = False
            for i,v in enumerate(self.arvore[posicao]):
                if (v != 0): # se o valor for diferente de zero
                    print("encontei")
                    controle = True  
                    #print(str(i) + " " + str(v)) # imprime o indice e o valor
                    caminhos[i] = v
                else:
                    print("nada encontrado")

            if not controle:
                print("FIM DO CAMINHO")
                break
            else:
                print("caminhos encontados:" + str(caminhos) + " em " + str(posicao))
                caminhoEscolhido = random.choice(list(caminhos.keys()))
                print(caminhos)
                print(caminhoEscolhido)
                indiceCaminho = caminhos[caminhoEscolhido] 
                print("caminho escolhido:" + str(caminhoEscolhido) + " indice:" + str(indiceCaminho + 1))
                posicao = indiceCaminho
            
            if j == self.vertices -1:
                print("Fim raiz")



    #escolher possibilidade
    #volta e verifica as possibilidades 

a = Arvore(8)

a.add_arestas(1,2,4)
a.add_arestas(2,3,3)
a.add_arestas(2,4,2)

a.add_arestas(4,5,1)
a.add_arestas(4,6,1)
a.add_arestas(4,7,1)

a.add_arestas(7,8,2)



a.mostra_matriz()
a.criar_caminho()







