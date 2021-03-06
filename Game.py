import numpy as np
from colored import fg, bg, attr
from AI import *


class Game(object):
    def __init__(self, col, row, playerNum):
        self.row = row
        self.col = col
        self.players = playerNum
        self.board = np.zeros((self.row, self.col))
        self.player1 = []
        self.player2 = []

    def __repr__(self):
        pass

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getMoves(self, player):
        moveList = []
        for i in range(self.getRow()):
            for j in range(self.getCol()):
                if self.board[i][j] == 0:
                    moveList.append((i, j))
        return moveList

    def makeMove(self, row, col, player):
        if player == 1:
            self.player1.append([row, col])
        else:
            self.player2.append([row, col])

        if (row, col) in self.getMoves(1):
            self.board[row][col] = player
        else:
            pass

    def resetMove(self, row, col):
        self.board[row][col] = 0
        if [row, col] in self.player1:
            self.player1.remove([row, col])
        else:
            self.player2.remove([row, col])

    def checkWin(self):
        pass

    def resetBoard(self):
        self.board = np.zeros((self.row, self.col))
        self.player1 = []
        self.player2 = []


class TicTacToe(Game):
    def __init__(self):
        super(TicTacToe, self).__init__(3, 3, 2)
        self.name = 'TicTacToe'

    def __repr__(self):
        print_string = ''
        for i in range(self.getRow()):
            for j in range(self.getCol()):
                if self.board[i][j] == 1:
                    print_string = print_string + '|{}{}  {}|'.format(fg(1), bg(196), attr(0))
                elif self.board[i][j] == -1:
                    print_string = print_string + '|{}{}  {}|'.format(fg(4), bg(21), attr(0))
                else:
                    print_string = print_string + '|{}{:^2}{}|'.format(bg(0), i * 3 + j, attr(0))
            print_string = print_string + '\n'
        return print_string

    def getName(self):
        return self.name

    def checkWin(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0:
            return self.board[0][0]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != 0:
            return self.board[1][0]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != 0:
            return self.board[2][0]
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != 0:
            return self.board[0][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != 0:
            return self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != 0:
            return self.board[0][2]
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        elif not self.getMoves(1):
            return 0
        else:
            return None


class ConnectFour(Game):
    def __init__(self):
        super(ConnectFour, self).__init__(7, 6, 2)
        self.name = 'ConnectFour'
        self.player1 = []
        self.player2 = []

    def __repr__(self):
        print_string = ''
        for i in range(self.getRow()):
            for j in range(self.getCol()):
                if self.board[i][j] == 1:
                    print_string = print_string + '|{}{}  {}|'.format(fg(1), bg(196), attr(0))
                elif self.board[i][j] == -1:
                    print_string = print_string + '|{}{}  {}|'.format(fg(100), bg(226), attr(0))
                else:
                    print_string = print_string + '|{}{}  {}|'.format(fg(0), bg(0), attr(0))
            print_string = print_string + '\n'
        return print_string

    def getName(self):
        return self.name

    def getMoves(self, player):
        move_list = []
        for j in range(self.getCol()):
            for i in range(self.getRow() - 1, -1, -1):
                if self.board[i][j] == 0:
                    move_list.append([i, j])
                    break
        return move_list

    def makeMove(self, row, col, player):
        if [row, col] in self.getMoves(1):
            self.board[row][col] = player
            if player == 1:
                self.player1.append([row, col])
            else:
                self.player2.append([row, col])

    def checkWin(self):
        if self.board[5][0] == self.board[5][1] == self.board[5][2] == self.board[5][3] != 0:
            return self.board[5][0]
        elif self.board[5][1] == self.board[5][2] == self.board[5][3] == self.board[5][4] != 0:
            return self.board[5][1]
        elif self.board[5][2] == self.board[5][3] == self.board[5][4] == self.board[5][5] != 0:
            return self.board[5][2]
        elif self.board[5][3] == self.board[5][4] == self.board[5][5] == self.board[5][6] != 0:
            return self.board[5][3]
        elif self.board[4][0] == self.board[4][1] == self.board[4][2] == self.board[4][3] != 0:
            return self.board[4][0]
        elif self.board[4][1] == self.board[4][2] == self.board[4][3] == self.board[4][4] != 0:
            return self.board[4][1]
        elif self.board[4][2] == self.board[4][3] == self.board[4][4] == self.board[4][5] != 0:
            return self.board[4][2]
        elif self.board[4][3] == self.board[4][4] == self.board[4][5] == self.board[4][6] != 0:
            return self.board[4][3]
        elif self.board[3][0] == self.board[3][1] == self.board[3][2] == self.board[3][3] != 0:
            return self.board[3][0]
        elif self.board[3][1] == self.board[3][2] == self.board[3][3] == self.board[3][4] != 0:
            return self.board[3][1]
        elif self.board[3][2] == self.board[3][3] == self.board[3][4] == self.board[3][5] != 0:
            return self.board[3][2]
        elif self.board[3][3] == self.board[3][4] == self.board[3][5] == self.board[3][6] != 0:
            return self.board[3][3]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == self.board[2][3] != 0:
            return self.board[2][0]
        elif self.board[2][1] == self.board[2][2] == self.board[2][3] == self.board[2][4] != 0:
            return self.board[2][1]
        elif self.board[2][2] == self.board[2][3] == self.board[2][4] == self.board[2][5] != 0:
            return self.board[2][2]
        elif self.board[2][3] == self.board[2][4] == self.board[2][5] == self.board[5][6] != 0:
            return self.board[2][3]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == self.board[1][3] != 0:
            return self.board[1][0]
        elif self.board[1][1] == self.board[1][2] == self.board[1][3] == self.board[1][4] != 0:
            return self.board[1][1]
        elif self.board[1][2] == self.board[1][3] == self.board[1][4] == self.board[1][5] != 0:
            return self.board[1][2]
        elif self.board[1][3] == self.board[1][4] == self.board[1][5] == self.board[1][6] != 0:
            return self.board[1][3]
        elif self.board[0][0] == self.board[0][1] == self.board[0][2] == self.board[0][3] != 0:
            return self.board[0][0]
        elif self.board[0][1] == self.board[0][2] == self.board[0][3] == self.board[0][4] != 0:
            return self.board[0][1]
        elif self.board[0][2] == self.board[0][3] == self.board[0][4] == self.board[0][5] != 0:
            return self.board[0][2]
        elif self.board[0][3] == self.board[0][4] == self.board[0][5] == self.board[0][6] != 0:
            return self.board[0][3]
        elif self.board[5][0] == self.board[4][0] == self.board[3][0] == self.board[2][0] != 0:
            return self.board[5][0]
        elif self.board[5][1] == self.board[4][1] == self.board[3][1] == self.board[2][1] != 0:
            return self.board[5][1]
        elif self.board[5][2] == self.board[4][2] == self.board[3][2] == self.board[2][2] != 0:
            return self.board[5][2]
        elif self.board[5][3] == self.board[4][3] == self.board[3][3] == self.board[2][3] != 0:
            return self.board[5][3]
        elif self.board[5][4] == self.board[4][4] == self.board[3][4] == self.board[2][4] != 0:
            return self.board[5][4]
        elif self.board[5][5] == self.board[4][5] == self.board[3][5] == self.board[2][5] != 0:
            return self.board[5][5]
        elif self.board[5][6] == self.board[4][6] == self.board[3][6] == self.board[2][6] != 0:
            return self.board[5][6]
        elif self.board[4][0] == self.board[3][0] == self.board[2][0] == self.board[1][0] != 0:
            return self.board[4][0]
        elif self.board[4][1] == self.board[3][1] == self.board[2][1] == self.board[1][1] != 0:
            return self.board[4][1]
        elif self.board[4][2] == self.board[3][2] == self.board[2][2] == self.board[1][2] != 0:
            return self.board[4][2]
        elif self.board[4][3] == self.board[3][3] == self.board[2][3] == self.board[1][3] != 0:
            return self.board[4][3]
        elif self.board[4][4] == self.board[3][4] == self.board[2][4] == self.board[1][4] != 0:
            return self.board[4][4]
        elif self.board[4][5] == self.board[3][5] == self.board[2][5] == self.board[1][5] != 0:
            return self.board[4][5]
        elif self.board[4][6] == self.board[3][6] == self.board[2][6] == self.board[1][6] != 0:
            return self.board[4][6]
        elif self.board[3][0] == self.board[2][0] == self.board[1][0] == self.board[0][0] != 0:
            return self.board[3][0]
        elif self.board[3][1] == self.board[2][1] == self.board[1][1] == self.board[0][1] != 0:
            return self.board[3][1]
        elif self.board[3][2] == self.board[2][2] == self.board[1][2] == self.board[0][2] != 0:
            return self.board[3][2]
        elif self.board[3][3] == self.board[2][3] == self.board[1][3] == self.board[0][3] != 0:
            return self.board[3][3]
        elif self.board[3][4] == self.board[2][4] == self.board[1][4] == self.board[0][4] != 0:
            return self.board[3][4]
        elif self.board[3][5] == self.board[2][5] == self.board[1][5] == self.board[0][5] != 0:
            return self.board[3][5]
        elif self.board[3][6] == self.board[2][6] == self.board[1][6] == self.board[0][6] != 0:
            return self.board[3][6]
        elif self.board[5][0] == self.board[4][1] == self.board[3][2] == self.board[2][3] != 0:
            return self.board[5][0]
        elif self.board[5][1] == self.board[4][2] == self.board[3][3] == self.board[2][4] != 0:
            return self.board[5][1]
        elif self.board[5][2] == self.board[4][3] == self.board[3][4] == self.board[2][5] != 0:
            return self.board[5][2]
        elif self.board[5][3] == self.board[4][4] == self.board[3][5] == self.board[2][6] != 0:
            return self.board[5][3]
        elif self.board[4][0] == self.board[3][1] == self.board[2][2] == self.board[1][3] != 0:
            return self.board[4][0]
        elif self.board[4][1] == self.board[3][2] == self.board[2][3] == self.board[1][4] != 0:
            return self.board[4][1]
        elif self.board[4][2] == self.board[3][3] == self.board[2][4] == self.board[1][5] != 0:
            return self.board[4][2]
        elif self.board[4][3] == self.board[3][4] == self.board[2][5] == self.board[1][6] != 0:
            return self.board[4][3]
        elif self.board[3][0] == self.board[2][1] == self.board[1][2] == self.board[0][3] != 0:
            return self.board[3][0]
        elif self.board[3][1] == self.board[2][2] == self.board[1][3] == self.board[0][4] != 0:
            return self.board[3][1]
        elif self.board[3][2] == self.board[2][3] == self.board[1][4] == self.board[0][5] != 0:
            return self.board[3][2]
        elif self.board[3][3] == self.board[2][4] == self.board[1][5] == self.board[0][6] != 0:
            return self.board[3][3]
        elif self.board[5][3] == self.board[4][2] == self.board[3][1] == self.board[2][0] != 0:
            return self.board[5][3]
        elif self.board[5][4] == self.board[4][3] == self.board[3][2] == self.board[2][1] != 0:
            return self.board[5][4]
        elif self.board[5][5] == self.board[4][4] == self.board[3][3] == self.board[2][2] != 0:
            return self.board[5][5]
        elif self.board[5][6] == self.board[4][5] == self.board[3][4] == self.board[2][3] != 0:
            return self.board[5][6]
        elif self.board[4][3] == self.board[3][2] == self.board[2][1] == self.board[1][0] != 0:
            return self.board[4][3]
        elif self.board[4][4] == self.board[3][3] == self.board[2][2] == self.board[1][1] != 0:
            return self.board[4][4]
        elif self.board[4][5] == self.board[3][4] == self.board[2][3] == self.board[1][2] != 0:
            return self.board[4][5]
        elif self.board[4][6] == self.board[3][5] == self.board[2][4] == self.board[1][3] != 0:
            return self.board[4][6]
        elif self.board[3][3] == self.board[2][2] == self.board[1][1] == self.board[0][0] != 0:
            return self.board[3][3]
        elif self.board[3][4] == self.board[2][3] == self.board[1][2] == self.board[0][1] != 0:
            return self.board[3][4]
        elif self.board[3][5] == self.board[2][4] == self.board[1][3] == self.board[0][2] != 0:
            return self.board[3][5]
        elif self.board[3][6] == self.board[2][5] == self.board[1][4] == self.board[0][3] != 0:
            return self.board[3][6]
        elif 0 not in self.board:
            return 0
        else:
            return None


class Stratego(Game):
    def __init__(self, pieces):
        super(Stratego, self).__init__(10, 10, 2)
        self.name = 'Stratego'
        self.version = pieces
        if self.version == 40:
            self.pieces = {
                88: 6,
                10: 1,
                9: 1,
                8: 2,
                7: 3,
                6: 4,
                5: 4,
                4: 4,
                3: 5,
                2: 8,
                1: 1,
                99: 1
                }

        if self.version == 20:
            self.pieces = {
                88: 4,
                10: 1,
                9: 1,
                8: 1,
                7: 1,
                6: 1,
                5: 1,
                4: 1,
                3: 3,
                2: 4,
                1: 1,
                99: 1
                }

        self.player1 = []
        self.player2 = []

        for key in self.pieces:
            for i in range(self.pieces[key]):
                self.player1.append([key, [-1, -1]])
                self.player2.append([key, [-1, -1]])

        self.board[4][2] = -1
        self.board[4][3] = -2
        self.board[5][2] = -1
        self.board[5][3] = -2
        self.board[4][6] = -1
        self.board[4][7] = -2
        self.board[5][6] = -1
        self.board[5][7] = -2

    def resetBoard(self):
        for i in range(10):
            for j in range(10):
                self.board[i][j] = 0

        if self.version == 40:
            self.pieces = {
                88: 6,
                10: 1,
                9: 1,
                8: 2,
                7: 3,
                6: 4,
                5: 4,
                4: 4,
                3: 5,
                2: 8,
                1: 1,
                99: 1
                }

        if self.version == 20:
            self.pieces = {
                88: 4,
                10: 1,
                9: 1,
                8: 1,
                7: 1,
                6: 1,
                5: 1,
                4: 1,
                3: 3,
                2: 4,
                1: 1,
                99: 1
                }

        self.player1 = []
        self.player2 = []

        for key in self.pieces:
            for i in range(self.pieces[key]):
                self.player1.append([key, [-1, -1]])
                self.player2.append([key, [-1, -1]])

        self.board[4][2] = -1
        self.board[4][3] = -2
        self.board[5][2] = -1
        self.board[5][3] = -2
        self.board[4][6] = -1
        self.board[4][7] = -2
        self.board[5][6] = -1
        self.board[5][7] = -2

    def getName(self):
        return self.name

    def __repr__(self):

        for i in self.player1:
            if i[1] == [-1, -1]:
                pass
            else:
                self.board[i[1][0]][i[1][1]] = i[0]

        for i in self.player2:
            if i[1] == [-1, -1]:
                pass
            else:
                self.board[i[1][0]][i[1][1]] = i[0]

        print_string = ''
        for i in range(self.getRow()):
            for j in range(self.getCol()):
                if self.board[i][j] == 99:
                    if [99, [i, j]] in self.player1:
                        print_string = print_string + '|{}{:^4}{}|'.format(fg(1), 'F', attr(0))
                    elif [99, [i, j]] in self.player2:
                        print_string = print_string + '|{}{:^4}{}|'.format(fg(4), 'F', attr(0))
                elif self.board[i][j] == 88:
                    if [88, [i, j]] in self.player1:
                        print_string = print_string + '|{}{:^4}{}|'.format(fg(1), 'B', attr(0))
                    elif [88, [i, j]] in self.player2:
                        print_string = print_string + '|{}{:^4}{}|'.format(fg(4), 'B', attr(0))
                elif self.board[i][j] == 1:
                    if [1, [i, j]] in self.player1:
                        print_string = print_string + '|{}{:^4}{}|'.format(fg(1), 'S', attr(0))
                    elif [1, [i, j]] in self.player2:
                        print_string = print_string + '|{}{:^4}{}|'.format(fg(4), 'S', attr(0))
                    else:
                        print_string = print_string + '|{:^4}|'.format('10')
                elif self.board[i][j] == -1:
                    print_string = print_string + '|{:^5}'.format('XXXXX')
                elif self.board[i][j] == -2:
                    print_string = print_string + '{:^5}|'.format('XXXXX')
                elif self.board[i][j] == 0:
                    print_string = print_string + '|{:^4}|'.format(' ')
                else:
                    if [self.board[i][j], [i, j]] in self.player1:
                        print_string = print_string + '|{}{:^4}{}|'.format(fg(1), int(self.board[i][j]), attr(0))
                    elif [self.board[i][j], [i, j]] in self.player2:
                        print_string = print_string + '|{}{:^4}{}|'.format(fg(4), int(self.board[i][j]), attr(0))
                    else:
                        print_string = print_string + '|{:^4}|'.format(int(self.board[i][j]))
            print_string = print_string + '\n'

        return print_string

    def listMoves(self, row, col, player):

        for i in self.player1:
            if i[1] == [-1, -1]:
                pass
            else:
                self.board[i[1][0]][i[1][1]] = i[0]

        for i in self.player2:
            if i[1] == [-1, -1]:
                pass
            else:
                self.board[i[1][0]][i[1][1]] = i[0]

        moves = []
        piece = 0
        if player == 1:
            for i in self.player1:
                if [row, col] == i[1]:
                    piece = i[0]
            if piece == 88 or piece == 99:
                return moves
            for i in range(len(self.player1)):
                if [piece, [row, col]] == self.player1[i]:
                    if piece == 2:
                        for j in range(row - 1, -1, -1):
                            if self.board[j][col] == 0:
                                moves.append([j, col])
                            elif self.board[j][col] > 0:
                                moves.append([j, col])
                                break
                            else:
                                break
                        for j in range(row + 1, 10):
                            if self.board[j][col] == 0:
                                moves.append([j, col])
                            elif self.board[j][col] > 0:
                                moves.append([j, col])
                                break
                            else:
                                break
                        for j in range(col - 1, -1, -1):
                            if self.board[row][j] == 0:
                                moves.append([row, j])
                            elif self.board[row][j] > 0:
                                moves.append([row, j])
                                break
                            else:
                                break
                        for j in range(col + 1, 10):
                            if self.board[row][j] == 0:
                                moves.append([row, j])
                            elif self.board[row][j] > 0:
                                moves.append([row, j])
                                break
                            else:
                                break
                    else:
                        if row == 0 and col == 0:
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])
                        elif row == 9 and col == 0:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])
                        elif row == 0 and col == 9:
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                        elif row == 9 and col == 9:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                        elif row == 0:
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])
                        elif row == 9:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])
                        elif col == 0:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])
                        elif col == 9:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                        else:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])
        else:
            for i in self.player2:
                if [row, col] == i[1]:
                    piece = i[0]
            if piece == 88 or piece == 99:
                return moves
            for j in range(len(self.player2)):
                if [piece, [row, col]] == self.player2[j]:
                    if piece == 2:
                        for i in range(row - 1, -1, -1):
                            if self.board[i][col] == 0:
                                moves.append([i, col])
                            elif self.board[i][col] > 0:
                                moves.append([i, col])
                                break
                            else:
                                break
                        for i in range(row + 1, 10):
                            if self.board[i][col] == 0:
                                moves.append([i, col])
                            elif self.board[i][col] > 0:
                                moves.append([i, col])
                                break
                            else:
                                break
                        for i in range(col - 1, -1, -1):
                            if self.board[row][i] == 0:
                                moves.append([row, i])
                            elif self.board[row][i] > 0:
                                moves.append([row, i])
                                break
                            else:
                                break
                        for i in range(col + 1, 10):
                            if self.board[row][i] == 0:
                                moves.append([row, i])
                            elif self.board[row][i] > 0:
                                moves.append([row, i])
                                break
                            else:
                                break
                    else:
                        if row == 0 and col == 0:
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])
                        elif row == 9 and col == 0:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])
                        elif row == 0 and col == 9:
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                        elif row == 9 and col == 9:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                        elif row == 0:
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])
                        elif row == 9:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])
                        elif col == 0:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])
                        elif col == 9:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                        else:
                            if self.board[row - 1][col] >= 0:
                                moves.append([row - 1, col])
                            if self.board[row + 1][col] >= 0:
                                moves.append([row + 1, col])
                            if self.board[row][col - 1] >= 0:
                                moves.append([row, col - 1])
                            if self.board[row][col + 1] >= 0:
                                moves.append([row, col + 1])

        toRemove = []
        for move in moves:
            if player == 1:
                for i in self.player1:
                    if move in i:
                        toRemove.append(move)
            else:
                for i in self.player2:
                    if move in i:
                        toRemove.append(move)

        for i in toRemove:
            moves.remove(i)

        return moves

    def listAll(self, player):
        moves = []
        if player == 1:
            for i in self.player1:
                possibleMoves = self.listMoves(i[1][0], i[1][1], player)
                for j in possibleMoves:
                    moves.append([i[1], j])
        else:
            for i in self.player2:
                possibleMoves = self.listMoves(i[1][0], i[1][1], player)
                for j in possibleMoves:
                    moves.append([i[1], j])
        return moves

    def makeMove(self, moveFrom, moveTo, player):
        moves = self.listMoves(moveFrom[0], moveFrom[1], player)

        if moveTo in moves:
            if self.board[moveTo[0]][moveTo[1]] == 0:
                if player == 1:
                    for i in self.player1:
                        if moveFrom in i:
                            i[1] = moveTo
                            self.board[moveFrom[0]][moveFrom[1]] = 0
                else:
                    for i in self.player2:
                        if moveFrom in i:
                            i[1] = moveTo
                            self.board[moveFrom[0]][moveFrom[1]] = 0
            else:
                if player == 1:
                    for i in self.player2:
                        if moveTo in i:
                            for j in self.player1:
                                if moveFrom in j:
                                    if j[0] == 1:
                                        if i[0] == 10 or i[0] == 99:
                                            j[1] = moveTo
                                            self.player2.remove(i)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0
                                        else:
                                            self.player1.remove(j)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0
                                    elif j[0] == 3:
                                        if i[0] == 88 or i[0] == 99:
                                            j[1] = moveTo
                                            self.player2.remove(i)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0
                                        else:
                                            self.player1.remove(j)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0
                                    else:
                                        if j[0] > i[0]:
                                            j[1] = moveTo
                                            self.player2.remove(i)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0
                                        else:
                                            self.player1.remove(j)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0
                else:
                    for i in self.player1:
                        if moveTo in i:
                            for j in self.player2:
                                if moveFrom in j:
                                    if j[0] == 1:
                                        if i[0] == 10 or i[0] == 99:
                                            j[1] = moveTo
                                            self.player1.remove(i)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0
                                        else:
                                            self.player2.remove(j)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0
                                    elif j[0] == 3:
                                        if i[0] == 88 or i[0] == 99:
                                            j[1] = moveTo
                                            self.player1.remove(i)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0
                                        else:
                                            self.player2.remove(j)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0
                                    else:
                                        if j[0] > i[0] or i[0] == 99:
                                            j[1] = moveTo
                                            self.player1.remove(i)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0
                                        else:
                                            self.player2.remove(j)
                                            self.board[moveFrom[0]][moveFrom[1]] = 0

    def checkWin(self):
        flag = False
        for i in self.player1:
            if 99 in i:
                flag = True
        if not flag:
            return -1
        flag = False
        for i in self.player2:
            if 99 in i:
                flag = True
        if not flag:
            return 1

        if not self.listAll(1):
            return -1

        if not self.listAll(2):
            return 1

        return None


