import os
import random


def clear_terminal():
    os.system('cls')


class Board:
    def __init__(self):
        self.board = [' '] * 10

    def draw_board(self):
        print(f' {self.board[7]} | {self.board[8]} | {self.board[9]} ')
        print(f'-----------')
        print(f' {self.board[4]} | {self.board[5]} | {self.board[6]} ')
        print(f'-----------')
        print(f' {self.board[1]} | {self.board[2]} | {self.board[3]} ')


class Player:
    def __init__(self):
        self.marker = ''


class Game:
    def __init__(self):
        self.the_board = Board()
        self.player = Player()
        self.ai = Player()
        self.player.marker, self.ai.marker = self.choose_marker()

    def choose_marker(self):
        marker = ''
        while (marker not in ['X', 'O']):
            marker = input('Player choose X or O: ').upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

    def choose_first(self):
        flip = random.randint(1, 2)
        if flip == 1:
            return 'Player'
        else:
            return 'AI'

    def validate_position(self, board, pos):
        if (1 <= pos <= 9):
            if board.board[pos] == ' ':
                return True
        return False

    def place_marker(self, board, pos, mark):
        board.board[pos] = mark

    def check_win(self, mark):
        return (self.the_board.board[7] == self.the_board.board[8] == self.the_board.board[9] == mark or
                self.the_board.board[4] == self.the_board.board[5] == self.the_board.board[6] == mark or
                self.the_board.board[1] == self.the_board.board[2] == self.the_board.board[3] == mark or
                self.the_board.board[7] == self.the_board.board[4] == self.the_board.board[1] == mark or
                self.the_board.board[8] == self.the_board.board[5] == self.the_board.board[2] == mark or
                self.the_board.board[9] == self.the_board.board[6] == self.the_board.board[3] == mark or
                self.the_board.board[7] == self.the_board.board[5] == self.the_board.board[3] == mark or
                self.the_board.board[1] == self.the_board.board[5] == self.the_board.board[9] == mark)

    def full_board_check(self):
        for i in range(1, 10):
            if self.the_board.board[i] == ' ':
                return False
        return True

    def replay(self):
        return input('Play again? enter Y or N: ').lower().startswith('y')


print('Welcome to Tic-Tac-Toe Game..!\n')


game_on = True


while True:

    game = Game()

    turn = game.choose_first()
    print(turn + ' goes first..')

    game.the_board.draw_board()

    winner = ''

    while game_on:

        if turn == 'Player':
            position = 0
            while (game.validate_position(game.the_board, position) == False):
                position = int(input('Enter a number between 1 - 9:\n'))
            game.place_marker(game.the_board, position, game.player.marker)

            clear_terminal()
            game.the_board.draw_board()

            if game.check_win(game.player.marker):
                winner = turn
                break

            if game.full_board_check():
                break

            turn = 'AI'
            print(f"AI's turn [{game.ai.marker}]")

        elif turn == 'AI':
            position = 0
            while (game.validate_position(game.the_board, position) == False):
                position = random.randint(1, 9)
            game.place_marker(game.the_board, position, game.ai.marker)

            clear_terminal()
            game.the_board.draw_board()

            if game.check_win(game.ai.marker):
                winner = turn
                break

            if game.full_board_check():
                break

            turn = 'Player'
            print(f"Player's turn [{game.player.marker}]")

    if winner:
        print(winner + ' Won the match!')
    else:
        print('Game ended in a Tie!')

    if game.replay():
        continue
    else:
        break