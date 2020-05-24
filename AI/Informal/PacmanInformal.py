from AI.informed_search import *
from AI.utils import Problem


def move_right(x, y, obstacles):
    if x < 9 and [x + 1, y] not in obstacles:
        x += 1
    return x

def move_left(x, y, obstacles):
    if x > 0 and [x - 1, y] not in obstacles:
        x -= 1
    return x

def move_up(x, y, obstacles):
    if y < 9 and [x, y + 1] not in obstacles:
        y += 1
    return y

def move_down(x, y, obstacles):
    if y > 0 and [x, y - 1] not in obstacles:
        y -= 1
    return y

def ProdolziPravo(x, y, nasoka, obstacles):
    x_new = x
    y_new = y
    nasoka_new = nasoka
    if nasoka == 'istok':
        x_new = move_right(x, y, obstacles)
    elif nasoka == 'zapad':
        x_new = move_left(x, y, obstacles)
    elif nasoka == 'sever':
        y_new = move_up(x, y, obstacles)
    else:
        y_new = move_down(x, y, obstacles)

    return x_new, y_new, nasoka_new

def ProdolziNazad(x, y, nasoka, obstacles):
    x_new = x
    y_new = y
    if nasoka == 'istok':
        x_new = move_left(x, y, obstacles)
        nasoka_new = 'zapad'
    elif nasoka == 'zapad':
        x_new = move_right(x, y, obstacles)
        nasoka_new = 'istok'
    elif nasoka == 'sever':
        y_new = move_down(x, y, obstacles)
        nasoka_new = 'jug'
    else:
        y_new = move_up(x, y, obstacles)
        nasoka_new = 'sever'

    return x_new, y_new, nasoka_new

def SvrtiLevo(x, y, nasoka, obstacles):
    x_new = x
    y_new = y
    if nasoka == 'istok':
        y_new = move_up(x, y, obstacles)
        nasoka_new = 'sever'
    elif nasoka == 'zapad':
        y_new = move_down(x, y, obstacles)
        nasoka_new = 'jug'
    elif nasoka == 'sever':
        x_new = move_left(x, y, obstacles)
        nasoka_new = 'zapad'
    else:
        x_new = move_right(x, y, obstacles)
        nasoka_new = 'istok'

    return x_new, y_new, nasoka_new

def SvrtiDesno(x, y, nasoka, obstacles):
    x_new = x
    y_new = y
    if nasoka == 'istok':
        y_new = move_down(x, y, obstacles)
        nasoka_new = 'jug'
    elif nasoka == 'zapad':
        y_new = move_up(x, y, obstacles)
        nasoka_new = 'sever'
    elif nasoka == 'sever':
        x_new = move_right(x, y, obstacles)
        nasoka_new = 'istok'
    else:
        x_new = move_left(x, y, obstacles)
        nasoka_new = 'zapad'

    return x_new, y_new, nasoka_new

class Pacman(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()

        pacman_x = state[0]
        pacman_y = state[1]
        nasoka = state[2]
        dots_position = state[-1]

        pacman_x_new, pacman_y_new, nasoka_new = ProdolziPravo(pacman_x, pacman_y, nasoka, self.obstacles)
        if [pacman_x, pacman_y] != [pacman_x_new, pacman_y_new]:
            successors['ProdolzhiPravo'] = (pacman_x_new, pacman_y_new, nasoka_new,
                                           tuple([d for d in dots_position if d[0] != pacman_x_new or d[1] != pacman_y_new]))

        pacman_x_new, pacman_y_new, nasoka_new = ProdolziNazad(pacman_x, pacman_y, nasoka, self.obstacles)
        if [pacman_x, pacman_y] != [pacman_x_new, pacman_y_new]:
            successors['ProdolzhiNazad'] = (pacman_x_new, pacman_y_new, nasoka_new,
                                            tuple([d for d in dots_position if d[0] != pacman_x_new or d[1] != pacman_y_new]))

        pacman_x_new, pacman_y_new, nasoka_new = SvrtiLevo(pacman_x, pacman_y, nasoka, self.obstacles)
        if [pacman_x, pacman_y] != [pacman_x_new, pacman_y_new]:
            successors['SvrtiLevo'] = (pacman_x_new, pacman_y_new, nasoka_new,
                                            tuple([d for d in dots_position if
                                                   d[0] != pacman_x_new or d[1] != pacman_y_new]))

        pacman_x_new, pacman_y_new, nasoka_new = SvrtiDesno(pacman_x, pacman_y, nasoka, self.obstacles)
        if [pacman_x, pacman_y] != [pacman_x_new, pacman_y_new]:
            successors['SvrtiDesno'] = (pacman_x_new, pacman_y_new, nasoka_new,
                                       tuple([d for d in dots_position if
                                              d[0] != pacman_x_new or d[1] != pacman_y_new]))


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0

    def h(self, node):
        x = node.state[0]
        y = node.state[1]
        dots_position = node.state[-1]
        value = 0
        for x1, y1 in dots_position:
            t = abs(x - x1) + abs(y - y1)
            value = max(value, t)

        return value


dots_position = ()
obstacles_list = [[0, 6], [0, 8], [0, 9], [1, 2], [1, 3], [1, 4], [1, 9], [2, 9], [3, 6], [3, 9],
                  [4, 1], [4, 5], [4, 6], [4, 7], [5, 1], [5, 6], [6, 0], [6, 1], [6, 2], [6, 9],
                  [8, 1], [8, 4], [8, 7], [8, 8], [9, 4], [9, 7], [9, 8]]

pacman_position = [int(input()), int(input())]
nasoka = input()
my_list = []

for i in range(int(input())):
    position = input()
    post = (int(position.split(",")[0]), int(position.split(",")[1]))
    my_list.append(post)

dots_position = tuple(my_list)

pacman = Pacman(obstacles_list, (pacman_position[0], pacman_position[1], nasoka, dots_position))
result = astar_search(pacman)
print(result.solution())





