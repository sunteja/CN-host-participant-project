class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.p3Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None, None]
        self.wins = [0,0,0]
        self.ties = 0

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def buzzer(self,player):
        if player == 0:
            self.p2Went = True
            self.p3Went = True
        elif player == 1:
            self.p1Went = True
            self.p3Went = True
        elif player == 2:
            self.p1Went = True
            self.p2Went = True


    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        elif player == 1:
            self.p2Went = True
        else:
            self.p3Went = True

    def connected(self):
        return self.ready

    def allWent(self):
        return self.p1Went and self.p2Went and self.p3Went

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
        self.p3Went = False


'''
    def winner(self):

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]
        p3 = self.moves[2].upper()[0]

        winner = -1
        if p1 == self.ans:
            winner = 0
        if p2 == self.ans:
            winner = 1
        if p3 == self.ans:
            winner = 2
        
        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
        self.p3Went = False
'''        
