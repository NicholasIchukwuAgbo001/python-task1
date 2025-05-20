
from tic_tac_toe_game.current_state import CurrentState
from tic_tac_toe_game.tic_tac_toe import TicTacToe

game = TicTacToe()
current_player = CurrentState.X

print("\nWelcome to Tic-Tac-Toe Game!")

while True:
    print("====================")
    game.print_board()
    print("====================")

    while True:
        try:
            position = int(input(f"\nPlayer {current_player.name}, enter position (1-9): "))
            break
        except ValueError:
            print("Invalid input")

    try:
        game.make_move(current_player, position)
    except ValueError as e:
        print(e)
        continue

    winner = game.check_winner()
    if winner != CurrentState.EMPTY:
        game.print_board()
        print(f"\nPlayer {winner.name} wins!")
        break

    if game.is_tie():
        game.print_board()
        print("\nIt's a tie!")
        break

    current_player = CurrentState.O if current_player == CurrentState.X else CurrentState.X
