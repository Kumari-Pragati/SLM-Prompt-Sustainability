import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):

    def test_move_last_single_element(self):
        self.assertEqual(move_last([1]), [1])

    def test_move_last_same_elements(self):
        self.assertEqual(move_last([1, 1, 1]), [1, 1, 1])

    def test_move_last_different_elements(self):
        self.assertEqual(move_last([1, 2, 3]), [1, 2, 3])

    def test_move_last_mixed_elements(self):
        self.assertEqual(move_last([1, 2, 2, 1]), [1, 2, 2, 1])

    def test_move_last_first_element_last(self):
        self.assertEqual(move_last([2, 1]), [1, 2])

    def test_move_last_multiple_first_elements_last(self):
        self.assertEqual(move_last([2, 1, 1]), [1, 1, 2])

    def test_move_last_multiple_different_elements_last(self):
        self.assertEqual(move_last([2, 1, 3]), [1, 2, 3])

    def test_move_last_empty_list(self):
        self.assertEqual(move_last([]), [])
