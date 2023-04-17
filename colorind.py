#0 = vazio
#1 = ocupado
#2 = pintado

def FloodFill(grid, inicio_x,inicio_y) -> int:
    queue = [(inicio_x, inicio_y)]
    total = 0
    while queue:
        x,y = queue.pop(0)
        #print("X: {} Y: {}".format(x,y))
        #ignorar pois ocupado
        if grid[x][y] == 1:
            continue
        #ignorar pois pintado
        if grid[x][y] == 2:
            continue
        

        grid[x][y] = 2
        total += 1
        if x > 0:
            queue.append((x - 1, y))
        if x < len(grid) - 1:
            queue.append((x + 1, y))
        if y > 0:
            queue.append((x, y - 1))
        if y < len(grid[0]) - 1:
            queue.append((x, y + 1))
        if (x > 0) and y > 0:
            queue.append((x - 1, y - 1))
        if (x > 0) and (y < len(grid[0]) -1):
            queue.append((x-1, y + 1))
        if (x < len(grid) - 1) and (y > 0):
            queue.append((x + 1, y - 1))
        if (x < len(grid) - 1) and (y < len(grid[0]) -1):
            queue.append((x + 1, y + 1))
        
        print(queue)
    return total



N,M,X,Y,K = input("Insira os valores").split()

#cria a matriz de tamanho NxM
matriz = [[0] * int(M) for _ in range(int(N))]


#preenche a matriz com os quadrados ocupados
for i in range(int(K)):
    a,b = input("Insira a coordenada a ser ocupada").split()
    a = int(a)
    b = int(b)
    a = a-1
    b = b-1
    #print("Pos: {} {}".format(a,b))
    matriz[a][b] = 1

#print(matriz)




#print para debug
mystr = ""
for i in range(int(N)):
    for j in range(int(M)):
        val = matriz[i][j]
        str_val = str(val)
        mystr += str_val

    print(mystr)    
    mystr = ""

X = int(X)
Y = int(Y)
X = X-1
Y = Y-1
total = FloodFill(matriz, X,Y)
print("Quadrados pintados: {}".format(total))

