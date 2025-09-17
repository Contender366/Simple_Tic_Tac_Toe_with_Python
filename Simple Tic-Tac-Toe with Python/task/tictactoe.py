# Tic-Tac-Toe Game (Refactored to match input/output)

EMPTY_CELL = ' '
BOARD_SIZE = 3

# Initialize empty grid
grid = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
current_player = 'X'


def print_board():
    """Displays the current state of the game board."""
    print("---------")
    for row in grid:
        print(f"| {' '.join(row)} |")
    print("---------")


def get_flat_board():
    """Flattens the 2D grid into a 1D list."""
    return [cell for row in grid for cell in row]


def switch_player(player):
    """Switches the current player between X and O."""
    return 'O' if player == 'X' else 'X'


def is_valid_coordinates(row, col):
    """Checks if the row and column are within the board limits."""
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE


def is_cell_empty(row, col):
    """Checks if the selected cell is empty."""
    return grid[row][col] == EMPTY_CELL


def check_win(player):
    """Checks if the given player has a winning line."""
    win_lines = []

    for i in range(BOARD_SIZE):
        win_lines.append(grid[i])  # Rows
        win_lines.append([grid[j][i] for j in range(BOARD_SIZE)])  # Columns

    # Diagonals
    win_lines.append([grid[i][i] for i in range(BOARD_SIZE)])
    win_lines.append([grid[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)])

    return any(all(cell == player for cell in line) for line in win_lines)


def both_players_win():
    """Checks if both X and O win at the same time (invalid state)."""
    return check_win('X') and check_win('O')


def is_draw():
    """Checks if the board is full and no player has won."""
    return all(cell != EMPTY_CELL for cell in get_flat_board())


def play_game():
    """Main game loop for handling input, game state, and output."""
    global current_player

    print_board()

    while True:
        user_input = input().split()

        # Input validation
        if len(user_input) != 2 or not all(part.isdigit() for part in user_input):
            print("You should enter numbers!")
            continue

        row, col = map(int, user_input)
        row -= 1
        col -= 1

        if not is_valid_coordinates(row, col):
            print("Coordinates should be from 1 to 3!")
            continue

        if not is_cell_empty(row, col):
            print("This cell is occupied!")
            continue

        # Make move
        grid[row][col] = current_player
        print_board()

        # Check for game end conditions
        if both_players_win():
            print("Impossible")
            break
        elif check_win(current_player):
            print(f"{current_player} wins")
            break
        elif is_draw():
            print("Draw")
            break

        # Switch turn
        current_player = switch_player(current_player)


# Start the game
play_game()

