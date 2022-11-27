class Game():
    column_counts = 7
    row_counts = 6

    def __init__(self):
        self.gameboard = [[' ' for i in range(Game.column_counts)] for j in range(
            Game.row_counts)]

    def print_gameboard(self):
        # constructing gameboard
        gameboard = ''
        for i in self.gameboard:
            gameboard += '-' * 15 + '\n'
            for j in i:
                gameboard += f'|{j}'
            gameboard += '|\n'
        gameboard += '-' * 15
        print(gameboard)

    def add_block(self, col, team):

        if col:
            if col.isdigit():
                col = int(col)
                if col < 7 and col > -1 or col == None:
                    col -= 1
                    if self.gameboard[0][col] == ' ':
                        for i in range(5, -1, -1):
                            if self.gameboard[i][col] == ' ':
                                self.gameboard[i][col] = team
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
        for c in range(Game.column_counts - 3):
            for r in range(Game.row_counts - 3):
                if self.gameboard[r][c] == team and self.gameboard[r + 1][c + 1] == team and self.gameboard[r + 2][
                    c + 2] == team and self.gameboard[r + 3][c + 3] == team:
                    return True

        # check for diag for left
        for c in range(Game.column_counts - 4, Game.column_counts):
            for r in range(Game.row_counts - 3):
                if self.gameboard[r][c] == team and self.gameboard[r + 1][c - 1] == team and self.gameboard[r + 2][
                    c - 2] == team and self.gameboard[r + 3][c - 3] == team:
                    return True
                # check horizontal
            for i in range(Game.column_counts - 3):
                for j in range(Game.row_counts):
                    if self.gameboard[j][i] == team and self.gameboard[j][i + 1] == team and self.gameboard[j][
                        i + 2] == team and \
                            self.gameboard[j][i + 3] == team:
                        return True

            # check for vertical
            for c in range(Game.column_counts):
                for r in range(Game.row_counts - 3):
                    if self.gameboard[r][c] == team and self.gameboard[r + 1][c] == team and self.gameboard[r + 2][
                        c] == team and \
                            self.gameboard[r + 3][c] == team:
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
        col = input('Player 1 (X) choose col (1-7): ')
        game.add_block(col, player1)
        game.print_gameboard()

        if game.check(player1):
            print('PLAYER 1  WINS!')
            quit()

        if game.check_tie():
            print('Tie!')
            quit()

        col = input('Player 2 (O) choose col (1-7): ')
        game.add_block(col, player2)
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
