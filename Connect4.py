class Game():
    columumn_counts = 7
    row_counts = 6

    def __init__(self):
        self.gameboard = [[' ' for i in range(Game.columumn_counts)] for j in range(
            Game.row_counts)]

    def print_gameboard(self):
        # constructing gameboard
        gameboard = ''
        for i in self.gameboard:
            gameboard += '$' * 15 + '\n'
            for j in i:
                gameboard += f'|{j}'
            gameboard += '|\n'
        gameboard += '$' * 15
        print(gameboard)

    def add_statement(self, colum, team):

        if colum:
            if colum.isdigit():
                colum = int(colum)
                if colum < 7 and colum > -1 or colum == None:
                    colum -= 1
                    if self.gameboard[0][colum] == ' ':
                        for i in range(5, -1, -1):
                            if self.gameboard[i][colum] == ' ':
                                self.gameboard[i][colum] = team
                                break
                    else:
                        print(
                            'ERROR')
                else:
                    print('You must enter from 1-7 , Next player will continue')
            else:
                print('You must enter only numbers!!! , Next player will continue')
        else:
            print('Can not be empty! , Next player will continue')

    def check(self, team):

        # check for diag for right
        for c in range(Game.columumn_counts - 3):
            for d in range(Game.row_counts - 3):
                if self.gameboard[d][c] == team and self.gameboard[d + 1][c + 1] == team and self.gameboard[d + 2][
                    c + 2] == team and self.gameboard[d + 3][c + 3] == team:
                    return True

        # check for diag for left
        for c in range(Game.columumn_counts - 4, Game.columumn_counts):
            for d in range(Game.row_counts - 3):
                if self.gameboard[d][c] == team and self.gameboard[d + 1][c - 1] == team and self.gameboard[d + 2][
                    c - 2] == team and self.gameboard[d + 3][c - 3] == team:
                    return True
                # check horizontal
            for i in range(Game.columumn_counts - 3):
                for j in range(Game.row_counts):
                    if self.gameboard[j][i] == team and self.gameboard[j][i + 1] == team and self.gameboard[j][
                        i + 2] == team and \
                            self.gameboard[j][i + 3] == team:
                        return True

            # check for vertical
            for c in range(Game.columumn_counts):
                for d in range(Game.row_counts - 3):
                    if self.gameboard[d][c] == team and self.gameboard[d + 1][c] == team and self.gameboard[d + 2][
                        c] == team and \
                            self.gameboard[d + 3][c] == team:
                        return True

    def check_tie(self):

        for i in self.gameboard:
            for j in i:
                if j == ' ':
                    return False
        return True


def game_loop(game: Game):
    player1, player2 = 'X', 'O'

    while not game.check(player1) and not game.check(player2):
        colum = input('Player 1 (X) : choose colum (1-7): ')
        game.add_statement(colum, player1)
        game.print_gameboard()

        if game.check(player1):
            print('PLAYER 1  WINS!')
            quit()

        if game.check_tie():
            print('Tie!')
            quit()

        colum = input('Player 2 (O) : choose colum (1-7): ')
        game.add_statement(colum, player2)
        game.print_gameboard()

        if game.check(player2):
            print('PLAYER 2  WINS!')
            quit()

        if game.check_tie():
            print('Tie!')
            quit()


def main():
    game = Game()
    game.print_gameboard()
    game_loop(game)


if __name__ == '__main__':
    print("Game Started!")
    main()
