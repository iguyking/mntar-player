
from collections import namedtuple
import copy
import logging

logging.basicConfig(level=logging.DEBUG, format= '%(message)s')

# Legend:
#    X = Nothing (not part of maze)
#    W = White
#    B = Blue
#    G = Green
#    Br= Brown
#    O = Orange
#    E = Exit
#    S = Start

# Maze to follow - 0,0 location is upper left corner
MAZE = [ ['X', 'W', 'B', 'E', 'W', 'W', 'W', 'X'],
        ['W', 'W', 'G', 'W', 'G', 'W', 'W', 'W'],
        ['W', 'G', '2', '?', 'B', 'W', 'W', 'W']
    ]

# Color Rotation groupings
GRAPH = {
    'O': {
        'W': 'G',
        'G': 'B',
        'B': 'W'
    },
    'Br': {
        'W': 'B',
        'B': 'G', 
        'G': 'W'
    }
}

# Defines all the details of a given switch port and how it should work
SwitchPort = namedtuple('SwitchPort', 'x y color')
SWITCH = {
    '1': [
        SwitchPort( 1,-1, 'O'), SwitchPort( 1,0, 'Br'), SwitchPort( 1,1, 'O'),
        SwitchPort( 0,-1, 'O'),                         SwitchPort( 0,1, 'O'),
        SwitchPort(-1,-1, 'O'), SwitchPort(-1,0, 'Br'), SwitchPort(-1,1, 'O')
        ]
}

# References a location in the maze
LocationTracking = namedtuple('Location', 'x y')

# Print maze in a visual format
def print_maze(daMaze):
    for row in daMaze:
        for spot in row:
            print(f" {spot} ", end='')
        print("")

def can_i_move(daMaze, location) -> bool:
    VALID_MOVES = ['W', '1', '2', '?']
    if daMaze[location.x][location.y] in set(VALID_MOVES):
        return True
    else:
        return False

PATH_TAKEN = []


print("Starting Maze")
print_maze(MAZE)



location = LocationTracking(0,3)

# Create the next step of the MAZE
NEXTMAZE = copy.deepcopy(MAZE)

def update_maze_with_switch(switch_taken, maze_step):
#TODO: Assuming location is switch setting of '1' and is valid member of SWITCH
    for port in SWITCH[switch_taken]:
        #print(port)
        x = location.x + port.x
        y = location.y + port.y
        color = port.color
    # MAZE starts counting at 0
        if x >= len(maze_step) or (x < 0): 
            continue
        if y >= len(maze_step[0]) or (y < 0):
            continue
    # The port is within the confines of the Maze so update the maze location with the graph loop
        current_value = maze_step[x][y]
        future_value = GRAPH[color][maze_step[x][y]]
        logging.debug(f"Now turning {x},{y} from {current_value} into {future_value} using color of {color}")
        maze_step[x][y] = future_value
        logging.debug(print_maze(maze_step))
    

update_maze_with_switch('1', NEXTMAZE)
# TODO: Loop to ask for which way to go
# TODO: Track each step, maze as going through it (to ultimately get to the solver)
# TODO: Remember - X is up and down, y is left to right (Do I want to change that to be proper X/Y)
