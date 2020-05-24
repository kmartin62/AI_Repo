from AI.informed_search import *
from AI.utils import Problem

def D1(lista, x):
    new_lista = list.copy(lista)
    if x < len(new_lista) - 1 and new_lista[x] != 0 and new_lista[x+1]==0:
        element = new_lista[x]
        new_lista[x+1] = element
        new_lista[x] = 0
        return new_lista
    return

def D2(lista, x):
    new_lista = list.copy(lista)
    if x < len(new_lista) - 2 and new_lista[x] != 0 and new_lista[x+1]!=0 and new_lista[x+2] == 0:
        element = new_lista[x]
        new_lista[x+2] = element
        new_lista[x] = 0
        return new_lista
    return

def L1(lista, x):
    new_lista = list.copy(lista)
    if x > 0 and new_lista[x] != 0 and new_lista[x-1]==0:
        element = new_lista[x]
        new_lista[x-1] = element
        new_lista[x] = 0
        return new_lista
    return

def L2(lista, x):
    new_lista = list.copy(lista)
    if x > 1 and new_lista[x] != 0 and new_lista[x-1]!=0 and new_lista[x-2]==0:
        element = new_lista[x]
        new_lista[x-2] = element
        new_lista[x] = 0
        return new_lista
    return




class Diskovi(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        lista = list(state)
        for i in range(len(lista)):
            #D1
            new_lista = D1(lista, i)
            if new_lista != lista and new_lista != None:
                successors['D1: Disk ' + str(lista[i])] = tuple(new_lista)
            #D2
            new_lista = D2(lista, i)
            if new_lista != lista and new_lista != None:
                successors['D2: Disk ' + str(lista[i])] = tuple(new_lista)
            #L1
            new_lista = L1(lista, i)
            if new_lista != lista and new_lista != None:
                successors['L1: Disk ' + str(lista[i])] = tuple(new_lista)
            #L2
            new_lista = L2(lista, i)
            if new_lista != lista and new_lista != None:
                successors['L2: Disk ' + str(lista[i])] = tuple(new_lista)


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        counter = 0

        for x, y in zip(node.state, self.goal):
            if x != y:
                counter += 1


        return counter

N = int(input())
L = int(input())

initial_list = [0] * L

for i in range(N):
    initial_list[i] = i+1

goal_list = initial_list[::-1]
diskovi = Diskovi(tuple(initial_list), tuple(goal_list))
result = astar_search(diskovi)
print(result.solution())

# result1 = greedy_best_first_graph_search(diskovi)
# print(result1.solution())
#
# result2 = recursive_best_first_search(diskovi)
# print(result2.solution())


# for x, y in zip(tuple(initial_list), tuple(goal_list)):
#     print(x, y)