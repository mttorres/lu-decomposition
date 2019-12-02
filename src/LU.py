from numpy import matmul
from numpy.linalg import inv, det
import copy
from numpy.linalg import inv
from numpy import asarray



# O menor principal associado ao elemento aij é a matriz que se obtém eliminando a linha e a coluna e quem está o elemento aij, onde i=j
def menorPrincipal(mat, i):
    mat_menor = copy.deepcopy(mat)

    del mat_menor[0]                            # Retira a primeira linha
    for k in list(range(len(mat_menor))):       # Retira a coluna i
        del mat_menor[k][i]
    return mat_menor

# Cálculo do determinante através do método de cofatores
# Aij = (-1)^i+j . MCij
def determinante(matriz):
    mat = copy.deepcopy(matriz)
    if len(mat) == 1:                           # Fim de cada pilha de recursão
        return mat[0][0]
    else:
        val = 0
        tam = len(mat)
        for x in list(range(tam)):                                                              # na primeira linha encontrando cofatores
            val += mat[0][x] * (-1) ** (2 + x) * determinante(menorPrincipal(mat, x))           # Somatorio dos elementos multiplicado por  seus cofactores
        return val


# cria matriz identidade para facilitar operações
def criaIdentidade(n):
    return [[1.0 if i == j else 0.0 for j in range(n)]
                for i in range(n)]


#troca linha 1 por linha 2
def trocaLinha(a,lineindex1,lineindex2):
    temp = a[lineindex1]
    a[lineindex1] = a[lineindex2]
    a[lineindex2] = temp

#realiza a operação de eliminação de gaus para cada linha(abaixo do pivo): li = aij - (aij/pivo)*(linhaPivo)
def eliminacaoGauss(a,pivoindex,lineindex,n,operacoes):
    I = criaIdentidade(n)
    while(lineindex < n):
        # guarda os coeficientes na matriz Ei
        I[lineindex][pivoindex] = (a[lineindex][pivoindex] / a[pivoindex][pivoindex])*(-1)
        a[lineindex] =  [
            (a[lineindex][x] - ( (a[lineindex][pivoindex]/a[pivoindex][pivoindex] )*a[pivoindex][x] ) )
            for x in range(0,n)
            ]

        #guarda um vetor de operacoes Ei

        lineindex+=1
    if(n != pivoindex):
        operacoes.append(I)
        # evita salvar mais matrizes do que devia ao fim da iteração


def PivoteamentoParcial(A,permutacoes,n,posXpivo):
    mudanca = posXpivo
    maior = A[posXpivo][posXpivo]

    for i in range(1+posXpivo,n):
        if(abs(maior) < abs(A[i][posXpivo]) ):
            maior = A[i][posXpivo]
            mudanca = i

    if (mudanca != posXpivo):
        trocaLinha(A, posXpivo, mudanca)
        I = criaIdentidade(n)
        trocaLinha(I, posXpivo, mudanca)
        permutacoes.append(I)



#cria a matriz A' (após pivoteamento parcial)
def criaEscalonada(A,n,operacoes,permutacoes):
    for i in range(0,n-1):
        PivoteamentoParcial(A,permutacoes,n,i)
        # ao fim desse processo ele ja vai ter a LINHA ATUAL AJUSTADA e guardou a permutacao de linha na matriz "permutacoes"
        #pode realizar eliminacao de Gauss
        eliminacaoGauss(A,i,i+1,n,operacoes)


def criarL(operacoes,permutacoes,n):
    L = []
    # deve criar (Enx...E1^)
    # onde Ei^ = (Pi+1)X Ei X(Pi+1)
    # note que L deve ser triangular inferior!
    for i in range(len(operacoes)-1,0,-1):

        # note que ele so realiza essa operacao se ocorreu ALGUMA PERMUTACAO DE LINHA!
        if(i == 1 and len(permutacoes) > 0):
            Etiu = matmul(matmul(permutacoes[i],operacoes[i-1]),permutacoes[i])
            if(len(L) != 0 ):
                L = matmul(L,Etiu)
            else:
                L = matmul(operacoes[i], Etiu)
        else:
            L = matmul(operacoes[i], operacoes[i - 1])

    L = inv(L)
    return L


