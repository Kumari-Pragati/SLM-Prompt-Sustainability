import unittest
from mbpp_460_code import Extract

class TestExtractFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(Extract([]), [])

    def test_single_item_list(self):
        self.assertListEqual(Extract([(1,)]), [1])

    def test_multi_item_list(self):
        self.assertListEqual(Extract([(1, 2), (3, 4), (5, 6)]), [1, 3, 5])

    def test_list_with_non_tuple_items(self):
        self.assertRaises(TypeError, Extract, [1, 2, 3])
