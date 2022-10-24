import random


def check_win(view):

    return view[0][0] == view[0][2] == view[0][4] != ' ' or view[2][0] == view[2][2] == view[2][4] != ' ' or \
            view[4][0] == view[4][2] == view[4][4] != ' ' or view[0][0] == view[2][0] == view[4][0] != ' ' or \
            view[2][0] == view[2][2] == view[2][4] != ' ' or view[4][0] == view[4][2] == view[4][4] != ' ' or \
            view[0][0] == view[2][2] == view[4][4] != ' ' or view[0][4] == view[2][2] == view[4][0] != ' '


if __name__ == '__main__':
    print('info : choose a number between 1-9')
    view = [[' ', '|', ' ', '|', ' '], ['_', ' ', '_', ' ', '_'], [' ', '|', ' ', '|', ' '], ['_', ' ', '_', ' ', '_'], [' ', '|', ' ', '|', ' ']]

    play_cells = {
        1: '00',
        2: '02',
        3: '04',
        4: '20',
        5: '22',
        6: '24',
        7: '40',
        8: '42',
        9: '44'
    }

    cpu = ''
    player_alpha = input('choose X or O : ')

    # define the players
    if player_alpha == 'X':
        cpu = 'O'
    elif player_alpha == 'O':
        cpu = 'X'
    else:
        cpu = 'O'
        player_alpha = 'X'

    while True:
        play_player = input('give a number : ')

        play_player = play_cells[int(play_player)]
        view[int(play_player[0])][int(play_player[1])] = player_alpha

        if check_win(view):
            print('Congra! you won the game !')
            break
        print('\n'.join([''.join(item) for item in view]))

        print('computer play now : ')

        def get_random_value():
            ran = random.randint(1, 9)

            ran = play_cells[ran]
            if view[int(ran[0])][int(ran[1])] == ' ':
                view[int(ran[0])][int(ran[1])] = cpu
            else:
                get_random_value()

        get_random_value()

        if check_win(view):
            print('Congra! you won the game !')
            break

        print('\n'.join([''.join(item) for item in view]))
