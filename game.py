from gameparts import Board
from inspect import getsource
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
   
    game = Board()
    game.display()

    current_player = 'X'

    running = True

    
    while running:
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError # ('Введено значение за границами игрового поля')
                col = int(input('Введите номер столбца: '))
                if col < 0 or col >= game.field_size:
                    raise FieldIndexError # ('дурак')
                if game.board[row][col] != (' '):
                    raise CellOccupiedError
            
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
            except CellOccupiedError as e:
                print(e)
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
            
                continue
            else:
                break
    
        game.make_move(row, col, current_player)
        print('Ход сделан!')
        print('Ходит другой игрок')
        game.display()
        if game.check_win(current_player) == True:
            winner = f'{current_player} is a winner!'
            game.save_result(winner) 
            print(f'{current_player} is a winner!')
            running = False
        elif game.is_board_full() == True:
            winner = f'it is a Draw'
            game.save_result(winner) 
            print('it is Draw')
            running = False
        
          
        current_player = 'O' if current_player == 'X' else 'X' 

       
           

    # print(isinstance(game,int))
    # print(game.__str__())
    # print(game.__class__.__dict__)
    # print(getsource(Board))
   


if __name__ == '__main__':
    main()

# print(Board.__doc__)