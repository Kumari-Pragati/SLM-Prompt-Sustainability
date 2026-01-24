import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(mul_list([]), [])
        self.assertListEqual(mul_list([], [1, 2, 3]), [])

    def test_single_element_lists(self):
        self.assertListEqual(mul_list([1], [2, 3]), [2, 3, 2])
        self.assertListEqual(mul_list([2, 3], [1]), [2, 3])

    def test_simple_lists(self):
        self.assertListEqual(mul_list([1, 2], [3, 4]), [3, 4, 6, 2, 4])
        self.assertListEqual(mul_list([3, 4], [1, 2]), [3, 4, 6, 8])

    def test_negative_numbers(self):
        self.assertListEqual(mul_list([-1, 2], [3, -4]), [-3, 4, -6, 8])
        self.assertListEqual(mul_list([3, -4], [-1, 2]), [-3, 4, -6, -8])

    def test_zero(self):
        self.assertListEqual(mul_list([0], [1, 2, 3]), [0, 0, 0])
        self.assertListEqual(mul_list([1, 2, 3], [0]), [0, 0, 0])
