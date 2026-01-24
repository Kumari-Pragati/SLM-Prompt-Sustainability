import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(find_max([[5]]), 5)

    def test_multiple_elements_list(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6]]), 6)

    def test_empty_list(self):
        self.assertRaises(ValueError, find_max, [])

    def test_non_integer_list(self):
        with self.assertRaises(TypeError):
            find_max([['a', 'b', 'c'], ['d', 'e', 'f']])

    def test_mixed_integer_and_non_integer_list(self):
        with self.assertRaises(TypeError):
            find_max([['a', 'b', 'c'], [1, 2, 3]])
