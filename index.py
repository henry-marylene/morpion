

map = [
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . ']
]

player = 'Player 1'

def draw():
    for i in range(3):
        for j in range(3):
            print(map[i][j], end="")
        print()

def check_win():
    for i in range(3):
        if map[i][0] == map[i][1] == map[i][2] != ' . ' :
        # map[i][0] != ' . ' and map[i][0] == map[i][1] == map[i][2]:
        # (map[i][0] == map[i][1]) and  ( map[i][1] == map[i][2])
            return True
    
    for j in range(3):
        if map[0][j] == map[1][j] == map[2][j] != ' . ' :
            return True
    
    if map[0][0] == map[1][1] == map[2][2] != ' . ' :
        return True
    
    elif map[0][2] == map[1][1] == map[2][0] != ' . ' :
        return True
    return False


def check_equality():
    for i in range(3):
        for j in range(3):
            if map[i][j] == ' . ':
                return False 
    return True

draw()
while True:
    choice = int(input(f'{player} [1-9] ? > '))
    row = (choice - 1)//3
    column = (choice - 1) % 3

    if map[row][column] == ' . ':
        map[row][column] = ' X ' if player == 'Player 1' else ' O '
    draw()
    if check_win():
        print(f'{player} : You win !')
        break
    if check_equality():
        print('Equals')
        break
    player = 'Player 1' if player == 'Player 2' else 'Player 2'

    