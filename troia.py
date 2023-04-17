def DFS(grafo, inicioPilha):
    marked = set()
    pilha = []
    pilha.append(inicioPilha)

    while pilha:
        no = pilha.pop()
        if no not in marked:
            marked.add(no)
            pilha.extend(grafo[no] - marked)

    return marked

entrada = input("Insira o número máximo para uma aresta e o número de elementos da comunidade")

numeroMaximo,numeroNos = map(int, entrada.split())

grafo = {int: set()}

print("Insira 2 números separados por espaço em branco ")
for i in range(numeroNos):
    value = input("")

    num1, num2 = map(int, value.split())
    if( ((num1 > numeroMaximo) or (num2 > numeroMaximo)) or (((0 > num1)  or (0>num2)))):
        print("Valores inválidos, reinicie o programa")
        break

    if num1 in grafo.keys():
        grafo[num1].add(num2)
    if num1 not in grafo.keys():
        grafo[num1] = {num2}

    if num2 in grafo.keys():
        grafo[num2].add(num1)
    if num2 not in grafo.keys():
        grafo[num2] = {num1}


resultados = []
iterator_size = len(grafo.keys())
for j in range(1,iterator_size):
    val = DFS(grafo, j)
    resultados.append(val)

#remove duplicados
aux = []
for value in resultados:
    if value not in aux:
        aux.append(value)

#print(resultados)
#print(aux)

print("Total: %d" %len(aux))
