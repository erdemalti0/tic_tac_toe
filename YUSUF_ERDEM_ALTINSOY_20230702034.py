import random

B = [[0,0,0],[0,0,0],[0,0,0]] # CRATE A LIST FOR STORE THE MOVES

print('Welcome to Game of Tic-Tac-Toe')
print('By Yusuf Erdem ALTINSOY')

print('------------------------------')
start = random.randint(1,2) # CHOOSE WHO WILL START THE GAME

if start % 2 == 0:# CHOOSE THE SYMBOLS
    player_symbol = 'X'
    computer_symbol = 'O'
else:
    player_symbol = 'O'
    computer_symbol = 'X'

if start == 1:
    print("You will start the game")
elif start == 2:
    print("I will start the game")

print('------------------------------')

def read_the_player_move():
    while True:
        draw_the_game()
        move = str(input('Your move (Enter 00 to Exit)? ')) # GET THE PLAYER'S MOVE
        if move == '00':# CHECK THE INPUT
            return 'EXIT'
        seperate_move = list(move) # SEPERATE THE MOVE
        for char in seperate_move:
            if char.isnumeric():
                num1 = int(char) - 1
            else:
                if char.lower() == 'a':
                    num2 = 0
                elif char.lower() == 'b':
                    num2 = 1
                elif char.lower() == 'c':
                    num2 = 2
        if B[num1][num2] == 0:
            B[num1][num2] = 2
            break
        else:
            print('------------------------------')
            print('That cell is already full. Try Again.')              
def read_the_computer_move():
    while True:
        num1 = random.randint(0,2)
        num2 = random.randint(0,2)

        if B[num1][num2] == 0:
            B[num1][num2] = 1
        else:
            continue
        break   
def win_or_tie():
    collum = 0
    while collum <= 2:
        if all(x == 1 for x in [B[row][collum] for row in range(3)]):
            draw_the_game()
            print('I win try again')
            return 'Win'
        if all(x == 2 for x in [B[row][collum] for row in range(3)]):
            draw_the_game()
            print('Congratulations. You Win!')
            return 'Win'
        collum += 1

    for moves in B:
        if all(x == 2 for x in moves[:]):
            draw_the_game()
            print('Congratulations. You Win!')
            return 'Win'
        
        elif all(x == 1 for x in moves[:]):
            draw_the_game()
            print('I win try again')
            return 'Win'
    if (B[0][0] == 1 and B[1][1] == 1 and B[2][2] == 1) or (B[0][2] == 1 and B[1][1] == 1 and B[2][0] == 1):
        draw_the_game()
        print('I win try again')
        return 'Win'
    elif (B[0][0] == 2 and B[1][1] == 2 and B[2][2] == 2) or (B[0][2] == 2 and B[1][1] == 2 and B[2][0] == 2):
        draw_the_game()
        print('Congratulations. You Win!')
        return 'Win'    

    if any(0 in x for x in B) == False:
        draw_the_game()
        print('The game is a draw')
        return 'TIE'    
def draw_the_game():
    head_line = '     |  a  |  b  |  c  |'
    line = '-----+-----+-----+-----|'
    last_line = '-----------------------|'
    fundental_line = '  {}  |  {}  |  {}  |  {}  |'
    print(head_line + "\n" + line)
    flat = 1
    while flat <= 3:
        move1 , move2 , move3 = B[flat - 1]
        if move1 == 0:
            move1 = ' '
        if move2 == 0:
            move2 = ' '
        if move3 == 0:
            move3 = ' '
        if move1 == 1:
            move1 = player_symbol
        if move2 == 1:
            move2 = player_symbol
        if move3 == 1:
            move3 = player_symbol
        if move1 == 2:
            move1 = computer_symbol
        if move2 == 2:
            move2 = computer_symbol
        if move3 == 2:
            move3 = computer_symbol
        
        if flat == 3:
            print(fundental_line.format(flat, move1, move2, move3) + '\n' + last_line )
        else:
            print(fundental_line.format(flat, move1, move2, move3) + '\n' + line )
        flat +=1
    print('\n')

while True:
    if start % 2 == 1:
        move = read_the_player_move()
        if move == 'EXIT':
            break
    else:
        read_the_computer_move()
    if win_or_tie() == 'Win':
        break
    elif win_or_tie() == 'TIE':
        break
    start += 1

# NAME: YUSUF ERDEM
# SURNAME: ALTINSOY
# STUDENTID: 20230702034
# LECTURE CSE 101