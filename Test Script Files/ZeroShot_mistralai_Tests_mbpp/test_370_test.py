import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(float_sort([]), [])

    def test_single_item(self):
        self.assertListEqual(float_sort([['1', '1']]), [['1', '1']])

    def test_multiple_items(self):
        self.assertListEqual(float_sort([['2.5', '2.5'], ['1.0', '1.0'], ['3.0', '3.0']]), [['3.0', '3.0'], ['2.5', '2.5'], ['1.0', '1.0']])

    def test_mixed_types(self):
        self.assertRaises(TypeError, float_sort, [['1', '1'], 2, 3.0])
