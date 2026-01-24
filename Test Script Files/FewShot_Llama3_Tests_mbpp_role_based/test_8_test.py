import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(square_nums([]), [])

    def test_single_element(self):
        self.assertEqual(square_nums([5]), [25])

    def test_multiple_elements(self):
        self.assertEqual(square_nums([1, 2, 3, 4]), [1, 4, 9, 16])

    def test_negative_numbers(self):
        self.assertEqual(square_nums([-1, -2, -3, -4]), [1, 4, 9, 16])

    def test_non_integer_numbers(self):
        self.assertEqual(square_nums([1.5, 2.5, 3.5, 4.5]), [1.5625, 6.5625, 12.5625, 20.5625])
