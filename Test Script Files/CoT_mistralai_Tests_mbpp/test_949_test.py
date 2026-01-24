import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_list([]), '[]')

    def test_single_element(self):
        self.assertEqual(sort_list([1]), '[1]')
        self.assertEqual(sort_list([0]), '[0]')
        self.assertEqual(sort_list([-1]), '[-1]')

    def test_multiple_elements(self):
        self.assertEqual(sort_list([1, 10, 2, 3, 4]), '[0, 1, 2, 3, 10]')
        self.assertEqual(sort_list([-1, -10, -2, -3, -4]), '[-4, -10, -3, -2, -1]')
        self.assertEqual(sort_list([1.1, 10.01, 2, 3, 4]), '[2, 3, 4, 1.1, 10.01]')

    def test_mixed_types(self):
        self.assertEqual(sort_list([1, 'a', 10, 2.5]), '[1, 2.5, 10, a]')

    def test_duplicates(self):
        self.assertEqual(sort_list([1, 1, 10, 2, 2, 3, 3]), '[1, 1, 10, 2, 2, 3, 3]')

    def test_large_numbers(self):
        self.assertEqual(sort_list([123456789, 987654321]), '[123456789, 987654321]')

    def test_negative_numbers(self):
        self.assertEqual(sort_list([-123456789, -987654321]), '[-987654321, -123456789]')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_list('string')
        with self.assertRaises(TypeError):
            sort_list([None])
