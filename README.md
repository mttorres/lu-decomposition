# lu-decomposition
Trabalho de Métodos Numéricos:

Implementar um programa em linguagem de programação para resolver m sistemas de n
equações com n incógnitas pelo método da Fatoração LU com a estratégia do pivoteamento
parcial. 




Como rodar o programa? 

0. Edite o arquivo SISTEMA na pasta /resource e informe os valores desejados da seguinte forma:
    
    A=
    linha1
    ...
    linhaN
    
    B=
    linha1
    ...
    linhaN
    
    ou (caso deseje calcular a inversa da matriz A)(calcular a inversa por fatoração LU)
    
    A=
    linha1
    ...
    linhaN
    
    B= CANNONi 
    
    *Existem exemplos de entrada na pasta /resource.
    
1. Entre no virtual environment:
    
    * On **Linux** or **macOS**:
    ```sh
    source ./bin/activate 
    ```

    * On **Windows**:
    ```sh
    ./Scripts/activate 
    ```
2. Instale os pacotes usando pip(nesse caso o numpy): 
    ```sh
    pip install package-name
    ``` 
3. Leave the virtual environment:
    ```sh
    deactivate
    ```

Ou baixe o projeto e rode no Pycharm, acredito que ele já resolva as dependências.
  
  
## About
uses the Python *Numpy** to perform matrix arithmetics. 

**Project for UFF 2019.1 TCC 00.306  Numerical Methods.**
