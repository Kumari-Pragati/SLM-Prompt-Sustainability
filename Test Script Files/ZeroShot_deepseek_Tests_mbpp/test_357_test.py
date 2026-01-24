import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):

    def test_find_max_with_integers(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_find_max_with_floats(self):
        self.assertEqual(find_max([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]), 9.9)

    def test_find_max_with_negative_numbers(self):
        self.assertEqual(find_max([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -1)

    def test_find_max_with_mixed_numbers(self):
        self.assertEqual(find_max([[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]), 8)

    def test_find_max_with_empty_list(self):
        self.assertIsNone(find_max([]))

    def test_find_max_with_single_element(self):
        self.assertEqual(find_max([[1]]), 1)

    def test_find_max_with_nested_empty_list(self):
        self.assertIsNone(find_max([[], []]))
