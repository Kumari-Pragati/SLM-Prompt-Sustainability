import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):

    def test_float_sort(self):
        price = [('apple', '1.2'), ('banana', '0.8'), ('cherry', '2.0')]
        expected_output = [('cherry', '2.0'), ('apple', '1.2'), ('banana', '0.8')]
        self.assertEqual(float_sort(price), expected_output)

    def test_float_sort_with_same_prices(self):
        price = [('apple', '1.2'), ('banana', '1.2'), ('cherry', '2.0')]
        expected_output = [('cherry', '2.0'), ('apple', '1.2'), ('banana', '1.2')]
        self.assertEqual(float_sort(price), expected_output)

    def test_float_sort_with_negative_prices(self):
        price = [('apple', '-1.2'), ('banana', '-0.8'), ('cherry', '-2.0')]
        expected_output = [('cherry', '-2.0'), ('apple', '-1.2'), ('banana', '-0.8')]
        self.assertEqual(float_sort(price), expected_output)

    def test_float_sort_with_zero_prices(self):
        price = [('apple', '0'), ('banana', '0'), ('cherry', '0')]
        expected_output = [('cherry', '0'), ('apple', '0'), ('banana', '0')]
        self.assertEqual(float_sort(price), expected_output)
