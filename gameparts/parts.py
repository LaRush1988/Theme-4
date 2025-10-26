class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    def check_win(self, player):
        for i in range(self.field_size):
            if (all([self.board[i][j] == player for j in range(self.field_size)]) or all([self.board[j][i] == player for j
            in range (self.field_size)])):
                return True
        if (
            all([self.board[i][i] == player for i in range (self.field_size)]) or 
            all([self.board[i][self.field_size-1-i] == player for i in range (self.field_size)])
            ):
            return True
        return False
    def save_result(self, winner):
            with open('results', 'a') as file:
                file.write (winner + '\n') 
    

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        ) 

print(Board.__doc__)