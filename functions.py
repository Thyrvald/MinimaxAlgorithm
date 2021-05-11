from random import randint
from copy import deepcopy


class TicTacToeNode:
    def __init__(self, root=None):
        self.root = root
        self.children = []
        self.game_field_values = []
        if self.root is not None:
            self.game_field_values = deepcopy(root.game_field_values)
            self.fields_taken = deepcopy(root.fields_taken)
        else:
            for i in range(3):
                self.game_field_values.append([0, 0, 0])
            self.fields_taken = []
        self.is_terminal = False
        self.min_move = False
        self.min_mark = -1
        self.max_move = True
        self.max_mark = 1
        self.payment = 10
        self.heuristic = 1000

    def __str__(self):
        board = ''
        for row in self.game_field_values:
            board += '|'
            for value in row:
                if value == self.max_mark:
                    board += 'x|'
                elif value == self.min_mark:
                    board += 'o|'
                else:
                    board += ' |'
            board += '\n'
        return board

    def set_payment(self, value):
        self.payment = value
        return self.payment

    def set_heuristic(self, value):
        self.heuristic = value
        return self.heuristic

    def change_moving_player(self):
        if self.max_move:
            self.max_move = False
            self.min_move = True
        else:
            self.max_move = True
            self.min_move = False

    def set_game_fields(self, new_fields):
        self.game_field_values = new_fields

    def player_move(self, i, j):
        if self.max_move:
            self.game_field_values[i][j] = self.max_mark
        elif self.min_move:
            self.game_field_values[i][j] = self.min_mark
        self.fields_taken.append((i, j))
        self.check_if_game_finished()

    def set_terminal(self):
        self.is_terminal = True

    def check_if_game_finished(self):
        fields_sum = 0

        # checking if there is a win in any of the rows

        for i in range(3):
            for j in self.game_field_values[i]:
                fields_sum += j
            if self.check_who_won(fields_sum) != 0:
                self.set_terminal()
                return self.check_who_won(fields_sum)
            else:
                fields_sum = 0

        # checking if there is a win on any of the diagonals

        j = 0
        for i in range(3):
            fields_sum += self.game_field_values[i][j]
            j += 1
        if self.check_who_won(fields_sum) != 0:
            self.set_terminal()
            return self.check_who_won(fields_sum)
        else:
            fields_sum = 0
        j = 2
        for i in range(3):
            fields_sum += self.game_field_values[i][j]
            j -= 1
        if self.check_who_won(fields_sum) != 0:
            self.set_terminal()
            return self.check_who_won(fields_sum)
        else:
            fields_sum = 0

        # checking if there is a win in any of the columns

        for i in range(3):
            for j in range(3):
                fields_sum += self.game_field_values[j][i]
            if self.check_who_won(fields_sum) != 0:
                self.set_terminal()
                return self.check_who_won(fields_sum)
            else:
                fields_sum = 0
        if len(self.fields_taken) == 9:
            self.set_terminal()
        return 0

    def check_who_won(self, fields_sum):
        if fields_sum == 3:
            return self.max_mark
        elif fields_sum == -3:
            return self.min_mark
        else:
            return 0

    def is_field_taken(self, coordinates):
        if len(self.fields_taken) > 0:
            for field in self.fields_taken:
                if coordinates == field:
                    return True
            return False
        else:
            return False


def add_node_children(root_node):
    i = j = 0
    if not root_node.is_terminal:
        while i < 3:
            new_node = TicTacToeNode(root_node)
            if new_node.is_field_taken((i, j)):
                if j < 2:
                    j += 1
                else:
                    j = 0
                    i += 1
            else:
                if new_node.root.max_move == new_node.max_mark and new_node.root.root is not None:
                    new_node.change_moving_player()
                new_node.player_move(i, j)
                root_node.children.append(new_node)
                if j < 2:
                    j += 1
                else:
                    j = 0
                    i += 1
    for child in root_node.children:
        add_node_children(child)


def make_tree():
    game_board = TicTacToeNode()
    add_node_children(game_board)
    return game_board


def random_game(game_board):
    current_game_node = game_board
    while current_game_node is not current_game_node.is_terminal and len(current_game_node.fields_taken) < 9 and len(
            current_game_node.children) > 0:
        current_game_node = current_game_node.children[randint(0, len(current_game_node.children) - 1)]
    print(current_game_node)
    return current_game_node.check_if_game_finished()


def minimax_full(game_board):
    # function evaluates payment for each node

    if game_board.is_terminal:
        return game_board.set_payment(game_board.check_if_game_finished())
    else:
        payments = []
        for child_board in game_board.children:
            payments.append(minimax_full(child_board))
        if game_board.max_move:
            return game_board.set_payment(max(payments))
        else:
            return game_board.set_payment(min(payments))


