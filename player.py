class Player:
    def __init__(self, name = 'IA', symbol = 'x'):
        self.name = name
        self.symbol = symbol
        self.score = 0
    
    def win(self):
        self.score += 1

    def reset(self):
        self.score = 0
    
    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol
    
    def get_score(self):
        return self.score
