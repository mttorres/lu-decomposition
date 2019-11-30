

#cria matriz identidade para facilitar operações
def criaIdentidade(n):
    return [[1.0 if i == j else 0.0 for j in range(n)]
                for i in range(n)]


#troca linha 1 por linha 2
def trocaLinha(a,lineindex1,lineindex2):
    temp = a[lineindex1]
    a[lineindex1] = a[lineindex2]
    a[lineindex2] = temp

#realiza a operação de eliminação de gaus para cada membro da linha: li = aij - (aij/pivo)*(linhaPivo)
def eliminacaoGauss(a,pivoindex,lineindex):
    a[lineindex] =  [
            (a[lineindex][x] - ( (a[lineindex][x]/a[pivoindex][pivoindex] )*a[pivoindex][x] ) )
            for x in range(0,len(a[lineindex]))
            ]


def PivoteamentoParcial(A,permutacoes,n,posXpivo):
    mudanca = posXpivo
    #posXpivo = i # fixamos o 0,0 como inicio (depois é 1,1, ... n,n)
    #é alguma das linhas da vez da chamada
    while(posXpivo < n):
        maior = A[posXpivo][posXpivo] # recebe 0,0 ou 1,1 .. nn

        for i in range(1+posXpivo,n):
            if(maior < A[i][posXpivo]):
                maior = A[i][posXpivo]
                mudanca = i

        if(mudanca != posXpivo):
            permutacoes = trocaLinha(A,posXpivo,mudanca)








#cria a matriz A' (após pivoteamento parcial)
def criaEscalonada(A,n):
    operacoes = [] # matrizes E(eliminações gauss)
    permutacoes = [] # matrizes P (trocas de linhas
    return A




#operação LU
def operation(A,B,controlCanon):
    n = len(A)

    L = criaIdentidade(n)
    U = criaEscalonada(A,n)

    #print()
    #print(L)


