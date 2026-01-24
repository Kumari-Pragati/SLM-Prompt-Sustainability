import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertListEqual(div_list([1, 2, 3], [1, 2, 3]), [1.0, 1.5, 1.5])

    def test_zero_in_first_list(self):
        self.assertListEqual(div_list([0, 1, 2], [1, 2, 3]), [0.0, 0.5, 0.6666666666666666])

    def test_zero_in_second_list(self):
        self.assertListEqual(div_list([1, 2, 3], [0, 0, 0]), [1.0, 2.0, 3.0])

    def test_mixed_zeros(self):
        self.assertListEqual(div_list([0, 1, 2, 0], [1, 0, 3, 0]), [0.0, 1.0, 0.6666666666666666, 0.0])

    def test_negative_numbers(self):
        self.assertListEqual(div_list([-1, -2, -3], [-1, -2, -3]), [-1.0, -1.0, -1.0])
