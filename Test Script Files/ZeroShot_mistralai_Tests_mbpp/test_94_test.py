import unittest
from mbpp_94_code import itemgetter
from 94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(index_minimum([]))

    def test_single_item_list(self):
        self.assertEqual(index_minimum([(1, 1)]), 1)

    def test_multiple_items_same_value(self):
        self.assertEqual(index_minimum([(1, 2), (1, 2), (1, 3)]), 1)

    def test_multiple_items_different_values(self):
        self.assertEqual(index_minimum([(1, 2), (3, 4), (1, 5)]), 1)

    def test_negative_numbers(self):
        self.assertEqual(index_minimum([(-1, 2), (-3, 4), (-1, 5)]), -1)

    def test_floats(self):
        self.assertAlmostEqual(index_minimum([(1.1, 2), (3.3, 4), (1.2, 5)]), 1.1)
