from constraint import *

if __name__ == '__main__':
    n = 6
    problem = Problem()

    domain = []
    for i in range(n):
         domain.append(i)

    # print(domain)

    rooks = range(0, n)

    problem.addVariables(rooks, domain)

    for rook1 in rooks:
        for rook2 in rooks:
            if rook1 < rook2:
                problem.addConstraint(lambda r1, r2: r1 != r2, (rook1, rook2))

    solution = problem.getSolution()
    print(solution)