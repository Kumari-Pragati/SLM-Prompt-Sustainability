import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(Extract([]), [])

    def test_single_item_list(self):
        self.assertListEqual(Extract([[1]]), [1])

    def test_multiple_items_list(self):
        self.assertListEqual(Extract([[1], [2], [3]]), [3, 2, 1])

    def test_list_with_non_list_elements(self):
        self.assertRaises(TypeError, Extract, [[1], 'a', 2])

    def test_list_with_empty_elements(self):
        self.assertListEqual(Extract([[], [1], [], [2]]), [2, 1])

    def test_list_with_negative_index(self):
        self.assertRaises(IndexError, Extract, [[-1]])
