import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_unique([]), '{}')

    def test_single_element_list(self):
        self.assertEqual(get_unique([['a', 1]]), '{"1": 1}')

    def test_multiple_elements_list(self):
        self.assertEqual(get_unique([['a', 1], ['b', 1], ['c', 2]]), '{"1": 2, "2": 1}')

    def test_multiple_elements_list_with_duplicates(self):
        self.assertEqual(get_unique([['a', 1], ['a', 1], ['b', 1], ['c', 2]]), '{"1": 2, "2": 1}')

    def test_list_with_negative_numbers(self):
        self.assertEqual(get_unique([['a', -1], ['b', 1], ['c', 2]]), '{"-1": 1, "1": 1, "2": 1}')

    def test_list_with_zero(self):
        self.assertEqual(get_unique([['a', 0], ['b', 1], ['c', 2]]), '{"0": 1, "1": 1, "2": 1'})

    def test_list_with_non_integer_values(self):
        self.assertEqual(get_unique([['a', 1.0], ['b', 1], ['c', 2]]), '{"1.0": 1, "2": 1}')
