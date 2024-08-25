import io
import sys

def test_print_board(self):
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", " ", "O"]
    ]
    expected_output = "X | O | X\n-----\nO | X | O\n-----\nX |   | O\n"
    captured_output = io.StringIO()
    sys.stdout = captured_output
    self.user_module.print_board(board)
    sys.stdout = sys.__stdout__
    if captured_output.getvalue() == expected_output:
        return True, "test_print_board passes!"
    else:
        return False, f"test_print_board failed. Your board did not match the expected output. Expected: {expected_output} Actual: {captured_output.getvalue()}"

def test_check_winner_row(self):
    board = [
        ["X", "X", "X"],
        ["O", " ", "O"],
        [" ", " ", " "]
    ]
    expected_winner = "X"
    actual_winner = self.user_module.check_winner(board)
    if actual_winner == expected_winner:
        return True, "test_check_winner_row passes!"
    else:
        return False, f"test_check_winner_row failed. Expected winner: {expected_winner}, but got: {actual_winner}"

def test_check_winner_column(self):
    board = [
        ["X", "O", " "],
        ["X", "O", " "],
        [" ", "O", "X"]
    ]
    expected_winner = "O"
    actual_winner = self.user_module.check_winner(board)
    if actual_winner == expected_winner:
        return True, "test_check_winner_column passes!"
    else:
        return False, f"test_check_winner_column failed. Expected winner: {expected_winner}, but got: {actual_winner}"

def test_check_winner_diagonal(self):
    board = [
        ["X", "O", " "],
        ["O", "X", " "],
        [" ", "O", "X"]
    ]
    expected_winner = "X"
    actual_winner = self.user_module.check_winner(board)
    if actual_winner == expected_winner:
        return True, "test_check_winner_diagonal passes!"
    else:
        return False, f"test_check_winner_diagonal failed. expected winner: {expected_winner}, but got: {actual_winner}"

def test_get_move(self):
    player = "X"
    expected_move = (1, 1)
    captured_input = io.StringIO("2 2\n")
    sys.stdin = captured_input
    actual_move = self.user_module.get_move(player)
    sys.stdin = sys.__stdin__
    if actual_move == expected_move:
        return True, "test_get_move passes!"
    else:
        return False, f"test_get_move failed. Expected move: {expected_move}, but got: {actual_move}"

def test_is_valid_move(self):
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", " ", "O"]
    ]
    valid_move = (2, 1)
    invalid_move = (0, 0)

    is_valid = self.user_module.is_valid_move(board, valid_move)
    is_invalid = not self.user_module.is_valid_move(board, invalid_move)

    if is_valid and is_invalid:
        return True, "test_is_valid_move passes!"
    else:
        return False, f"test_is_valid_move failed. Failed on valid or invalid move. Valid: {valid_move} Invalid: {invalid_move}"