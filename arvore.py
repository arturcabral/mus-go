#FAZER:
#Ajustar a função percorrerLed para apagar os leds no final da fita 

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
                caminhoEscolhido = random.choice(list(caminhos.keys()))
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