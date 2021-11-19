#Teste de Python PS Navi
#Natã do Santos Carvalho  
#Engenharia Eletrônica e de Computação - UFRJ
#natancarvalho@poli.ufrj.br 
#GIT HUB: https://github.com/natancarvalho

#Teste 1

def teste1 ():
    targetCount = 0

    for number in range (1, 5000001):
        if (((number % 2) == 0) and ((number % 49)==0) and ((number % 37)==0)):
            targetCount += 1
    print ("Total de numeros pares, multiplos de 49 e multiplos de 37 simultaneamente: ", targetCount)

    return principal()

#teste1()
#------------------------------------------------------------------------------------------------------------

#Teste 2
import math
import numpy as np

#Optei pela utilização das bibliotecas acima para agilizar e facilitar o desenvolvimento 
#do algoritmo.

def teste2 ():
    vectorX = []

    #Como o vetor x possuia 10 posições, não vi necessidade na utilização do vetor v
    #e utilizei a função range () para gerar os valores do vetor x.
    for indexI in range(10):
        if ((indexI % 2) == 0):
            vectorX.append(pow(3, indexI) + (7 * math.factorial(indexI))) 
        else:
            vectorX.append(pow(2, indexI) + (4 * math.log(indexI))) 
    print ("Vetor X: ",vectorX)            

    #Utilizei a função max () para encontrar o maior valor e seu respectivo indice
    #no recem criado vetor x.
    highestIndex = max(vectorX)
    print ("Maior indice: ", vectorX.index(highestIndex))

    mean = round(np.mean(vectorX), 2)
    print ("Media dos elementos do vetor X: ", mean)

    return principal()
#------------------------------------------------------------------------------------------------------------

#Teste 3
#Como não havia especificação, pré determinei nomes no dicionário recebendo pelo terminal
#apenas as notas.

def teste3 ():
    students = ["Nata", "Kobe", "LeBron", "Jordan", "Paul"]                                           
    grades = []

    #Para cada nome, recebe-se uma nota e atribui-se aos nomes no dicionário nas suas 
    #respectivas ordens.

    for index in range (5):
        grades.append(float(input("Nota: ")))

    studentsGrades = {
        students[0] : grades[0],
        students[1] : grades[1],
        students[2] : grades[2],
        students[3] : grades[3],
        students[4] : grades[4]        
    }

    print ("Alunos : Notas\n", studentsGrades)

    #Busca a maior nota e retorna o nome correspondente.
    greaterGrade = max(studentsGrades, key = studentsGrades.get)
    print ("Maior nota: ", greaterGrade)

    return principal()
#------------------------------------------------------------------------------------------------------------

#Função apenas para controlar a execução das tarefas acima.
def principal():
    teste = 4

    print ("Escolha um testes para executar (1 a 3) ou 0 para sair: ")
    teste = input ()

    while teste != "0":
        if teste == "1":
            return teste1 ()
        elif teste == "2":
            return teste2 ()
        elif teste == "3":
            return teste3 ()
        else: 
            print ("Valor incorreto !")
            return principal()

principal ()    