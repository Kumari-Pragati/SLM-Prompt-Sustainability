import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):
    def test_typical_use_case(self):
        nums = array('i', [1, -2, 3, -4, 5, -6])
        self.assertEqual(negative_count(nums), 0.42)

    def test_all_positive(self):
        nums = array('i', [1, 2, 3, 4, 5])
        self.assertEqual(negative_count(nums), 0.0)

    def test_all_negative(self):
        nums = array('i', [-1, -2, -3, -4, -5])
        self.assertEqual(negative_count(nums), 1.0)

    def test_empty_array(self):
        nums = array('i', [])
        self.assertEqual(negative_count(nums), 0.0)

    def test_single_negative(self):
        nums = array('i', [-1])
        self.assertEqual(negative_count(nums), 1.0)

    def test_single_positive(self):
        nums = array('i', [1])
        self.assertEqual(negative_count(nums), 0.0)

    def test_zero(self):
        nums = array('i', [0])
        self.assertEqual(negative_count(nums), 0.0)
