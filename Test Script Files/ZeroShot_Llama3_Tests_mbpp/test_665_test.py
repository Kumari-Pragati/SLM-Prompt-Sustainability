import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):

    def test_move_last(self):
        self.assertEqual(move_last([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])
        self.assertEqual(move_last([1, 1, 2, 2, 3, 3]), [2, 2, 3, 3, 1, 1])
        self.assertEqual(move_last([1, 2, 3, 4, 5, 5]), [2, 3, 4, 5, 5, 1])
        self.assertEqual(move_last([1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 1])
        self.assertEqual(move_last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])

    def test_move_last_empty_list(self):
        self.assertEqual(move_last([]), [])

    def test_move_last_single_element_list(self):
        self.assertEqual(move_last([1]), [1])

    def test_move_last_all_same_element_list(self):
        self.assertEqual(move_last([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
