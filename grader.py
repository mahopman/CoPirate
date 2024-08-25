from enum import Enum
import importlib.util
import io
import sys

class HomeworkType(Enum):
    TICTACTOE = 0
    CALCULATOR = 1
    SORTING_ALGORITHM = 2
    CAESAR_CIPHER = 3


def grade_assignment(code: str, homework: HomeworkType):
    save_code_to_file(code, "user_code.py")
    user_module = import_code("user_code.py")
    if homework == HomeworkType.TICTACTOE:
        grader = TicTacToeGrader(user_module)
    passes, test_messages = grader.grade_assignment()
    test_results = ""
    if passes:
        test_results = """
        ### :white_check_mark: Congratulations!
        **Your code passes all tests!**
        """
    else:
        test_results = """
        ### :x: Your code did not pass all tests.
        """
        for test_message in test_messages:
            test_results = test_results + "\n- " + test_message

    return passes, test_results

def save_code_to_file(code, filename):
    with open(filename, "w") as file:
        file.write(code)

def import_code(filename):
    spec = importlib.util.spec_from_file_location("user_code", filename)
    user_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(user_module)
    return user_module

class TicTacToeGrader():
    def __init__(self, user_module):
        self.user_module = user_module
        self.tests = [
            self.test_check_winner_row,
            self.test_check_winner_column,
            self.test_check_winner_diagonal, 
            self.test_get_move, 
            self.test_is_valid_move
        ]

    def grade_assignment(self):
        passes = []
        test_messages = []
        for test in self.tests:
            test_pass, message = test()
            passes.append(test_pass)
            test_messages.append(message)
        
        return False not in passes, test_messages

    def test_check_winner_row(self):
        board = [
            ["X", "X", "X"],
            ["O", " ", "O"],
            [" ", " ", " "]
        ]
        expected_winner = "X"
        actual_winner = self.user_module.check_winner(board)
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
        actual_winner = self.user_module.check_winner(board)
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
        actual_winner = self.user_module.check_winner(board)
        if actual_winner == expected_winner:
            return True, "`test_check_winner_diagonal` passes!"
        else:
            return False, f"`test_check_winner_diagonal` failed. expected winner: {expected_winner}, but got: {actual_winner}"

    def test_get_move(self):
        player = "X"
        expected_move = (1, 1)
        captured_input = io.StringIO("2 2\n")
        sys.stdin = captured_input
        actual_move = self.user_module.get_move(player)
        sys.stdin = sys.__stdin__
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

        is_valid = self.user_module.is_valid_move(board, valid_move)
        is_invalid = not self.user_module.is_valid_move(board, invalid_move)

        if is_valid and is_invalid:
            return True, "`test_is_valid_move` passes!"
        else:
            return False, f"`test_is_valid_move` failed. Failed on valid or invalid move. Valid: {valid_move} Invalid: {invalid_move}"
