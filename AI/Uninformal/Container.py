from AI.uninformed_search import *

class Container(Problem):
    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)
        self.capacities = capacities

    def successor(self, state):

        successors = dict()

        x, y = state
        c0, c1 = self.capacities

        if x > 0:
            successors['Isprazni go sadot J0'] = (0, y)

        if y > 0:
            successors['Isprazi go sadot J1'] = (x, 0)

        if x > 0 and y < c1:
            delta = min(x, c1 - y)
            successors['Preturi od J0 vo sadot J1'] = (x - delta, y + delta)

        if y > 0 and x < c0:
            delta = min(c0 - x, y)
            successors['Preturi od J1 vo sadot J0'] = (x + delta, y - delta)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


container = Container([15, 15], (5, 5), (10, 0))
result = breadth_first_graph_search(container)
print(result.solution())
