import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4]), [2, 3, 4])
        self.assertEqual(add_consecutive_nums([5, 6, 7, 8]), [6, 7, 8])

    def test_zero_at_beginning(self):
        self.assertEqual(add_consecutive_nums([0, 1, 2, 3]), [1, 2, 3])
        self.assertEqual(add_consecutive_nums([0, 0, 1, 2]), [0, 1])

    def test_zero_at_end(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 0]), [2, 3])
        self.assertEqual(add_consecutive_nums([1, 0, 2, 3]), [1, 2])

    def test_empty_list(self):
        self.assertEqual(add_consecutive_nums([]), [])

    def test_single_element(self):
        self.assertEqual(add_consecutive_nums([1]), [])
