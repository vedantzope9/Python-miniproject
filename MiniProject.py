import random
print("\n\t\t\t\t\t\t\t\t\t\tWhich game would you like to play??\n\n\t\t\t\t\t\t\t\t\t\t\t1-Rock,Paper,Scissors\n\t\t\t\t\t\t\t\t\t\t\t2-Guessing a number\n\t\t\t\t\t\t\t\t\t\t\t3- Tic-Tac-Toe\n\t\t\t\t\t\t\t\t\t\t\t4-Dice Roll Generator\n")
c=input("Enter your choice::")

if c=='1' :
        choices = ["Rock", "Paper", "Scissors"]
        computer = random.choice(choices)
        player = False
        cpu_score = 0
        player_score = 0
        print("\t\t\t Welcome to Rock,Paper,Scissor Game")
        print("Enter 'end' to STOP the game\n")
        while True:
            player = input("Rock, Paper or  Scissors?\n").capitalize()

            if player == computer:
                print("Tie!")
            elif player == "Rock":
                if computer == "Paper":
                    print("You lose!", computer, "covers", player)
                    cpu_score+=1
                else:
                    print("You win!", player, "smashes", computer)
                    player_score+=1
            elif player == "Paper":
                if computer == "Scissors":
                    print("You lose!", computer, "cut", player)
                    cpu_score+=1
                else:
                    print("You win!", player, "covers", computer)
                    player_score+=1
            elif player == "Scissors":
                if computer == "Rock":
                    print("You lose...", computer, "smashes", player)
                    cpu_score+=1
                else:
                    print("You win!", player, "cut", computer)
                    player_score+=1
            elif player=='End':
                print("Final Scores:")
                print(f"CPU:{cpu_score}")
                print(f"Player:{player_score}")
                break

elif c=='2':
    import random

    number = random.randint(1, 10)

    player_name = input("Hello, What's your name?")
    number_of_guesses = 0
    print('okay! ' + player_name + ' I am Guessing a number between 1 and 10:')

    while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            break
    if guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('You did not guess the number, The number was ' + str(number))

elif c=='3':
    import random
    class TicTacToe:

        def __init__(self):
            self.board = []

        def create_board(self):
            for i in range(3):
                row = []
                for j in range(3):
                    row.append('-')
                self.board.append(row)

        def get_random_first_player(self):
            return random.randint(0, 1)

        def fix_spot(self, row, col, player):
            self.board[row][col] = player

        def has_player_won(self, player):
            n = len(self.board)
            board_values = set()

            # check rows
            for i in range(n):
                for j in range(n):
                    board_values.add(self.board[i][j])

                if board_values == {player}:
                    return True
                else:
                    board_values.clear()

            # check cols
            for i in range(n):
                for j in range(n):
                    board_values.add(self.board[j][i])

                if board_values == {player}:
                    return True
                else:
                    board_values.clear()

            # check diagonals
            for i in range(n):
                board_values.add(self.board[i][i])
            if board_values == {player}:
                return True
            else:
                board_values.clear()

            board_values.add(self.board[0][2])
            board_values.add(self.board[1][1])
            board_values.add(self.board[2][0])
            if board_values == {player}:
                return True
            else:
                return False

        def is_board_filled(self):
            for row in self.board:
                for item in row:
                    if item == '-':
                        return False
            return True

        def swap_player_turn(self, player):
            return 'X' if player == 'O' else 'O'

        def show_board(self):
            for row in self.board:
                for item in row:
                    print(item, end=' ')
                print()

        def start(self):
            self.create_board()
            player = 'X' if self.get_random_first_player() == 1 else 'O'
            game_over = False

            while not game_over:
                try:
                    self.show_board()
                    print(f'\nPlayer {player} turn')

                    row, col = list(
                        map(int, input(
                            'Enter row & column numbers to fix spot: ').split()))
                    print()

                    if col is None:
                        raise ValueError(
                            'not enough values to unpack (expected 2, got 1)')

                    self.fix_spot(row - 1, col - 1, player)

                    game_over = self.has_player_won(player)
                    if game_over:
                        print(f'Player {player} wins the game!')
                        continue

                    game_over = self.is_board_filled()
                    if game_over:
                        print('Match Draw!')
                        continue

                    player = self.swap_player_turn(player)

                except ValueError as err:
                    print(err)

            print()
            self.show_board()


    if __name__ == '__main__':
        tic_tac_toe = TicTacToe()
        tic_tac_toe.start()

elif c=='4':
    import random
    import os


    def num_die():
        while True:
            try:
                num_dice = input('Number of dice: ')
                valid_responses = ['1', 'one', 'two', '2']
                if num_dice not in valid_responses:
                    raise ValueError('1 or 2 only')
                else:
                    return num_dice
            except ValueError as err:
                print(err)


    def roll_dice():
        min_val = 1
        max_val = 6
        roll_again = 'y'

        while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            amount = num_die()

            if amount == '2' or amount == 'two':
                print('Rolling the dice...')
                dice_1 = random.randint(min_val, max_val)
                dice_2 = random.randint(min_val, max_val)

                print('The values are:')
                print('Dice One: ', dice_1)
                print('Dice Two: ', dice_2)
                print('Total: ', dice_1 + dice_2)

                roll_again = input('Roll Again? ')
            else:
                print('Rolling the die...')
                dice_1 = random.randint(min_val, max_val)
                print(f'The value is: {dice_1}')

                roll_again = input('Roll Again? ')


    if __name__ == '__main__':
        roll_dice()

else:
    print("Invalid\nPlease Try again!!!")

