# problem.addConstraint(AllDifferentConstraint(), [0, 1, 2, 3, 4, 5, 6, 7, 8])
# problem.addConstraint(AllDifferentConstraint(), [9, 10, 11, 12, 13, 14 ,15 ,16, 17])
# problem.addConstraint(AllDifferentConstraint(), [18, 19, 20, 21, 22, 23, 24, 25, 26])
# problem.addConstraint(AllDifferentConstraint(), [27, 28, 29, 30, 31, 32, 33, 34, 35])
# problem.addConstraint(AllDifferentConstraint(), [36, 37, 38, 39, 40, 41, 42, 43, 44])
# problem.addConstraint(AllDifferentConstraint(), [45, 46, 47, 48, 49, 50, 51, 52, 53])
# problem.addConstraint(AllDifferentConstraint(), [54, 55, 56, 57, 58, 59, 60, 61, 62])
# problem.addConstraint(AllDifferentConstraint(), [63, 64, 65, 66, 67, 68, 69, 70, 71])
# problem.addConstraint(AllDifferentConstraint(), [72, 73, 74, 75, 76, 77, 78, 79, 80])



# problem.addConstraint(AllDifferentConstraint(), [0, 9, 18, 27, 36, 45, 54, 63, 72])
    # #0 - 9 - 18 - 27 - 36 - 45 - 54 - 63 - 72
    # problem.addConstraint(AllDifferentConstraint(), [1, 10, 19, 28, 37, 46, 55, 64, 73])
    # #1 - 10 - 19 - 28 - 37 - 46 - 55 - 64 - 73
    # problem.addConstraint(AllDifferentConstraint(), [2, 11, 20, 29, 38, 47, 56, 65, 74])
    # #2 - 11 - 20 - 29 - 38 - 47 - 56 - 65 - 74
    # problem.addConstraint(AllDifferentConstraint(), [3, 12, 21, 30, 39, 48, 57, 66, 75])
    # #3 - 12 - 21 - 30 - 39 - 48 - 57 - 66 - 75
    # problem.addConstraint(AllDifferentConstraint(), [4, 13, 22, 31, 40, 49, 58, 67, 76])
    # #4 - 13 - 22 - 31 - 40 - 49 - 58 - 67 - 76
    # problem.addConstraint(AllDifferentConstraint(), [5, 14, 23, 32, 41, 50, 59, 68, 77])
    # #5 - 14 - 23 - 32 - 41 - 50 - 59 - 68 - 77
    # problem.addConstraint(AllDifferentConstraint(), [6, 15, 24, 33, 42, 51, 60, 69, 78])
    # #6 - 15 - 24 - 33 - 42 - 51 - 60 - 69 - 78
    # problem.addConstraint(AllDifferentConstraint(), [7, 16, 25, 34, 43, 52, 61, 70, 79])
    # #7 - 16 - 25 - 34 - 43 - 52 - 61 - 70 - 79
    # problem.addConstraint(AllDifferentConstraint(), [8, 17, 26, 35, 44, 53, 62, 71, 80])
    #8 - 17 - 26 - 35 - 44 - 53 - 62 - 71 - 80



# problem.addConstraint(AllDifferentConstraint(), [0, 1, 2, 9, 10, 11, 18, 19, 20])

# lista = [9 * i + j for i in range(3) for j in range(3)]
# problem.addConstraint(AllDifferentConstraint(), [9 * i + j for i in range(3) for j in range(3)])
# problem.addConstraint(AllDifferentConstraint(), [27, 28, 29, 36, 37, 38, 45, 46, 47])
# problem.addConstraint(AllDifferentConstraint(), [54, 55, 56, 63, 64, 65, 72, 73, 74])

# problem.addConstraint(AllDifferentConstraint(), [3, 4, 5, 12, 13, 14, 21, 22, 23])
# problem.addConstraint(AllDifferentConstraint(), [30, 31, 32, 39, 40, 41, 48, 49, 50])
# problem.addConstraint(AllDifferentConstraint(), [57, 58, 59, 66, 67, 68, 75, 76, 77])

# problem.addConstraint(AllDifferentConstraint(), [6, 7, 8, 15, 16, 17, 24, 25, 26])
# problem.addConstraint(AllDifferentConstraint(), [33, 34, 35, 42, 43, 44, 51, 52, 53])
# problem.addConstraint(AllDifferentConstraint(), [60, 61, 62, 69, 70, 71, 78, 79, 80])

lista = list()
for i in range(9):
    for j in range(3):
        lista.append(9 * i + j + 6)


# print(lista)