# função percorre o led 
# receber tamanho fita e qual vertice.


fita1= [0]*6 #contrutor fita 1
fita1[0]=10  #add primeiro peso

print(fita1)

for n, i in enumerate(fita1): #varre a lista
    if not i == 0: # procura onde está o pixel
        valTemp = fita1[n]
        fita1[n] = 0
        #print("achei")
        #print(n)

        
        if (len(fita1) -1 > n):   # passa para proxima casa e diminui o peso
            if valTemp > 1:
                fita1[n+1] = valTemp - 1
            else:
                fita1[n+1] =  0

        print(fita1)    
