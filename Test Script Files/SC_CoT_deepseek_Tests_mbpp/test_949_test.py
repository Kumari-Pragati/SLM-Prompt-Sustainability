import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_list([123, 45, 678]), '[45, 123, 678]')

    def test_empty_list(self):
        self.assertEqual(sort_list([]), '[]')

    def test_single_element(self):
        self.assertEqual(sort_list([1]), '[1]')

    def test_same_number_of_digits(self):
        self.assertEqual(sort_list([10, 20, 30]), '[10, 20, 30]')

    def test_different_number_of_digits(self):
        self.assertEqual(sort_list([1, 10, 100]), '[1, 10, 100]')

    def test_negative_numbers(self):
        self.assertEqual(sort_list([-123, -45, -678]), '[-678, -123, -45]')

    def test_mixed_positive_negative(self):
        self.assertEqual(sort_list([123, -45, 678, -100]), '[-100, -45, 123, 678]')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_list('123')
