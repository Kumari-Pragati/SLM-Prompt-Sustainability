import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(index_minimum([]))

    def test_single_item_list(self):
        self.assertEqual(index_minimum([(1, 1)]), 1)

    def test_multiple_items_same_min(self):
        self.assertEqual(index_minimum([(1, 1), (2, 2), (3, 3)]), 1)

    def test_multiple_items_different_min(self):
        self.assertEqual(index_minimum([(1, 1), (2, 2), (3, 1)]), 2)

    def test_min_at_beginning(self):
        self.assertEqual(index_minimum([(1, 1), (2, 2), (1, 2)]), 0)

    def test_min_in_middle(self):
        self.assertEqual(index_minimum([(2, 2), (1, 1), (2, 2)]), 1)

    def test_min_at_end(self):
        self.assertEqual(index_minimum([(2, 2), (2, 2), (1, 1)]), 2)

    def test_min_with_non_comparable_types(self):
        with self.assertRaises(TypeError):
            index_minimum([(1, 1), (2, 'a')])

    def test_min_with_non_iterable_input(self):
        with self.assertRaises(TypeError):
            index_minimum(1)
