from constraint import *

niza = []


def test():
    elem = niza[0]
    for n in range(1, len(niza) - 1):
        if n > elem:
          return False
    return True


def queens_attacking(q1, q2):
    if abs(q1[0] - q2[0]) != abs(q1[1] - q2[1]):
        return True
    return False


def queens_attacking_hv(q1, q2):
    if q1[0] != q2[0] and q1[1] != q2[1]:
        return True
    return False


if __name__ == '__main__':
    n = int(input())
    problem = Problem()

    domain = [(i, j) for i in range(n) for j in range(n)]

    queens = range(1, n + 1)

    problem.addVariables(queens, domain)

    for queen1 in queens:
        for queen2 in queens:
            if queen1 < queen2:
                problem.addConstraint(queens_attacking, (queen1, queen2))  # diagonal
                problem.addConstraint(queens_attacking_hv, (queen1, queen2))  # horizontal and vertical

    solution = problem.getSolutions()

    print(len(solution) if n <= 6 else problem.getSolution())

    # if n <= 6:
    #     solution = problem.getSolutions()
    #     print(len(solution))
    # else:
    #     solution = problem.getSolution()
    #     print(solution)
