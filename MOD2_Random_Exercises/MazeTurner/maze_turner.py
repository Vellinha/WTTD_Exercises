"""
https://www.reddit.com/r/dailyprogrammer/comments/7aae56/20171102_challenge_338_intermediate_maze_turner/

Our explorer has the following rules:
I always walk 6 blocks straight on and then turn 180° and start walking 6 blocks again
If a wall is in my way I turn to the right, if that not possible I turn to the left and if that is not possible I turn back from where I came.

> : Explorer looking East
< : Explorer looking West
^ : Explorer looking North
v : Explorer looking south
E : Exit
# : wall
  : Clear passage way (empty space)
----------------

Mazes at maps.txt
"""


def load_mazes(map_file):
    map_file = open(map_file, 'r')
    lines = map_file.read().split('\n')
    mazes = []
    maze = ''
    for line in lines:
        if '#' in line:  # is a maze line
            maze += line if maze == '' else '\n' + line
        elif line.strip() == '':
            if maze != '':
                mazes.append(maze)
                maze = ''

    if maze != '':
        mazes.append(maze)

    return mazes


def select_maze(mazes, maze_id):
    maze = ''
    for id, m in enumerate(mazes):
        if id == maze_id:
            maze = m

    if maze.strip() == '':
        return 'Map_not_found'

    width, height = len(maze.split('\n')[0]), len(maze.split('\n'))
    matrix_maze = [[0 for x in range(width)] for y in range(height)]

    x, y = 0, 0
    for char in maze:
        if char == '\n':
            y += 1
            x = 0
            continue

        matrix_maze[y][x] = char
        x += 1

    return matrix_maze


def find_explorer(maze):
    direction = ''

    for row_num, row in enumerate(maze):
        for col_num, char in enumerate(row):
            if char in ('^', '>', '<', 'v'):
                direction = char
                y = row_num
                x = col_num
                break

    return direction, x, y


def walk(explorer, maze):
    """
    I always walk 6 blocks straight on and then turn 180° and start walking 6 blocks again
    """
    print(explorer)
    take_a_step(explorer, maze)


def take_a_step(explorer, maze):
    explorer, looking_at = choose_a_way(explorer, maze)
    explorer = next_step(explorer)

    if looking_at == ' ':
        print(explorer)
        take_a_step(explorer, maze)
    elif looking_at == 'E':
        print(explorer)
        print('I\'m free!')


def take_a_look(explorer, maze):
    _, x, y = next_step(explorer)
    return maze[y][x]


def next_step(explorer):
    direction, x, y = explorer
    if direction == '>':
        x += 1
    elif direction == '<':
        x -= 1
    elif direction == '^':
        y -= 1
    elif direction == 'v':
        y += 1

    return direction, x, y


def choose_a_way(explorer, maze):
    """
    If a wall is in my way I turn to the right,
    if that not possible I turn to the left and if that is not possible I turn back from where I came.
    """
    looking_at = take_a_look(explorer, maze)
    new_direction = explorer[0]
    x, y = explorer[1], explorer[2]

    if looking_at == "#":
        new_direction = turn_right(explorer[0])
        looking_at = take_a_look((new_direction, x, y), maze)

        if looking_at == "#":
            new_direction = turn_left(explorer[0])
            looking_at = take_a_look((new_direction, x, y), maze)

            if looking_at == "#":
                new_direction = turn_around(explorer[0])
                looking_at = take_a_look((new_direction, x, y), maze)

    explorer = new_direction, x, y
    return explorer, looking_at


def turn_right(pos):
    return change_direction(pos)


def turn_left(pos):
    return change_direction(pos, 3)


def turn_around(pos):
    return change_direction(pos, 2)


def change_direction(pos, times=1):
    switcher = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^'
    }

    while times > 0:
        pos = switcher.get(pos)
        times -= 1

    return pos


if __name__ == "__main__":
    mazes = load_mazes('maps.txt')
    # 0, 1, 2, 3, 4, 5, 6
    maze_id = 6
    maze = select_maze(mazes, maze_id)

    if maze == 'Map_not_found':
        print('Map not found for ID ' + str(maze_id))
    else:
        print('Selected maze:')
        [print(m) for m in maze]
        print('\n')

        explorer = find_explorer(maze)
        walk(explorer, maze)

