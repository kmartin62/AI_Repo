from AI.uninformed_search import *

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

        x_new = move_right(pacman_x, pacman_y, self.obstacles)
        if x_new != pacman_x:
            successors['Right'] = (x_new, pacman_y, nasoka, tuple([d for d in dots_position if d[0] != x_new or d[1] != pacman_y]))

        x_new = move_left(pacman_x, pacman_y, self.obstacles)
        if x_new != pacman_x:
            successors['Left'] = (x_new, pacman_y, nasoka, tuple([d for d in dots_position if d[0] != x_new or d[1] != pacman_y]))

        y_new = move_up(pacman_x, pacman_y, self.obstacles)
        if y_new != pacman_y:
            successors['Up'] = (pacman_x, y_new, nasoka, tuple([d for d in dots_position if d[0] != pacman_x or d[1] != y_new]))

        y_new = move_down(pacman_x, pacman_y, self.obstacles)
        if y_new != pacman_y:
            successors['Down'] = (pacman_x, y_new, nasoka, tuple([d for d in dots_position if d[0] != pacman_x or d[1] != y_new]))


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0


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
result = breadth_first_graph_search(pacman)

print(result.solution())