def minimax_full_game(game_board):
    # function plays a game using minimax_full algorithm

    current_game_node = game_board
    minimax_full(game_board)
    while current_game_node is not current_game_node.is_terminal and len(current_game_node.fields_taken) < 9 and len(
            current_game_node.children) > 0:
        payments = []
        for child in current_game_node.children:
            payments.append(child.payment)
        if current_game_node.max_move:
            tmp_node = current_game_node.children[randint(0, len(current_game_node.children) - 1)]
            while tmp_node.payment != max(payments):
                tmp_node = current_game_node.children[randint(0, len(current_game_node.children) - 1)]
            current_game_node = tmp_node
        elif current_game_node.min_move:
            tmp_node = current_game_node.children[randint(0, len(current_game_node.children) - 1)]
            while tmp_node.payment != min(payments):
                tmp_node = current_game_node.children[randint(0, len(current_game_node.children) - 1)]
            current_game_node = tmp_node
    print(current_game_node)
    return current_game_node.check_if_game_finished()


def heuristic(game_board):
    # functions checks the number of positions available for x to win, and for y to win, and after that it returns
    # a difference between those two numbers

    x_win_possibilities = 0
    y_win_possibilities = 0

    # checking if there are win possibilities for x in rows

    for i in range(3):
        y_count = 0
        for j in game_board.game_field_values[i]:
            if game_board.game_field_values[i][j] == -1:
                y_count += 1
        if y_count == 0:
            x_win_possibilities += 1
        else:
            continue

    # checking if there are win possibilities for x in columns

    j = 0
    while j < 3:
        y_count = 0
        for i in range(3):
            if game_board.game_field_values[i][j] == -1:
                y_count += 1
        if y_count == 0:
            x_win_possibilities += 1
        j += 1

    # checking if there is a win possibility for x on any of the diagonals

    j = 0
    y_count = 0
    for i in range(3):
        if game_board.game_field_values[i][j] == -1:
            y_count += 1
        j += 1
    if y_count == 0:
        x_win_possibilities += 1
    else:
        y_count = 0
    j = 2
    for i in range(3):
        if game_board.game_field_values[i][j] == -1:
            y_count += 1
        j -= 1
    if y_count == 0:
        x_win_possibilities += 1

        # checking if there are win possibilities for y in rows

        for i in range(3):
            x_count = 0
            for j in game_board.game_field_values[i]:
                if game_board.game_field_values[i][j] == 1:
                    x_count += 1
            if x_count == 0:
                y_win_possibilities += 1
            else:
                continue

        # checking if there are win possibilities for y in columns

        j = 0
        while j < 3:
            x_count = 0
            for i in range(3):
                if game_board.game_field_values[i][j] == 1:
                    x_count += 1
            if x_count == 0:
                y_win_possibilities += 1
            j += 1

        # checking if there is a win possibility for y on any of the diagonals

        j = 0
        x_count = 0
        for i in range(3):
            if game_board.game_field_values[i][j] == 1:
                x_count += 1
            j += 1
        if x_count == 0:
            y_win_possibilities += 1
        else:
            x_count = 0
        j = 2
        for i in range(3):
            if game_board.game_field_values[i][j] == 1:
                x_count += 1
            j -= 1
        if x_count == 0:
            y_win_possibilities += 1

    return x_win_possibilities - y_win_possibilities


def minimax(game_board, search_depth):
    if game_board.is_terminal or search_depth == 0:
        return game_board.set_heuristic(heuristic(game_board))
    else:
        heuristics = []
        for child_board in game_board.children:
            heuristics.append(minimax(child_board, search_depth - 1))
        if game_board.max_move:
            return game_board.set_heuristic(max(heuristics))
        else:
            return game_board.set_heuristic(min(heuristics))


def minimax_game(game_board, search_depth):
    # function plays a game using minimax algorithm with heuristic

    current_game_node = game_board
    minimax(game_board, search_depth)
    countdown_to_next_minimax = search_depth
    while not current_game_node.is_terminal and len(current_game_node.fields_taken) < 9 and len(
            current_game_node.children) > 0:
        if countdown_to_next_minimax == 0:
            countdown_to_next_minimax = search_depth
            minimax(current_game_node, search_depth)
        heuristics = []
        for child in current_game_node.children:
            if child.heuristic != 1000:
                heuristics.append(child.heuristic)
            else:
                continue
        if current_game_node.max_move:
            tmp_node = current_game_node.children[randint(0, len(current_game_node.children) - 1)]
            while tmp_node.heuristic != max(heuristics):
                tmp_node = current_game_node.children[randint(0, len(current_game_node.children) - 1)]
            current_game_node = tmp_node
        elif current_game_node.min_move:
            tmp_node = current_game_node.children[randint(0, len(current_game_node.children) - 1)]
            while tmp_node.heuristic != min(heuristics):
                tmp_node = current_game_node.children[randint(0, len(current_game_node.children) - 1)]
            current_game_node = tmp_node
        countdown_to_next_minimax -= 1

    print(current_game_node)
    return current_game_node.check_if_game_finished()


