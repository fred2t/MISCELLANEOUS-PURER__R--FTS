# v computer
from typing import Callable, List, Union
import random

Board = List[List[int]]
class TicTacToe:
    def __init__(self) -> None:
        self.board: Board = [
                            ['+', '+', '+'],
                            ['+', '+', '+'],
                            ['+', '+', '+']]

    def showBoard(self) -> None:
        print('The Board')

        for row in self.board:
            print()            
            for column in row:
                print(column, end=' ')

    def playerMove(self):
        print('\nMake your move')
        row, column = int(input('Row: ')), int(input('Column: '))

        if self.isEmpty(row, column):
            self.board[row - 1][column - 1] = 'X'
            
        else: 
            self.showBoard()
            print("\nThat is taken")
            self.playerMove()
        self.showBoard()

    def computerMove(self) -> bool:
        if not self.stillSpace(): return False

        computerRow, computerColumn = random.randint(1, 3), random.randint(1, 3)
        if self.isEmpty(computerRow, computerColumn):
            self.board[computerRow - 1][computerColumn - 1] = 'O'
        
        else:
            self.computerMove()
        print('\nComputer Moved')
        self.showBoard()

    def isEmpty(self, row: int, column: int) -> bool:
        # taken = 
        return self.board[row - 1][column - 1] == '+'
        
    def stillSpace(self) -> bool:
        for row in self.board:
            for spot in row:
                if spot == '+':
                    return True
        return False

    def gameOver(self):
        for row in self.board:
            if all(play == row[0] for play in row) and row[0] == 'X':
                return '\nYou Win'
            elif all(play == row[0] for play in row) and row[0] == 'O':
                return '\nYou Lose'

        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] == 'X':
                return '\nYou Win'
            elif self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] == 'O':
                return '\nYou Lose'

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] == 'X':
            return '\nYou Win'
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] == 'X':
            return '\nYou Win'

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] == 'O':
            return '\nYou Lose'
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] == 'O':
            return '\nYou Lose'

        if not self.stillSpace():
            return '\nTie'

game = TicTacToe()

game.showBoard()
# while anything empty, keep playihng
while game.stillSpace():
    game.playerMove()
    game.computerMove()
    if game.gameOver():
        print(game.gameOver())
        break
