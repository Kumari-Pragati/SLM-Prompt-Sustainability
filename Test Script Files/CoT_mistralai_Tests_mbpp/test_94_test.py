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

    def test_list_with_non_tuple_elements(self):
        self.assertRaises(TypeError, index_minimum, [1, 2, 3])

    def test_list_with_non_number_second_elements(self):
        self.assertRaises(TypeError, index_minimum, [(1, 'a'), (2, 'b'), (3, 'c')])
