def check_win(self, player):
        for i in range(self.field_size):
            if (all([self.board[1][0] == player for j in range(self.field_size)]) or all([self.board[j][0] == player for j
            in range (self.field_size)])):
                return True
        if (all([self.board[i][i] == player for i in range (self.field_size)]) or all([self.board[i][2-i] == player 
            for i in range (self.field_size)])):
                return True
        return False