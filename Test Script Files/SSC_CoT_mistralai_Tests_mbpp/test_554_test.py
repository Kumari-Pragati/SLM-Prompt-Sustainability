import unittest
from mbpp_554_code import Split

class TestSplitFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(Split([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_empty_list(self):
        self.assertListEqual(Split([]), [])

    def test_single_element_list(self):
        self.assertListEqual(Split([1]), [1])

    def test_all_even_list(self):
        self.assertListEqual(Split([2, 4, 6]), [])

    def test_all_odd_list(self):
        self.assertListEqual(Split([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_negative_numbers(self):
        self.assertListEqual(Split([-1, -3, -5]), [-1, -3])
