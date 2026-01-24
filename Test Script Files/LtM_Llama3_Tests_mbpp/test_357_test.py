import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6]]), 6)

    def test_empty(self):
        self.assertIsNone(find_max([]))

    def test_single_element(self):
        self.assertEqual(find_max([[1]]), 1)

    def test_max_value(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_min_value(self):
        self.assertEqual(find_max([[-1, -2, -3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_negative_numbers(self):
        self.assertEqual(find_max([[-1, -2, -3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            find_max([['a', 'b', 'c'], [4, 5, 6], [7, 8, 9]])
