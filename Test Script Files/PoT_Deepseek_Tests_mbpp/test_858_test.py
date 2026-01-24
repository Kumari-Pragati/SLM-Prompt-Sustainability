import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_list([1, 2, 3]), 9)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_large_list(self):
        self.assertEqual(count_list(list(range(1000))), 1000000)

    def test_negative_elements(self):
        self.assertEqual(count_list([-1, -2, -3]), 9)

    def test_zero_elements(self):
        self.assertEqual(count_list([0, 0, 0]), 9)

    def test_mixed_elements(self):
        self.assertEqual(count_list([1, -1, 0]), 9)
