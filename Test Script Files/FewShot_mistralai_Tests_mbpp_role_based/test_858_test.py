import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):
    def test_positive_list_length(self):
        self.assertEqual(count_list([1, 2, 3]), 9)

    def test_zero_length_list(self):
        self.assertEqual(count_list([]), 0)

    def test_negative_list_length(self):
        self.assertEqual(count_list([-1, -2, -3]), 9)

    def test_list_with_one_element(self):
        self.assertEqual(count_list([4]), 4)
