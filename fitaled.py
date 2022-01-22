# função percorre o led 
# receber tamanho fita e qual vertice.


fita1 = [10,0,0,0,0,0,0,0]
#print(fita1)

for n, i in enumerate(fita1):
    if not i == 0:
        valTemp = fita1[n]
        fita1[n] = 0
        #print("achei")
        #print(n)

        
        if (len(fita1) -1 > n):   
            if valTemp > 1:
                fita1[n+1] = valTemp - 1
            else:
                fita1[n+1] =  0

        print(fita1)    





# diminui o peso da lista