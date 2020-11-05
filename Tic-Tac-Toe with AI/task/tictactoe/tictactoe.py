import random


class Field:
    def __init__(self):
        self.field = []
        self.reset()

    @staticmethod
    def _column_index(move):
        return move[0] - 4

    @staticmethod
    def _row_index(move):
        return -move[1]

    def reset(self):
        self.field = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]

    def set_field(self, field):
        self.field = field

    def print_field(self):
        print("---------")
        print("| {0} {1} {2} |".format(self.field[-3][-3], self.field[-3][-2], self.field[-3][-1]))
        print("| {0} {1} {2} |".format(self.field[-2][-3], self.field[-2][-2], self.field[-2][-1]))
        print("| {0} {1} {2} |".format(self.field[-1][-3], self.field[-1][-2], self.field[-1][-1]))
        print("---------")

    def initialize(self, start_values):
        _row = -3
        _column = -3
        for cell in start_values:
            set_value = " " if cell == "_" else cell
            self.write([_column, _row], set_value)
            _column += 1
            if _column >= 0:
                _column = -3
                _row += 1
        self.print_field()

    def make_move(self, player, move):
        self.write(player, move)
        self.print_field()

    def count(self, player):
        _quantity = 0
        for row in self.field:
            for item in row:
                if item == player:
                    _quantity += 1
        return _quantity

    def check_sequences(self, player):
        # Checking if there are any sequences in rows
        for row in self.field:
            if all(item == player for item in row):
                return True
        # Checking if there are any sequences in columns
        for column_index in range(-3, 0):
            if all(self.field[row_index][column_index] == player
                   for row_index in range(-3, 0)):
                return True
        # Checking if there are any sequences in diagonals
        if all(self.field[index][index] == player
               for index in range(-3, 0)):
            return True

        transposed = [[-1, -3], [-2, -2], [-3, -1]]
        if all(self.field[row][column] == player for
               (row, column) in transposed):
            return True

        return False

    def is_occupied(self, move):
        _column = self._column_index(move)
        _row = self._row_index(move)
        return self.field[_row][_column] != " "

    def has_empty_space(self):
        return any(True for row in self.field
                   for item in row
                   if item == " ")

    def copy_field(self):
        return [row.copy() for row in self.field.copy()]

    def write(self, player, move):
        _column = self._column_index(move)
        _row = self._row_index(move)
        self.field[_row][_column] = player

    def available_moves(self):
        moves = []
        for column in range(1, 4):
            for row in range(1, 4):
                if not self.is_occupied([column, row]):
                    moves.append((column, row))

        return moves


class Player:
    player_sign = "X"
    next_move = (0, 0)

    def __init__(self, player):
        self.player_sign = player

    def get_move(self, field: Field):
        return self.next_move

    def play(self, field: Field):
        move = self.get_move(field)
        if move:
            field.make_move(self.player_sign, move)


class UserPlayer(Player):
    def __str__(self):
        return "user"

    @staticmethod
    def validate_coordinates(coordinates, field: Field):
        if len(coordinates) != 2:
            print("You should enter numbers!")
            return False
        elif any(n for n in coordinates if n < 1 or n > 3):
            print("Coordinates should be from 1 to 3!")
            return False
        elif field.is_occupied(coordinates):
            print("This cell is occupied! Choose another one!")
            return False
        else:
            return True

    @staticmethod
    def get_coordinates(field: Field):
        raw_coordinates = [n for n in input("Enter the coordinates:")
                           if n != " "]
        coordinates = []
        for item in raw_coordinates:
            try:
                n = int(item)
                coordinates.append(n)
            except ValueError:
                print("You should enter numbers!")
                return None

        if not UserPlayer.validate_coordinates(coordinates, field):
            return None
        else:
            return coordinates

    def get_move(self, field: Field):
        return self.get_coordinates(field)


class ComputerPlayer(Player):
    def play(self, field: Field):
        print(f'Making move level "{self}"')
        super().play(field)


class EasyPlayer(ComputerPlayer):
    def __str__(self):
        return "easy"

    @staticmethod
    def random_move(field: Field):
        _column = random.randint(1, 3)
        _row = random.randint(1, 3)
        _change_column = True
        while field.is_occupied([_column, _row]):
            if _change_column:
                _column = random.randint(1, 3)
                _change_column = False
            else:
                _row = random.randint(1, 3)
                _change_column = True
        return _column, _row

    def get_move(self, field: Field):
        return self.random_move(field)


class MediumPlayer(EasyPlayer):
    def __str__(self):
        return "medium"

    @staticmethod
    def next_move_wins(player, move, field: Field):
        _fake_field = Field()
        _fake_field.set_field(field.copy_field())
        _fake_field.write(player, move)
        return _fake_field.check_sequences(player)

    def sharp_eyed_move(self, field: Field):
        _other_player = "O" if self.player_sign == "X" else "X"
        _win_move = []
        _block_move = []
        _next_move_wins = False
        _must_block = False

        for move in field.available_moves():
            if self.next_move_wins(self.player_sign, move, field):
                _next_move_wins = True
                _win_move = move
            elif self.next_move_wins(_other_player, move, field):
                _must_block = True
                _block_move = move

        if _next_move_wins:
            return _win_move
        elif _must_block:
            return _block_move
        else:
            return super().get_move(field)

    def get_move(self, field: Field):
        return self.sharp_eyed_move(field)


