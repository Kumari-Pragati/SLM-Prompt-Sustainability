import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_item_list(self):
        self.assertEqual(Extract([[1]]), [1])

    def test_negative_index(self):
        self.assertEqual(Extract([[-1, -2, -3]]), [-3])

    def test_list_with_non_list_item(self):
        self.assertEqual(Extract([[1, 2, 3], "test", [4, 5, 6]]), [3, "test", 6])
