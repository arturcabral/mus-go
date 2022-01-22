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




        
        posicao = 1
        valoresFita = []
        for i in self.arvore[0]: #busca na primeira linha o primeiro peso
             if (i != 0):
                 #print("Inicio" + " peso " + str(i))  # peso da aresta
                 valoresFita = [posicao,i]
                 print("FITA:" + str(valoresFita))

        for j in range(self.vertices): #percorre o caminho
            caminhos = {}
            controle = False
            for i,v in enumerate(self.arvore[posicao]):
                if (v != 0): # se o valor for diferente de zero
                    #print("encontei")
                    controle = True  
                    #print(str(i) + " " + str(v)) # imprime o indice(vertice) e o valor (peso)
                    caminhos[i] = v
                #else:
                    #print("nada encontrado")

            if not controle:
                print("FIM DO CAMINHO")
                break
            else: #seleciona o caminho
                #print("caminhos encontados:" + str(caminhos) + " em " + str(posicao))
                #print("caminho" + str(caminhos))
                #print("caminho chave" + str(list(caminhos.keys())))
                caminhoEscolhido = random.choice(list(caminhos.keys()))
                #print(caminhos)
                #print(caminhoEscolhido)
                valorCaminho = caminhos[caminhoEscolhido] 
                valoresFita = [caminhoEscolhido, valorCaminho]
                #print("caminho escolhido/vertice:" + str(caminhoEscolhido) + " indice/peso:" + str(valorCaminho))
                print("FITA:" + str(valoresFita))
                posicao = caminhoEscolhido
            
            if j == self.vertices -1:
                print("Fim raiz")



    #escolher possibilidade
    #volta e verifica as possibilidades 

a = Arvore(8)

a.add_arestas(1,2,14)
a.add_arestas(2,3,13)
a.add_arestas(2,4,12)

a.add_arestas(4,5,11)
a.add_arestas(4,6,11)
a.add_arestas(4,7,11)

a.add_arestas(7,8,15)



a.mostra_matriz()
a.criar_caminho()







