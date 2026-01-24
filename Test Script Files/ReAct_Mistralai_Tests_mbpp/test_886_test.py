import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):

    def test_empty_list(self):
        """Tests sum_num with an empty list"""
        with self.assertRaises(ZeroDivisionError):
            sum_num([])

    def test_single_element(self):
        """Tests sum_num with a single element"""
        result = sum_num([1])
        self.assertEqual(result, 1.0)

    def test_positive_numbers(self):
        """Tests sum_num with multiple positive numbers"""
        result = sum_num([1, 2, 3, 4, 5])
        self.assertEqual(result, 3.0)

    def test_negative_numbers(self):
        """Tests sum_num with multiple negative numbers"""
        result = sum_num([-1, -2, -3, -4, -5])
        self.assertEqual(result, -3.0)

    def test_mixed_numbers(self):
        """Tests sum_num with a mix of positive and negative numbers"""
        result = sum_num([1, -2, 3, -4, 5])
        self.assertEqual(result, 2.0)

    def test_zero(self):
        """Tests sum_num with a zero number"""
        result = sum_num([0])
        self.assertEqual(result, 0.0)

    def test_floats(self):
        """Tests sum_num with floats"""
        result = sum_num([1.5, 2.5, 3.5])
        self.assertEqual(round(result, 1), 2.5)

    def test_large_numbers(self):
        """Tests sum_num with large numbers"""
        result = sum_num([1000000, 2000000, 3000000])
        self.assertEqual(round(result, 1), 2.0)
