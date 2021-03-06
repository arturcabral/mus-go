#FAZER:
#Ajustar a função percorrerLed para apagar os leds no final da fita 
#Passar peso para a próxima fita

import random, math

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
                 percorrerLed(valoresFita[0],valoresFita[1]) #função para gerar animação na fita

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
                
                caminhoEscolhido = altChoice(list(caminhos.keys())) #versaoChoice

                #caminhoEscolhido = random.choice(list(caminhos.keys())) #nao suporta esp8266
                #print(caminhos)
                #print(caminhoEscolhido)
                valorCaminho = caminhos[caminhoEscolhido] 
                valoresFita = [caminhoEscolhido, valorCaminho]
                #print("caminho escolhido/vertice:" + str(caminhoEscolhido) + " indice/peso:" + str(valorCaminho))
                print("FITA:" + str(valoresFita))
                percorrerLed(valoresFita[0],valoresFita[1])
                posicao = caminhoEscolhido
            
            if j == self.vertices -1:
                print("Fim raiz")

 
def percorrerLed (e,t): #recebe o endereço da fita e o tamanho dela
    pesoIni = 18
    
    fita =[0]* t #contrutor da fita
    fita[0] = pesoIni #adiciona peso inicial (força do LED)
    print("Fita " + str(e))
    print(fita)
    for n, i in enumerate(fita): #varre a lista
        if not i == 0: # procura onde está o pixel
            valTemp = fita[n]
            fita[n] = 0
    
            if (len(fita) -1 > n):   # passa para proxima casa e diminui o peso
                if valTemp > 1:
                    fita[n+1] = valTemp - 1
                else:
                    fita[n+1] =  0
                print(fita)

#choice alternative
def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin)/ float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def altChoice(lista):
        randomBits = random.getrandbits(16)
        ceiling = len(lista)
        num = translate(randomBits, 0, 65535, 0 , ceiling)
        choice = lista[math.floor(num)]
        return choice
        


#  <GRAFO MODELO>
#        1 <vértice de início>
#        | 2 
#        |
#       / \
#      /   \
#   3 /     \ 4
#          /|\
#         / | \
#      5 /  |6 \ 7
#               |
#               | 8     


a = Arvore(8) #numeros de vertices( vertices = fita + 1) na árvore

a.add_arestas(1,2,14) # setando arestas (verticeA, verticeB, Tamanho Fita)
a.add_arestas(2,3,13)
a.add_arestas(2,4,12)

a.add_arestas(4,5,11)
a.add_arestas(4,6,11)
a.add_arestas(4,7,11)

a.add_arestas(7,8,15)



#a.mostra_matriz()
a.criar_caminho()







