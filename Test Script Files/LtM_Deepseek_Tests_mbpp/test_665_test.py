import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(move_last([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_single_element(self):
        self.assertEqual(move_last([1]), [1])

    def test_empty_list(self):
        self.assertEqual(move_last([]), [])

    def test_all_same_elements(self):
        self.assertEqual(move_last([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_all_different_elements(self):
        self.assertEqual(move_last([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_repeated_elements(self):
        self.assertEqual(move_last([1, 2, 2, 3]), [1, 2, 2, 3])

    def test_large_numbers(self):
        self.assertEqual(move_last([100, 200, 300]), [100, 200, 300])

    def test_negative_numbers(self):
        self.assertEqual(move_last([-1, -2, -3]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(move_last([-1, 0, 1]), [-1, 0, 1])
