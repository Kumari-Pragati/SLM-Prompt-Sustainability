import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_tuples([], 5), '[]')

    def test_no_tuples(self):
        self.assertEqual(find_tuples([[1, 2, 3], [4, 5, 6]], 7), '[]')

    def test_tuples(self):
        self.assertEqual(find_tuples([[0, 0, 0], [5, 5, 5], [10, 10, 10]], 5), '[[0, 0, 0], [5, 5, 5], [10, 10, 10]]')

    def test_tuples_with_duplicates(self):
        self.assertEqual(find_tuples([[0, 0, 0, 0], [5, 5, 5, 5], [10, 10, 10, 10]], 5), '[[0, 0, 0, 0], [5, 5, 5, 5], [10, 10, 10, 10]]')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_tuples('test', 5)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            find_tuples([[1, 2, 3]], '5')
