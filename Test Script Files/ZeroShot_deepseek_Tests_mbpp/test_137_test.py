import unittest
from mbpp_137_code import array
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):

    def test_zero_count(self):
        nums = array('i', [0, 1, 0, 3, 0])
        self.assertEqual(zero_count(nums), 0.6)

    def test_zero_count_all_zeros(self):
        nums = array('i', [0, 0, 0, 0, 0])
        self.assertEqual(zero_count(nums), 1.0)

    def test_zero_count_all_ones(self):
        nums = array('i', [1, 1, 1, 1, 1])
        self.assertEqual(zero_count(nums), 0.0)

    def test_zero_count_empty_array(self):
        nums = array('i', [])
        self.assertIsNone(zero_count(nums))