class Checkers(Game):
    def __init__(self):
        super(Checkers, self).__init__(8, 8, 2)
        self.name = "Checkers"
        self.player1 = []
        self.player2 = []

        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 1:
                        if i < 3:
                            self.player2.append([[i, j], 1])
                            self.board[i][j] = -1
                        if i > 4:
                            self.player1.append([[i, j], 1])
                            self.board[i][j] = 1
                    else:
                        self.board[i][j] = -3
                else:
                    if j % 2 == 0:
                        if i < 3:
                            self.player2.append([[i, j], 1])
                            self.board[i][j] = -1
                        if i >= 5:
                            self.player1.append([[i, j], 1])
                            self.board[i][j] = 1
                    else:
                        self.board[i][j] = -3

    def __repr__(self):
        print_str = ""

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 1:
                    print_str = print_str + '|{}{:^3}{}|'.format(bg(1), 'O', attr(0))
                elif self.board[i][j] == -1:
                    print_str = print_str + '|{}{:^3}{}|'.format(bg(4), 'O', attr(0))
                elif self.board[i][j] == 2:
                    print_str = print_str + '|{}{:^3}{}|'.format(bg(1), 'K', attr(0))
                elif self.board[i][j] == -2:
                    print_str = print_str + '|{}{:^3}{}|'.format(bg(4), 'K', attr(0))
                elif self.board[i][j] == -3:
                    print_str = print_str + '|{}{:^3}{}|'.format(bg(0), '-', attr(0))
                else:
                    print_str = print_str + '|{}{:^3}{}|'.format(bg(7), ' ', attr(0))
            print_str = print_str + '\n'

        return print_str

    def checkWin(self):
        if len(self.player2) == 0:
            return 1
        elif len(self.player1) == 0:
            return -1
        elif len(self.getMoves(1)) == 0:
            return -1
        elif len(self.getMoves(-1)) == 0:
            return 1
        else:
            return None

    def getMoves(self, player):  # For every piece, if can take, add moves then return, else add open spots
        moves = []
        if player == 1:
            for piece in self.player1:
                if piece[1] == 1:
                    location = piece[0]
                    if location[0] > 1:
                        if location[1] == 0 or location[1] == 1:  # Start checking for taking pieces
                            if self.board[location[0] - 1][location[1] + 1] < 0:
                                if self.board[location[0] - 2][location[1] + 2] == 0:
                                    moves.append([location,[location[0] - 2, location[1] + 2]])
                        elif location[1] == 6 or location[1] == 7:
                            if self.board[location[0] - 1][location[1] - 1] < 0:
                                if self.board[location[0] - 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] - 2]])
                        else:
                            if self.board[location[0] - 1][location[1] - 1] < 0:
                                if self.board[location[0] - 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] - 2]])
                            if self.board[location[0] - 1][location[1] + 1] < 0:
                                if self.board[location[0] - 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] + 2]])
                elif piece[1] == 2:
                    location = piece[0]
                    if 1 < location[0] < 6:
                        if location[1] == 0 or location[1] == 1:  # Start checking for taking pieces
                            if self.board[location[0] - 1][location[1] + 1] < 0:
                                if self.board[location[0] - 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] + 2]])
                            if self.board[location[0] + 1][location[1] + 1] < 0:
                                if self.board[location[0] + 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] + 2]])
                        elif location[1] == 6 or location[1] == 7:
                            if self.board[location[0] - 1][location[1] - 1] < 0:
                                if self.board[location[0] - 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] - 2]])
                            if self.board[location[0] + 1][location[1] - 1] < 0:
                                if self.board[location[0] + 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] - 2]])
                        else:
                            if self.board[location[0] - 1][location[1] - 1] < 0:
                                if self.board[location[0] - 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] - 2]])
                            if self.board[location[0] + 1][location[1] - 1] < 0:
                                if self.board[location[0] + 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] - 2]])
                            if self.board[location[0] - 1][location[1] + 1] < 0:
                                if self.board[location[0] - 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] + 2]])
                            if self.board[location[0] + 1][location[1] + 1] < 0:
                                if self.board[location[0] + 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] + 2]])
                    elif location[0] == 0:
                        if location[1] == 0 or location[1] == 1:  # Start checking for taking pieces
                            if self.board[location[0] + 1][location[1] + 1] < 0:
                                if self.board[location[0] + 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] + 2]])
                        elif location[1] == 6 or location[1] == 7:
                            if self.board[location[0] + 1][location[1] - 1] < 0:
                                if self.board[location[0] + 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] - 2]])
                        else:
                            if self.board[location[0] + 1][location[1] - 1] < 0:
                                if self.board[location[0] + 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] - 2]])
                            if self.board[location[0] + 1][location[1] + 1] < 0:
                                if self.board[location[0] + 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] + 2]])
                    elif location[0] == 7:
                        if location[1] == 0 or location[1] == 1:  # Start checking for taking pieces
                            if self.board[location[0] - 1][location[1] + 1] < 0:
                                if self.board[location[0] - 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] + 2]])
                        elif location[1] == 6 or location[1] == 7:
                            if self.board[location[0] - 1][location[1] - 1] < 0:
                                if self.board[location[0] - 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] - 2]])
                        else:
                            if self.board[location[0] - 1][location[1] - 1] < 0:
                                if self.board[location[0] - 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] - 2]])
                            if self.board[location[0] - 1][location[1] + 1] < 0:
                                if self.board[location[0] - 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] + 2]])
        else:
            for piece in self.player2:
                if piece[1] == 1:
                    location = piece[0]
                    if location[0] < 6:
                        if location[1] == 0 or location[1] == 1:  # Start checking for taking pieces
                            if self.board[location[0] + 1][location[1] + 1] > 0:
                                if self.board[location[0] + 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] + 2]])
                        elif location[1] == 6 or location[1] == 7:
                            if self.board[location[0] + 1][location[1] - 1] > 0:
                                if self.board[location[0] + 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] - 2]])
                        else:
                            if self.board[location[0] + 1][location[1] - 1] > 0:
                                if self.board[location[0] + 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] - 2]])
                            if self.board[location[0] + 1][location[1] + 1] > 0:
                                if self.board[location[0] + 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] + 2]])
                elif piece[1] == 2:
                    location = piece[0]
                    if 1 < location[0] < 6:
                        if location[1] == 0 or location[1] == 1:  # Start checking for taking pieces
                            if self.board[location[0] - 1][location[1] + 1] > 0:
                                if self.board[location[0] - 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] + 2]])
                            if self.board[location[0] + 1][location[1] + 1] > 0:
                                if self.board[location[0] + 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] + 2]])
                        elif location[1] == 6 or location[1] == 7:
                            if self.board[location[0] - 1][location[1] - 1] > 0:
                                if self.board[location[0] - 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] - 2]])
                            if self.board[location[0] + 1][location[1] - 1] > 0:
                                if self.board[location[0] + 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] - 2]])
                        else:
                            if self.board[location[0] - 1][location[1] - 1] > 0:
                                if self.board[location[0] - 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] - 2]])
                            if self.board[location[0] + 1][location[1] - 1] > 0:
                                if self.board[location[0] + 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] - 2]])
                            if self.board[location[0] - 1][location[1] + 1] > 0:
                                if self.board[location[0] - 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] + 2]])
                            if self.board[location[0] + 1][location[1] + 1] > 0:
                                if self.board[location[0] + 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] + 2]])
                    elif location[0] == 0:
                        if location[1] == 0 or location[1] == 1:  # Start checking for taking pieces
                            if self.board[location[0] + 1][location[1] + 1] > 0:
                                if self.board[location[0] + 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] + 2]])
                        elif location[1] == 6 or location[1] == 7:
                            if self.board[location[0] + 1][location[1] - 1] > 0:
                                if self.board[location[0] + 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] - 2]])
                        else:
                            if self.board[location[0] + 1][location[1] - 1] > 0:
                                if self.board[location[0] + 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] - 2]])
                            if self.board[location[0] + 1][location[1] + 1] > 0:
                                if self.board[location[0] + 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] + 2, location[1] + 2]])
                    elif location[0] == 7:
                        if location[1] == 0 or location[1] == 1:  # Start checking for taking pieces
                            if self.board[location[0] - 1][location[1] + 1] > 0:
                                if self.board[location[0] - 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] + 2]])
                        elif location[1] == 6 or location[1] == 7:
                            if self.board[location[0] - 1][location[1] - 1] > 0:
                                if self.board[location[0] - 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] - 2]])
                        else:
                            if self.board[location[0] - 1][location[1] - 1] > 0:
                                if self.board[location[0] - 2][location[1] - 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] - 2]])
                            if self.board[location[0] - 1][location[1] + 1] > 0:
                                if self.board[location[0] - 2][location[1] + 2] == 0:
                                    moves.append([location, [location[0] - 2, location[1] + 2]])
        if len(moves) != 0:
            return moves

        if player == 1:
            for piece in self.player1:
                if piece[1] == 1:
                    location = piece[0]
                    if location[0] != 0:
                        if location[1] == 0:
                            if self.board[location[0] - 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] + 1]])
                        elif location[1] == 7:
                            if self.board[location[0] - 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] - 1]])
                        else:
                            if self.board[location[0] - 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] - 1]])
                            if self.board[location[0] - 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] + 1]])
                elif piece[1] == 2:
                    location = piece[0]
                    if 0 < location[0] < 7:
                        if location[1] == 0:
                            if self.board[location[0] - 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] + 1]])
                            if self.board[location[0] + 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] + 1]])
                        elif location[1] == 7:
                            if self.board[location[0] - 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] - 1]])
                            if self.board[location[0] + 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] - 1]])
                        else:
                            if self.board[location[0] - 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] - 1]])
                            if self.board[location[0] - 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] + 1]])
                            if self.board[location[0] + 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] - 1]])
                            if self.board[location[0] + 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] + 1]])
                    elif location[0] == 0:
                        if location[1] == 0:
                            if self.board[location[0] + 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] + 1]])
                        elif location[1] == 7:
                            if self.board[location[0] + 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] - 1]])
                        else:
                            if self.board[location[0] + 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] - 1]])
                            if self.board[location[0] + 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] + 1]])
                    elif location[0] == 7:
                        if location[1] == 0:
                            if self.board[location[0] - 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] + 1]])
                        elif location[1] == 7:
                            if self.board[location[0] - 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] - 1]])
                        else:
                            if self.board[location[0] - 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] - 1]])
                            if self.board[location[0] - 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] + 1]])
        else:
            for piece in self.player2:
                if piece[1] == 1:
                    location = piece[0]
                    if location[0] != 7:
                        if location[1] == 0:
                            if self.board[location[0] + 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] + 1]])
                        elif location[1] == 7:
                            if self.board[location[0] + 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] - 1]])
                        else:
                            if self.board[location[0] + 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] - 1]])
                            if self.board[location[0] + 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] + 1]])
                elif piece[1] == 2:
                    location = piece[0]
                    if 0 < location[0] < 7:
                        if location[1] == 0:
                            if self.board[location[0] - 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] + 1]])
                            if self.board[location[0] + 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] + 1]])
                        elif location[1] == 7:
                            if self.board[location[0] - 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] - 1]])
                            if self.board[location[0] + 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] - 1]])
                        else:
                            if self.board[location[0] - 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] - 1]])
                            if self.board[location[0] - 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] + 1]])
                            if self.board[location[0] + 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] - 1]])
                            if self.board[location[0] + 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] + 1]])
                    elif location[0] == 0:
                        if location[1] == 0:
                            if self.board[location[0] + 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] + 1]])
                        elif location[1] == 7:
                            if self.board[location[0] + 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] - 1]])
                        else:
                            if self.board[location[0] + 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] - 1]])
                            if self.board[location[0] + 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] + 1, location[1] + 1]])
                    elif location[0] == 7:
                        if location[1] == 0:
                            if self.board[location[0] - 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] + 1]])
                        elif location[1] == 7:
                            if self.board[location[0] - 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] - 1]])
                        else:
                            if self.board[location[0] - 1][location[1] - 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] - 1]])
                            if self.board[location[0] - 1][location[1] + 1] == 0:
                                moves.append([location, [location[0] - 1, location[1] + 1]])
        return moves

    def makeMove(self, moveFrom, moveTo, player):
        if player == 1:
            for piece in self.player1:
                if piece[0] == moveFrom:
                    if moveTo[0] == 0:
                        piece[1] = 2
        else:
            for piece in self.player2:
                if piece[0] == moveFrom:
                    if moveTo[0] == 7:
                        piece[1] = 2
        if player == 1:
            for piece in self.player1:
                if piece[0] == moveFrom:
                    break
        else:
            for piece in self.player2:
                if piece[0] == moveFrom:
                    break
        if abs(moveTo[1] - moveFrom[1]) == 2:
            self.board[moveTo[0]][moveTo[1]] = piece[1] * player
            self.board[moveFrom[0]][moveFrom[1]] = 0
            self.board[moveFrom[0] + (moveTo[0] - moveFrom[0])//2][moveFrom[1] + (moveTo[1] - moveFrom[1])//2] = 0
            if player == 1:
                for piece in self.player2:
                    if piece[0] == [moveFrom[0] + (moveTo[0] - moveFrom[0])//2, moveFrom[1] + (moveTo[1] - moveFrom[1])//2]:
                        self.player2.remove(piece)
            else:
                for piece in self.player1:
                    if piece[0] == [moveFrom[0] + (moveTo[0] - moveFrom[0])//2, moveFrom[1] + (moveTo[1] - moveFrom[1])//2]:
                        self.player1.remove(piece)
        else:
            self.board[moveTo[0]][moveTo[1]] = piece[1] * player
            self.board[moveFrom[0]][moveFrom[1]] = 0

        if player == 1:
            for piece in self.player1:
                if piece[0] == moveFrom:
                    piece[0] = moveTo
        else:
            for piece in self.player2:
                if piece[0] == moveFrom:
                    piece[0] = moveTo

    def resetBoard(self):
        self.__init__()


if __name__ == "__main__":
    tic = TicTacToe()
    con = ConnectFour()
    strat = Stratego(40)
    check = Checkers()
    print(check.board)
    print(check)
    opp1 = AI(check, 1)
    opp2 = AI(check, 2)
    turn = 0
    try:
        while check.checkWin() is None:
            if turn % 2 == 0:
                move = opp1.chooseMove()
                check.makeMove(move[0], move[1], 1)
                print(check)
                turn += 1
            else:
                move = opp2.chooseMove()
                check.makeMove(move[0], move[1], -1)
                print(check)
                turn += 1
        print(check.checkWin())
    except KeyboardInterrupt:
        pass