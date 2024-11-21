class Game:
    def __init__(self, player1, player2):
        self.field = None
        self.players = [player1, player2]
        self.p = 0

        self.reset_field()

    def reset_field(self):
        self.field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def take_turn(self):
        if self.players[self.p] == self.players[0]:
            self.p = 1
        else:
            self.p = 0

    def play(self, i):
        if self.field[i] != self.players[0].symbol and self.field[i] != self.players[1].symbol:
            self.field[i] = self.players[self.p].symbol

            return True

        return False
    
    def is_winner(self):
        victories = [
            [0, 1, 2], 
            [3, 4, 5], 
            [6, 7, 8], 
            [0, 3, 6], 
            [1, 4, 7], 
            [2, 5, 8], 
            [0, 4, 8], 
            [2, 4, 6]
            ]

        for victory in victories:
            for i in victory:
                if self.field[i] != self.players[self.p].symbol:
                    break
                if i == victory[-1]:
                    return True
        
        return False

    def print(self):
        print(f'\n{self}\n')

    def __str__(self):
        END = '\033[m'
        COLOR = '\033[33m'

        if self.p == 0:
            string = f' {COLOR}{self.players[0].name} - {self.players[0].score}{END}\n {self.players[1].name} - {self.players[1].score}\n'
        else:
            string = f' {self.players[0].name} - {self.players[0].score}\n {COLOR}{self.players[1].name} - {self.players[1].score}{END}\n'

        for i in range(9):
            if i % 3 == 0 and i != 9:
                string += '\n'

            if self.field[i] == self.players[0].symbol or self.field[i] == self.players[1].symbol:
                string += f' {COLOR}{self.field[i]}{END}'
            else:
                string += f' {self.field[i]}'

        return string
