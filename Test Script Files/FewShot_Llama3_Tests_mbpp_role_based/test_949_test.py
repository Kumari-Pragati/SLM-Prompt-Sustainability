import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_list([]), '[]')

    def test_single_element_list(self):
        self.assertEqual(sort_list([123]), '[123]')

    def test_multiple_elements_list(self):
        self.assertEqual(sort_list([123, 456, 789]), '[123, 456, 789]')

    def test_list_with_duplicates(self):
        self.assertEqual(sort_list([123, 123, 456, 789]), '[123, 123, 456, 789]')

    def test_list_with_negative_numbers(self):
        self.assertEqual(sort_list([-123, 456, -789]), '[-123, -789, 456]')

    def test_list_with_zero(self):
        self.assertEqual(sort_list([0, 123, 456, 789]), '[0, 123, 456, 789]')

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            sort_list([123, 'abc', 456, 789])
