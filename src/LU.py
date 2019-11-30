from numpy import matmul

#cria matriz identidade para facilitar operações
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
        I[lineindex][pivoindex] = (a[lineindex][pivoindex] / a[pivoindex][pivoindex]) * (-1)
        a[lineindex] =  [
            (a[lineindex][x] - ( (a[lineindex][pivoindex]/a[pivoindex][pivoindex] )*a[pivoindex][x] ) )
            for x in range(0,n)
            ]

        #guarda um vetor de operacoes Ei

        lineindex+=1
    operacoes.append(I)

def PivoteamentoParcial(A,permutacoes,n,posXpivo):
    mudanca = posXpivo
    maior = A[posXpivo][posXpivo]

    for i in range(1+posXpivo,n):
        if(maior < abs(A[i][posXpivo]) ):
            maior = A[i][posXpivo]
            mudanca = i

        if(mudanca != posXpivo):
            trocaLinha(A, posXpivo, mudanca)
            I = criaIdentidade(n)
            trocaLinha(I,posXpivo, mudanca)
            permutacoes.append(I)
            mudanca = posXpivo







#cria a matriz A' (após pivoteamento parcial)
def criaEscalonada(A,n,operacoes,permutacoes):
    for i in range(0,n):
        PivoteamentoParcial(A,permutacoes,n,i)
        # ao fim desse processo ele ja vai ter a LINHA ATUAL AJUSTADA e guardou a permutacao de linha na matriz "permutacoes"
        #pode realizar eliminacao de Gauss
        eliminacaoGauss(A,i,i+1,n,operacoes)


def criarL(operacoes,permutacoes):
    L = []
    # deve criar (Enx...E1^)
    # onde Ei^ = (Pi+1)X Ei X(Pi+1)
    return L

#operação LU
def operation(A,B,controlCanon):

    #calcular determinante para saber se pode realizar a operacoes (se nao puder disparar erro)
    n = len(A)
    operacoes = []  # matrizes E(eliminações gauss)(a inversa dela é igual a L)
    permutacoes = []  # matrizes P (trocas de linhas) (Pnx...P2xP1xP0)
    criaEscalonada(A,n,operacoes,permutacoes) # ao fim disso A = A' !

    L = criarL(operacoes,permutacoes)

    print(operacoes)
    print()
    print(permutacoes) # ta salvando corretamente
    print(L)






# testando

A = [[1,4,3],[2,5,4],[1/2,-3,-2]]
operation(A,[],False)
print(A)