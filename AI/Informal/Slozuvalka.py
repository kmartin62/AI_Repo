from AI.informed_search import *
from AI.utils import Problem

class Slozuvalka(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        ind = state.index('*')

        if ind >= 3:
            tmp = list(state)
            tmp[ind], tmp[ind - 3] = tmp[ind - 3], tmp[ind]
            new_state = ''.join(tmp)
            successors['Gore'] = new_state

        if ind <= 5:
            tmp = list(state)
            tmp[ind], tmp[ind + 3] = tmp[ind + 3], tmp[ind]
            new_state = ''.join(tmp)
            successors['Dolu'] = new_state

        if ind % 3 != 0:
            tmp = list(state)
            tmp[ind], tmp[ind - 1] = tmp[ind - 1], tmp[ind]
            new_state = ''.join(tmp)
            successors['Levo'] = new_state

        if ind % 3 != 2:
            tmp = list(state)
            tmp[ind], tmp[ind + 1] = tmp[ind + 1], tmp[ind]
            new_state = ''.join(tmp)
            successors['Desno'] = new_state


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return super().goal_test(state)

    def h(self, node):
        counter = 0

        for x, y in zip(node.state, self.goal):
            if x != y:
                counter += 1

        return counter

slozuvalka = Slozuvalka('*32415678', '*12345678')
result1 = greedy_best_first_graph_search(slozuvalka)
print(result1.solution())

result2 = astar_search(slozuvalka)
print(result2.solution())

result3 = recursive_best_first_search(slozuvalka)
print(result3.solution())