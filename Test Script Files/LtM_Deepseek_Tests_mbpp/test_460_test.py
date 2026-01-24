import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(Extract([('a', 1), ('b', 2)]), ['a', 'b'])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_item_list(self):
        self.assertEqual(Extract([('c',)]), ['c'])

    def test_mixed_type_list(self):
        self.assertEqual(Extract([('d', 3), (4, 'e'), ('f',)]), ['d', 4, 'f'])

    def test_negative_values(self):
        self.assertEqual(Extract([('g', -1), ('h', -2)]), ['g', 'h'])

    def test_zero_values(self):
        self.assertEqual(Extract([('i', 0), ('j', 0)]), ['i', 'j'])

    def test_large_values(self):
        self.assertEqual(Extract([('k', 1000), ('l', 2000)]), ['k', 'l'])
