import unittest
from mbpp_105_code import count

class TestCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(count([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(count([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(count([1, -2, 3, -4]), 0)
