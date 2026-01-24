import unittest
from mbpp_530_code import negative_count
from array import array

class TestNegativeCount(unittest.TestCase):

    def test_typical_case(self):
        nums = array('i', [1, -2, 3, -4, 5, -6])
        self.assertAlmostEqual(negative_count(nums), 0.42, places=2)

    def test_empty_array(self):
        nums = array('i', [])
        self.assertEqual(negative_count(nums), 0.0)

    def test_all_positive_numbers(self):
        nums = array('i', [1, 2, 3, 4, 5])
        self.assertEqual(negative_count(nums), 0.0)

    def test_all_negative_numbers(self):
        nums = array('i', [-1, -2, -3, -4, -5])
        self.assertEqual(negative_count(nums), 1.0)

    def test_mixed_numbers(self):
        nums = array('i', [1, -2, 3, -4, 5, -6, 7, -8, 9])
        self.assertAlmostEqual(negative_count(nums), 0.44, places=2)
