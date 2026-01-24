import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(float_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(float_sort([['apple', '1.0']]), [['apple', '1.0']])

    def test_multiple_elements_list(self):
        self.assertEqual(float_sort([['apple', '1.0'], ['banana', '2.0'], ['cherry', '3.0']]), [['cherry', '3.0'], ['banana', '2.0'], ['apple', '1.0']])

    def test_negative_numbers(self):
        self.assertEqual(float_sort([['apple', '-1.0'], ['banana', '2.0'], ['cherry', '3.0']]), [['cherry', '3.0'], ['banana', '2.0'], ['apple', '-1.0']])

    def test_decimal_numbers(self):
        self.assertEqual(float_sort([['apple', '1.5'], ['banana', '2.0'], ['cherry', '3.0']]), [['cherry', '3.0'], ['banana', '2.0'], ['apple', '1.5']])
