import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_tuples([], 5), '[]')

    def test_single_tuple(self):
        self.assertEqual(find_tuples([(1, 2, 3)], 3), '[[1, 2, 3]]')

    def test_multiple_tuples(self):
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3), '[[1, 2, 3], [6, 9]]')

    def test_tuples_with_non_divisible_elements(self):
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 4), '[[1, 2, 3], [4, 5, 6]]')

    def test_tuples_with_divisible_elements(self):
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3), '[[1, 2, 3], [6, 9]]')

    def test_tuples_with_divisible_and_non_divisible_elements(self):
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3), '[[1, 2, 3], [6, 9]]')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_tuples('test', 5)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            find_tuples([1, 2, 3], '5')
