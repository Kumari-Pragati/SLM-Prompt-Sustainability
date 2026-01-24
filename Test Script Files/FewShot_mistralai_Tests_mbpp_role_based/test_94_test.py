import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):
    def test_minimum_with_valid_list(self):
        self.assertEqual(index_minimum([(1, 2), (3, 4), (2, 1)]), (1, 2))
        self.assertEqual(index_minimum([(0, 0), (1, 1), (2, 2)]), (0, 0))

    def test_minimum_with_empty_list(self):
        self.assertIsNone(index_minimum([]))

    def test_minimum_with_single_item_list(self):
        self.assertEqual(index_minimum([(1, 1)]), (1, 1))

    def test_minimum_with_list_of_tuples_of_different_lengths(self):
        self.assertRaises(ValueError, index_minimum, [(1, 2), (3, 4), (2, 1), (5,)])
