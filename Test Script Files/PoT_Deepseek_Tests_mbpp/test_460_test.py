import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Extract([('a', 1), ('b', 2)]), ['a', 'b'])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_item_list(self):
        self.assertEqual(Extract([('c',)]), ['c'])

    def test_duplicate_items(self):
        self.assertEqual(Extract([('d', 3), ('d', 4)]), ['d', 'd'])

    def test_negative_values(self):
        self.assertEqual(Extract([('e', -1), ('f', -2)]), ['e', 'f'])

    def test_zero(self):
        self.assertEqual(Extract([('g', 0)]), ['g'])
