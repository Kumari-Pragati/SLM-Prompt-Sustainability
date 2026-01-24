import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(Extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(Extract([[1]]), [1])

    def test_single_element_in_list(self):
        self.assertEqual(Extract([[1, 2, 3]]), [3])

    def test_negative_numbers(self):
        self.assertEqual(Extract([[1, -2, 3], [-4, 5, -6], [7, -8, 9]]), [3, -6, 9])

    def test_mixed_types(self):
        self.assertEqual(Extract([[1, 'two', 3], [4, 'five', 6], [7, 'eight', 9]]), [3, 6, 9])
