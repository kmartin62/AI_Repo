from constraint import *

if __name__ == '__main__':

    lista = list()
    algorithm = input()

    if algorithm == 'BacktrackingSolver':
        problem = Problem()
    elif algorithm == 'RecursiveBacktrackingSolver':
        problem = Problem(RecursiveBacktrackingSolver())
    else:
        problem = Problem(MinConflictsSolver())

    problem.addVariables(range(0, 81), range(1, 10))

    #Horizontalno
    for i in range(9):
        problem.addConstraint(AllDifferentConstraint(), [9 * i + j for j in range(9)])


    #Vertikalno
    for i in range(9):
        problem.addConstraint(AllDifferentConstraint(), [j * 9 + i for j in range(9)])

    #3x3 matrici

    #3x3 matrici vo prvite 3 koloni [0, 1, 2, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38, 45, 46, 47..]
    for i in range(9):
        if i % 3 == 0 and i != 0:
            problem.addConstraint(AllDifferentConstraint(), lista)
            lista = list()
        for j in range(3):
            lista.append(9 * i + j)
        if i == 8:
            problem.addConstraint(AllDifferentConstraint(), lista)

    #3x3 matrici vo 3-5ta kolona [3, 4, 5, 12, 13, 14, 21, 22, 23, 30, 31, 32, 39, 40, 41, 48, 49, 50..]
    lista = list()
    for i in range(9):
        if i % 3 == 0 and i != 0:
            problem.addConstraint(AllDifferentConstraint(), lista)
            lista = list()
        for j in range(3):
            lista.append(9 * i + j + 3)
        if i == 8:
            problem.addConstraint(AllDifferentConstraint(), lista)

    #3x3 matrici vo poslednite 3 koloni [6, 7, 8, 15, 16, 17, 24, 25, 26, 33, 34, 35, 42, 43, 44, 51, 52, 53..]
    lista = list()
    for i in range(9):
        if i % 3 == 0 and i != 0:
            problem.addConstraint(AllDifferentConstraint(), lista)
            lista = list()
        for j in range(3):
            lista.append(9 * i + j + 6)
        if i == 8:
            problem.addConstraint(AllDifferentConstraint(), lista)


    solution = problem.getSolution()
    print(solution)