class HardPlayer(MediumPlayer):
    def __str__(self):
        return "hard"

    # The end_score, min and max functions were adapted from the following link
    # https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
    # This was the best reference I found on minimax algorithm
    # The reference from JetBrains Academy was not very helpful
    def end_score(self, field: Field):
        # define terminal states
        _other_player = "O" if self.player_sign == "X" else "X"
        if field.check_sequences(_other_player):
            return -10, 0, 0
        elif field.check_sequences(self.player_sign):
            return 10, 0, 0
        elif not field.has_empty_space():
            return 0, 0, 0

    # Maximize victory during HardPlayer turn
    # Possible values: (-10 - loss) (0  - a tie) (10  - win)
    def max(self, moves: list, fake_field: Field):
        # Evaluate and return if the game has ended
        score = self.end_score(fake_field)
        if score:
            return score

        maximum = -20
        max_column = None
        max_row = None
        for column, row in moves:
            # Write AI player sign to start evaluating possible moves
            fake_field.write(self.player_sign, (column, row))
            remaining_moves = moves[::]
            remaining_moves.remove((column, row))
            (m, min_c, min_r) = self.min(remaining_moves, fake_field)
            # Evaluate maximum value
            if m > maximum:
                maximum = m
                max_row = row
                max_column = column
            # Reset position to empty
            fake_field.write(" ", (column, row))

        return maximum, max_column, max_row

    # Minimize victory during adversary turn
    # Possible values: (-10 - win) (0  - a tie) (10  - loss)
    def min(self, moves: list, fake_field: Field):
        # Evaluate and return if the game has ended
        score = self.end_score(fake_field)
        if score:
            return score

        minimum = 20
        min_column = None
        min_row = None
        other_player = "O" if self.player_sign == "X" else "X"
        for column, row in moves:
            # Write adversary move to evaluate possible moves
            fake_field.write(other_player, (column, row))
            remaining_moves = moves[::]
            remaining_moves.remove((column, row))
            (m, max_c, max_r) = self.max(remaining_moves, fake_field)
            # Evaluate minimum value
            if m < minimum:
                minimum = m
                min_row = row
                min_column = column
            # Reset position to empty
            fake_field.write(" ", (column, row))

        return minimum, min_column, min_row

    def intelligent_move(self, field: Field):
        fake_field = Field()
        fake_field.set_field(field.copy_field())
        moves = fake_field.available_moves()
        (score, column, row) = self.max(moves, fake_field)
        return column, row

    def get_move(self, field: Field):
        return self.intelligent_move(field)


class Game:
    _current_turn = "X"
    _start_command = "start"
    _exit_command = "exit"
    _player_parameters = ("user", "easy", "medium", "hard")
    _player_one = UserPlayer("X")
    _player_two = EasyPlayer("O")
    _selected_command = ""
    field = Field()

    @staticmethod
    def create_player(player_type, player_sign):
        if player_type == "user":
            return UserPlayer(player_sign)
        elif player_type == "easy":
            return EasyPlayer(player_sign)
        elif player_type == "medium":
            return MediumPlayer(player_sign)
        elif player_type == "hard":
            return HardPlayer(player_sign)

    def start_game(self):
        _valid_parameters = False
        while not _valid_parameters:
            parameters = input("Input command:").split(' ')
            _valid_parameters = self.validate_parameters(parameters)
        return self._selected_command == self._start_command

    def validate_parameters(self, parameters: list):
        if len(parameters) < 1:
            print("Bad parameters!")
            return False

        first_param = parameters[0]
        if first_param == self._exit_command:
            self._selected_command = first_param
            return True

        if len(parameters) != 3:
            print("Bad parameters!")
            return False
        second_param = parameters[1]
        third_param = parameters[2]
        valid_first = first_param == self._start_command
        valid_second = second_param in self._player_parameters
        valid_third = third_param in self._player_parameters

        if not valid_first or not valid_second or not valid_third:
            print("Bad parameters!")
            return False

        self._selected_command = first_param
        self._player_one = Game.create_player(second_param, "X")
        self._player_two = Game.create_player(third_param, "O")
        return True

    def start_with_inputs(self):
        _game_over = False
        start_field = [str(cell) for cell in input("Enter cells:")
                       if cell == "X"
                       or cell == "O"
                       or cell == "_"]

        if len(start_field) != 9:
            print("Invalid initial field")
        else:
            self.field.initialize(start_field)
        while not _game_over:
            _game_over = self.next_turn()

    def start(self):
        while True:
            if self.start_game():
                _game_over = False
                self._current_turn = "X"
                self.field.reset()
                self.field.print_field()
                while not _game_over:
                    _game_over = self.next_turn()
            else:
                break

    def next_turn(self):
        _game_over = False
        if self._current_turn == "X":
            self._player_one.play(self.field)
            _game_over = not self.continue_game(self._player_one.player_sign)
        else:
            self._player_two.play(self.field)
            _game_over = not self.continue_game(self._player_two.player_sign)
        self._current_turn = "X" if self.field.count("X") == self.field.count("O") else "O"
        return _game_over

    def continue_game(self, field_member):
        if self.check_win(field_member):
            return False
        elif not self.field.has_empty_space():
            print("Draw")
            return False
        return True

    def check_win(self, field_member):
        if self.field.check_sequences(field_member):
            print(f"{field_member} wins")
            return True
        return False


game = Game()
game.start()
