from src import LU

def main():
    entrada = open("../resource/SISTEMA.txt",'r')
    saida = open("../resource/RESUL.txt",'w+')
    controlReadA = False
    controlReadB = False
    controlTipoInt = False
    controlTipoFloat = False
    controlCannon = False
    A = []
    B = []
    # le a entrada
    for line in entrada:
        # le as configuracoes de precisao do arquivo
        controlTipoInt = True if line=="INT\n" else controlTipoInt
        controlTipoFloat = True if line=="FLOAT\n" else controlTipoFloat

        #identificou um novo sistema
        if(line == "A=\n"):
            saida.write("novo sistema detectado \n")
            saida.write("\n")
            A = []
            B = []
            controlReadA = True

        # terminou de ler a matriz de coeficientes A
        if(controlReadA and line == "\n"):
            #print("A terminou leitura")
            controlReadA = False

        #esta lendo a matriz de coeficientes A
        elif(controlReadA and line != "A=\n"):
            #print(line)
            readA(A,line,controlTipoInt,controlTipoFloat)

        # detectou a matriz B
        #nesse caso se B = CANNONi o sistema entende que você gostaria de calcular a inversa de A
        if(line == "B= CANNONi"):
            B.extend([ [1.0 if i == j else 0.0 for j in range(len(A))]
                        for i in range(len(A)) ])

            #variavel de controle para resolver N sistemas para encontrar a inversa
            controlCannon = True

        # nesse caso o sistema entende que você gostaria resolver um sistema comum por fatoracao LU
        elif(line == "B=\n"):
            controlReadB = True

        # terminou de ler B
        if(controlReadB and line == "\n"):
            print(line)
            controlReadB = False

        # esta lendo B
        elif(controlReadB and line != "B=\n"):
            print(line)
            readB(B,line,controlTipoInt,controlTipoFloat)

        #realiza a operacao LU apos a leitura de A e B do sistema da vez
        if(len(A) != 0 and len(B) != 0 and controlReadA == False and controlReadB == False):
            LU.operation(A,B,controlCannon,saida)
            # SETA controlCannon(variavel que decide se vai resolver N sistemas para inversa) como falso
            controlCannon = False

    #fecha os arquivos
    saida.close()
    entrada.close()

# le os valores para A utilizando a precisao Int ou Float
def readA(A,line,controlTipoInt,controlTipoFloat):
    if(controlTipoInt):
        A.append([ int(x) for x in line.split()])
    if(controlTipoFloat):
        A.append([ float(x) for x in line.split()])

# le os valores para B utilizando a precisao Int ou Float
def readB(B,line,controlTipoInt,controlTipoFloat):
    if (controlTipoInt):
        B.append([float(x) for x in line.split()])
    if (controlTipoFloat):
        B.append([float(x) for x in line.split()])


if __name__ == '__main__':
    main()
