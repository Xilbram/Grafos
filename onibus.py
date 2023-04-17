def findPath(graph, start, end):
    visitados = set()
    #tupla contendo os possiveis caminhos e a lista com o path feito até entao
    pilha = [(start, [start])]
    while pilha:
        no, caminho = pilha.pop()
        if no == end:
            return caminho
        
        #verifica os que não foram acessados; marca ao acessar
        if no not in visitados:
            visitados.add(no)   
            for adj in graph.get(no, []):
                pilha.append((adj, caminho + [adj]))
            
    #existe a possibilidade de n ter caminho ent return none se n bater em "no == end"
    return None



N,A,B = [int(x) for x in input("Insira os valores de Nº cidades, cidade origem e e cidade destino separados por espaços ").split()]
adjs = {}

for i in range(N-1):
    no, aresta = [int (x) for x in input("Insira o nó e a aresta que ele conecta ").split()]
    
    if no in adjs.keys():
        adjs[no].append(aresta)

    if no not in adjs.keys():
        adjs[no] = [aresta]

    if aresta in adjs.keys():
        adjs[aresta].append(no)

    if aresta not in adjs.keys():
        adjs[aresta] = [no]

    
path = findPath(adjs, A,B)

#print(adjs)
#print(path)
print("Total caminhos: {}".format(len(path)-1))

