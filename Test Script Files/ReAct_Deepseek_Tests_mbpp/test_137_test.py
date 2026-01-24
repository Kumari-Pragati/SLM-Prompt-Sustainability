import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):

    def test_typical_case(self):
        nums = array('i', [1, 0, 2, 0, 3])
        self.assertAlmostEqual(zero_count(nums), 0.4, places=2)

    def test_all_zeros(self):
        nums = array('i', [0, 0, 0, 0, 0])
        self.assertAlmostEqual(zero_count(nums), 1.0, places=2)

    def test_all_non_zeros(self):
        nums = array('i', [1, 2, 3, 4, 5])
        self.assertAlmostEqual(zero_count(nums), 0.0, places=2)

    def test_empty_array(self):
        nums = array('i', [])
        self.assertAlmostEqual(zero_count(nums), 0.0, places=2)

    def test_single_zero(self):
        nums = array('i', [0])
        self.assertAlmostEqual(zero_count(nums), 1.0, places=2)

    def test_single_non_zero(self):
        nums = array('i', [1])
        self.assertAlmostEqual(zero_count(nums), 0.0, places=2)

    def test_negative_numbers(self):
        nums = array('i', [-1, 0, -2, 0, -3])
        self.assertAlmostEqual(zero_count(nums), 0.4, places=2)
