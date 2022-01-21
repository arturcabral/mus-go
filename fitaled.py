# função percorre o led 
# receber tamanho fita e qual vertice.


fita1 = [0,0,1,0,0,0]
#print(fita1)

for n, i in enumerate(fita1):
    if i == 1:
        fita1[n] = 0
        #print("achei")
        #print(n)
        
        if (len(fita1) -1 > n):   # muda pra um o próximo  
            fita1[n+1] = 1
        print(fita1)    



# diminui o peso da lista