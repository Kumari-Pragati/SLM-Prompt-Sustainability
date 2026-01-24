import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):

    def test_add_consecutive_nums(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4]), [3, 5])
        self.assertEqual(add_consecutive_nums([-1, 1, 2, 3]), [1, 3, 5])
        self.assertEqual(add_consecutive_nums([10, 20, 30, 40]), [30, 50])
        self.assertEqual(add_consecutive_nums([5, 5, 5, 5]), [5, 5, 5])
        self.assertEqual(add_consecutive_nums([1, 1, 1, 1]), [2, 2, 2])

    def test_add_consecutive_nums_empty_list(self):
        self.assertEqual(add_consecutive_nums([]), [])

    def test_add_consecutive_nums_single_element_list(self):
        self.assertEqual(add_consecutive_nums([1]), [])

    def test_add_consecutive_nums_two_element_list(self):
        self.assertEqual(add_consecutive_nums([1, 2]), [])
