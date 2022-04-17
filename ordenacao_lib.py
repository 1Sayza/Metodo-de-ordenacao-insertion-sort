def ordena_insertion(dados):
    i=1
    j=i-1
    while True:
        j=i-1
        newpos = -1
        while True:
            if(int(dados[i])<int(dados[j])):
                newpos=j
                j=j-1
            elif int(dados[i])>int(dados[j]) or int(dados[i])==int(dados[j]):
                newpos=j+1
                break             
            if j<0:
                break
        if newpos!=-1:
                k=i
                while k>newpos:
                    dados[k],dados[k-1]=dados[k-1],dados[k]
                    k=k-1
        i=i+1
        if i>=len(dados):
            break
    print (dados)
    return dados