import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(count_list([1, 2, 3, 4, 5]), 25)

    def test_negative_numbers_list(self):
        self.assertEqual(count_list([-1, -2, -3]), 9)

    def test_mixed_numbers_list(self):
        self.assertEqual(count_list([1, -2, 3, -4, 5]), 25)