def permutarB(permutacoes, B):
    for i in range(0,len(permutacoes)):
        B = matmul(permutacoes[i],B)
    return B


def retroSub(A,X,B,n,modo):
    #ORDEM PADRAO
    if(modo == 'U'):
        for i in range(n-1, -1, -1):
            if(i == n-1):
                X.append(B[i]/A[i][i])
            else:
                X.insert(0,B[i])
                for j in range(n-1,i,-1):
                    X[0] -= ( A[i][j]*X[j-i] )

                X[0] = X[0]/A[i][i]

    #ORDEM REVERSA
    if(modo == 'L'):
        for i in range(0,n):
            if(i == 0):
                X.append(B[i] / A[i][i])
            else:
                X.append(B[i])
                for j in range(0,i):
                    X[i] -= ( A[i][j] * X[j] )

                X[i] = X[i] / A[i][i]

def resolveSistema(A, L, Blinha,n):
    X = []
    Y = []

    #retrosubstituicao
    retroSub(L,Y,Blinha,n,modo='L')
    retroSub(A, X, Y, n, modo='U')

    print("####RESULTADOS#####")
    print(X)
    print(Y)
    print("####RESULTADOS#####")









#operação LU
def operation(A,B,controlCanon):

    #calcular determinante para saber se pode realizar a operacoes (se nao puder disparar erro)
    det = determinante(A)
    if(det == 0):
        print("SISTEMA INVALIDO!")
        #escrever isso no arquivo de saida
        return

    n = len(A)
    print("######################### SISTEMA ###########")
    print("A: ")
    print()
    print(asarray(A))
    print("B: ")
    print()
    print(B)
    print()
    print("Determinante")
    print(det)
    print()



    operacoes = []  # matrizes E(eliminações gauss)(a inversa dela é igual a L)
    permutacoes = []  # matrizes P (trocas de linhas) (Pnx...P2xP1xP0)
    criaEscalonada(A,n,operacoes,permutacoes) # ao fim disso A = A' !
    L = criarL(operacoes,permutacoes,n) # criar L usando as operações realizadas anteriormente

    print()
    print(operacoes)  # ta salvando corretamente
    print()
    print(permutacoes)  # ta salvando corretamente
    print()
    print(L)  # aparentemente esta salvando corretamente (deve ser triangular inferior)



    # e finalmente resolver os sistemas LY = B' e UX = Y respectivamente
    #se controlCannon é true ele resolve N sistemas iterando sobre os diversos membros da matriz B (N bases canonicas)
    #ou seja ele esta calculando a inversa da matriz A
    if(controlCanon):
        for i in range(0,n):
            Blinha = permutarB(permutacoes, B[i])  # criar PB = B'
            resolveSistema(A,L,Blinha,n)

    #resolve o sistema uma vez só por fatoração LU
    else:

        Blinha = permutarB(permutacoes, B)  # criar PB = B'
        print("B após permutações (B'): ")
        print(Blinha)
        print()
        resolveSistema(A,L,Blinha,n)


    # resultados(print, tem que salvar no arquivo dps)









''''''
# testando
A = [[1,4,3],[2,5,4],[1/2,-3,-2]]
B2 = [3,6,-16,18]
A2 = [[3,2,0,1],[9,8,-3,4],[-6,4,-8,0],[3,-8,3,-4]]


BT = []
BT.extend([ [1.0 if i == j else 0.0 for j in range(6)]
                        for i in range(6) ])


#operation(A,[],False)
#print(asarray(A))

operation(A2,B2,False)
print()




#### diferenca do determinante do NUMPY e o nosso
print("--------------------------")
determ = det(A2)


print("--------------------------")
determ2 = determinante(A2)
