import re

alphabet = []

rotor_1 = ['E', 'K', 'M', 'F', 'L', 'G,' 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I',
           'B', 'R', 'C', 'J']
rotor_2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y',
           'F', 'V', 'O', 'E']
rotor_3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M',
           'U', 'S', 'Q', 'O']
rotor_4 = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D',
           'C', 'M', 'W', 'B']
rotor_5 = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O',
           'F', 'E', 'C', 'K']

reversal_rotor_1 = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S',
                    'P', 'I', 'K', 'H', 'G', 'D']
reversal_rotor_2 = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z',
                    'C', 'W', 'V', 'J', 'A', 'T']
reversal_rotor_3 = ['F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X', 'W', 'G', 'C', 'T', 'K', 'U', 'Q',
                    'S', 'B', 'N', 'M', 'H', 'L']

board_left = []
board_right = []


def enigma(text, borad_connections, rotor_positioning, shift):
    board_left, board_right = get_board_connections(borad_connections)
    text = text_editing(text)
    text = apply_board_encryption(text, board_left, board_right)
    shift = get_shift_of_rotors(shift)

    char = [char for char in text]


def set_active_rotors(rotor_positioning):
    active_rotors = [char for char in rotor_positioning]


def get_index_of_char_alphabet(char):
    return ord(char) - ord('A')

def get_index_of_char_rotors(char, shift, rotor):
    if rotor == 0:

    elif rotor == 1:

    elif rotor == 2:

    elif rotor == 3:



def get_shift_of_rotors(shift):
    shift = [char for char in shift]
    return shift


def text_editing(text):
    text = text.upper()
    text = re.sub("[^A-Z]", "", text)
    return text


def check_for_transmitt():
    return 0


def get_board_connections(borad_connections):
    global board_right, board_left
    borad_connections = borad_connections.split(" ")

    for i in range(len(borad_connections)):
        board_left.append(borad_connections[i][0])
        board_right.append(borad_connections[i][1])

    return board_left, board_right


def apply_board_encryption(text, board_left, board_right):
    char = [char for char in text]
    for i in range(len(char)):

        for y in range(len(board_right)):

            if char[i] == board_right[y]:
                char[i] = board_left[y]
                break
            elif char[i] == board_left[y]:
                char[i] = board_right[y]
                break

    text = ""
    text += char[i]
    return text


if __name__ == '__main__':
    print(get_index_of_char('A', 0))
    print(get_index_of_char('A', 26))

