import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(add_consecutive_nums([1]), [])

    def test_two_element_list(self):
        self.assertEqual(add_consecutive_nums([1, 2]), [])

    def test_three_element_list(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3]), [1])

    def test_four_element_list(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4]), [1, 2])

    def test_five_element_list(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(add_consecutive_nums([]), [])
