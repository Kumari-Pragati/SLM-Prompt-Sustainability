import unittest
from mbpp_893_code import Extract

class TestExtractFunction(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])
        self.assertEqual(Extract([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), ['c', 'f', 'i'])
        self.assertEqual(Extract([[1], [2], [3]]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_item_lists(self):
        self.assertEqual(Extract([[1, 2, 3]]), [3])
        self.assertEqual(Extract([[4, 5, 6]]), [6])

    def test_single_element_lists(self):
        self.assertEqual(Extract([[1]]), [1])
        self.assertEqual(Extract([[2]]), [2])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            Extract([[1, 'a'], [2, 'b'], [3, 'c']])
