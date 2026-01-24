import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(big_diff([10, 2, 7, 2]), 8)

    def test_single_element(self):
        self.assertEqual(big_diff([5]), 0)

    def test_negative_numbers(self):
        self.assertEqual(big_diff([-10, -2, -7, -2]), 8)

    def test_same_elements(self):
        self.assertEqual(big_diff([1, 1, 1, 1]), 0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            big_diff([])

    def test_large_numbers(self):
        self.assertEqual(big_diff([1000000, 200000, 700000, 200000]), 800000)

    def test_float_numbers(self):
        self.assertAlmostEqual(big_diff([10.5, 2.5, 7.5, 2.5]), 8.0)
