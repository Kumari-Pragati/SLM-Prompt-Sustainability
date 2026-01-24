import unittest
from mbpp_137_code import array
from thirteen_seven import zero_count

class TestZeroCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(zero_count(array('i', [])), 0.0)

    def test_all_zeros(self):
        self.assertEqual(zero_count(array('i', [0, 0, 0])), 1.0)

    def test_single_zero(self):
        self.assertAlmostEqual(zero_count(array('i', [1, 0, 1])), 0.33)

    def test_multiple_zeros(self):
        self.assertAlmostEqual(zero_count(array('i', [1, 0, 1, 0, 1, 0])), 0.5)

    def test_negative_numbers(self):
        self.assertAlmostEqual(zero_count(array('i', [-1, 0, 1])), 0.33)

    def test_floats(self):
        self.assertAlmostEqual(zero_count(array('d', [0.0, 1.0, 0.0])), 0.5)
