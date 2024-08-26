import io
import sys
import traceback

def test_check_winner_row(self):
    board = [
        ["X", "X", "X"],
        ["O", " ", "O"],
        [" ", " ", " "]
    ]
    expected_winner = "X"
    try:
        actual_winner = self.user_module.check_winner(board)
    except Exception as e:
        stacktrace = traceback.format_exc()
        return False, f"`test_check_winner_row` failed with the following error: {stacktrace}"

    if actual_winner == expected_winner:
        return True, "`test_check_winner_row` passes!"
    else:
        return False, f"`test_check_winner_row` failed. Expected winner: {expected_winner}, but got: {actual_winner}"

def test_check_winner_column(self):
    board = [
        ["X", "O", " "],
        ["X", "O", " "],
        [" ", "O", "X"]
    ]
    expected_winner = "O"
    try:
        actual_winner = self.user_module.check_winner(board)
    except Exception as e:
        stacktrace = traceback.format_exc()
        return False, f"`test_check_winner_column` failed with the following error: {stacktrace}"

    if actual_winner == expected_winner:
        return True, "`test_check_winner_column` passes!"
    else:
        return False, f"`test_check_winner_column` failed. Expected winner: {expected_winner}, but got: {actual_winner}"

def test_check_winner_diagonal(self):
    board = [
        ["X", "O", " "],
        ["O", "X", " "],
        [" ", "O", "X"]
    ]
    expected_winner = "X"
    try:
        actual_winner = self.user_module.check_winner(board)
    except Exception as e:
        stacktrace = traceback.format_exc()
        return False, f"`test_check_winner_diagonal` failed with the following error: {stacktrace}"

    if actual_winner == expected_winner:
        return True, "`test_check_winner_diagonal` passes!"
    else:
        return False, f"`test_check_winner_diagonal` failed. Expected winner: {expected_winner}, but got: {actual_winner}"

def test_get_move(self):
    player = "X"
    expected_move = (1, 1)
    captured_input = io.StringIO("2 2\n")
    sys.stdin = captured_input
    try:
        actual_move = self.user_module.get_move(player)
    except Exception as e:
        sys.stdin = sys.__stdin__  # Restore stdin before returning
        stacktrace = traceback.format_exc()
        return False, f"`test_get_move` failed with the following error: {stacktrace}"
    sys.stdin = sys.__stdin__  # Restore stdin

    if actual_move == expected_move:
        return True, "`test_get_move` passes!"
    else:
        return False, f"`test_get_move` failed. Expected move: {expected_move}, but got: {actual_move}"

def test_is_valid_move(self):
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", " ", "O"]
    ]
    valid_move = (2, 1)
    invalid_move = (0, 0)
    try:
        is_valid = self.user_module.is_valid_move(board, valid_move)
        is_invalid = not self.user_module.is_valid_move(board, invalid_move)
    except Exception as e:
        stacktrace = traceback.format_exc()
        return False, f"`test_is_valid_move` failed with the following error: {stacktrace}"

    if is_valid and is_invalid:
        return True, "`test_is_valid_move` passes!"
    else:
        return False, f"`test_is_valid_move` failed. Failed on valid or invalid move. Valid: {valid_move} Invalid: {invalid_move}"