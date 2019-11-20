from src import LU

def main():
    entrada = open("../resource/SISTEMA")
    controlReadA = False
    controlReadB = False
    controlTipoInt = False
    controlTipoFloat = False
    controlCanno = False

    for line in entrada:


        controlTipoInt = True if line=="INT\n" else controlTipoInt
        controlTipoFloat = True if line=="FLOAT\n" else controlTipoFloat


        if(line == "A=\n"):
            #print("novo sistema detectado")
            A = []
            B = []
            controlReadA = True

        if(controlReadA and line == "\n"):
            #print("A terminou leitura")
            controlReadA = False

        elif(controlReadA and line != "A=\n"):
            #print(line)
            readA(A,line,controlTipoInt,controlTipoFloat)


        if(line == "B= CANNONi"):
            B.extend([ [1 if i == j else 0 for j in range(len(A))]
                        for i in range(len(A)) ])
            controlCanno = True

        elif(line == "B=\n"):
            controlReadB = True

        if(controlReadB and line == "\n"):
            print(line)
            controlReadB = False

        elif(controlReadB and line != "B=\n"):
            print(line)
            readB(B,line,controlTipoInt,controlTipoFloat)

    print("operandos:")
    print(A)
    print()
    print(B)
    LU.operation(A,B,controlCanno)
    controlCanno = False
    entrada.close()

def readA(A,line,controlTipoInt,controlTipoFloat):
    if(controlTipoInt):
        A.append([ int(x) for x in line.split()])
    if(controlTipoFloat):
        A.append([ float(x) for x in line.split()])

def readB(B,line,controlTipoInt,controlTipoFloat):
    if (controlTipoInt):
        B.append([int(x) for x in line.split()])
    if (controlTipoFloat):
        B.append([float(x) for x in line.split()])


if __name__ == '__main__':
    main()
