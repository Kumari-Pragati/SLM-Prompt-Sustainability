import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(Extract([[1]]), [1])

    def test_list_with_single_value(self):
        self.assertEqual(Extract([1, 2, 3]), [1, 2, 3])

    def test_list_with_non_integer_values(self):
        with self.assertRaises(TypeError):
            Extract([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])

    def test_list_with_non_list_values(self):
        with self.assertRaises(TypeError):
            Extract('12345')
