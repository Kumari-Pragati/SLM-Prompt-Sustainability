import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(big_diff([1, 2, 3, 4, 5]), 4)

    def test_negative_numbers(self):
        self.assertEqual(big_diff([-1, -2, -3, -4, -5]), 4)

    def test_mixed_numbers(self):
        self.assertEqual(big_diff([1, -2, 3, -4, 5]), 8)

    def test_single_element_list(self):
        self.assertEqual(big_diff([1]), 0)

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            big_diff([])

    def test_non_numeric_list(self):
        with self.assertRaises(TypeError):
            big_diff(['a', 'b', 'c'])
