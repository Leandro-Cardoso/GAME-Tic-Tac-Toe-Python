from game import Game
from player import Player
from utils import clear

def new_game():
    clear()

    while True:
        print('\n 1 - Player1 vs IA\n 2 - Player1 vs Player2')
        
        option = input('\n Opcao: ')

        if option == '1' or option == '2':
            break
        else:
            print('\n Opcao invalida !!!')
            continue

    clear()
    
    while True:
        player1 = input('\n Nome do Player1: ')

        if player1 == '':
            print('\n O Player1 precisa de um nome !!!')
            continue
        else:
            player1 = Player(player1)
            break
    
    if option == '2':
        clear()

        while True:
            player2 = input('\n Nome do Player2: ')

            if player2 == '':
                print('\n O Player2 precisa de um nome !!!')
                continue
            else:
                player2 = Player(player2, 'o')
                break
    else:
        player2 = Player(symbol = 'o')
        
    return Game(player1, player2)

def main():
    game = new_game()

    while True:
        clear()

        game.print()

        option = int(input(' Opcao: '))

        if 0 < option < 10:
            played = game.play(option - 1)

            if game.is_winner():
                game.players[game.p].win()
                game.reset_field()
            
            if played:
                game.take_turn()
        else:
            break

    print()

main()
