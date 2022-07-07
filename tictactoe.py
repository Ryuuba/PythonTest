from random import randint
from dataclasses import dataclass, field

def marker_init() -> list[list[int]]:
    return [[3*i+1, 3*i+2, 3*i+3] for i in range(3)]

def cell_status_init() -> dict[int, bool]:
    return dict([(i, False) for i in range(9)])

@dataclass
class TicTacToeBoard:
    """Class modelling a tictactoe board"""
    marker_position: list[list] = field(default_factory=marker_init)
    hline: str = """+-------+-------+-------+"""
    row: str = """|   {}   |   {}   |   {}   |"""
    layout: tuple = (1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1)
    cell_status: dict[int, bool] = field(default_factory=cell_status_init)
    turn_num: int = 9

def display_board(board: TicTacToeBoard):
    """
    The function accepts one parameter containing the board's current status and prints it out to the console.
    
    @param board: A board keeping the game status
    """
    marker_row = 0
    for key in board.layout:
        if key == 1:
            print(board.hline)
        elif key == 2:
            print(board.row.format(' ', ' ', ' '))
        else:
            print(board.row.format(board.marker_position[marker_row][0],
                    board.marker_position[marker_row][1],
                    board.marker_position[marker_row][2]
                )
            )
            marker_row += 1

def enter_move(board: TicTacToeBoard):
    """
    The function accepts the board's current status, asks the user about their move, checks the input, and updates the board according to the user's decision.

    @param board: A board keeping the game status 
    """
    while True:
        try:
            user_input = input('Enter cell number: ')
            cell_number = int(user_input)
            if cell_number not in range(1, 10):
                raise IndexError
            if board.cell_status[cell_number-1]:
                raise Exception
        except KeyboardInterrupt:
            print('Game ends manually')
            raise SystemExit
        except ValueError:
            print('Input {} cannot be processed, try with another cell'.format(
                    user_input
                )
            )
            display_board(board)
        except IndexError:
            print('Cell is not in range [1, 9], try with another cell')
            display_board(board)
        except Exception:
            print('Cell is not free, try with another cell')
            display_board(board)
        else:
            board.marker_position[(cell_number-1)//3][(cell_number-1)%3] = '○'
            board.cell_status[cell_number-1] = True
            board.turn_num -= 1
            break

def draw_move(board: TicTacToeBoard):
    """
    The function draws the computer's move and updates the board.

    @param board: A board keeping the game status 
    """
    print('Computer moves')
    free_cell_list = make_list_of_free_fields(board)
    free_cell_list_len = len(free_cell_list)
    if free_cell_list_len > 0:
        board_cell = free_cell_list[randint(0, free_cell_list_len-1)]
        board.marker_position[board_cell[0]][board_cell[1]] = '×'
        board.cell_status[3*board_cell[0] + board_cell[1]] = True
        board.turn_num -= 1

def make_list_of_free_fields(board: TicTacToeBoard) -> list[tuple[int, int]]:
    """
    The function browses the board and builds a list of all the free squares; the list consists of tuples, while each tuple is a pair of row and column numbers.

    @param board: A board keeping the game status
    """
    free_fields = []
    for key in board.cell_status.keys():
        if not board.cell_status[key]:
            free_fields.append((key//3, key%3))
    return free_fields

def victory_for(board: TicTacToeBoard, sign: str) -> str:
    """
    The function analyzes the board's status in order to check if the player using '○'s or '×'s has won the game

    @param board: A board keeping the game status
    @param sign: the marker
    """
    win = [sign, sign, sign]

    for i in range(3):
        if board.marker_position[i] == win:
            return sign
    
    for j in range(3):
        col = [
            board.marker_position[0][j],
            board.marker_position[1][j],
            board.marker_position[2][j]
        ]
        if col == win:
            return sign

    diag = [
            board.marker_position[0][0],
            board.marker_position[1][1],
            board.marker_position[2][2]
    ]

    if diag == win:
        return sign

    antidiag = [
            board.marker_position[0][2],
            board.marker_position[1][1],
            board.marker_position[2][0]
    ]

    if antidiag == win:
        return sign

    return ''

def main():
    board = TicTacToeBoard()
    result = 'Draw game'
    while board.turn_num > 0:
        if board.turn_num & 1 == 1:
            draw_move(board)
            display_board(board)
            if victory_for(board, '×') == '×':
                result = 'Computer wins'
                break
        else:
            enter_move(board)
            display_board(board)
            if victory_for(board, '○') == '○':
                result = 'You win'
                break
    print(result)
    
if __name__ == '__main__':
    main()