import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):
    def test_typical_use_case(self):
        data = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        self.assertEqual(find_minimum_range(data), (1, 8))

    def test_empty_list(self):
        self.assertIsNone(find_minimum_range([]))

    def test_single_list(self):
        data = [[1]]
        self.assertEqual(find_minimum_range(data), (1, 1))

    def test_single_value_list(self):
        data = [[1]]
        self.assertEqual(find_minimum_range(data), (1, 1))

    def test_single_value_list_empty(self):
        data = [[]]
        self.assertIsNone(find_minimum_range(data))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_minimum_range(123)
