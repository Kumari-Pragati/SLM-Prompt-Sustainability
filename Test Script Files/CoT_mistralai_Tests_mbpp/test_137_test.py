import unittest
from mbpp_137_code import array
from 137_code import zero_count

class TestZeroCount(unittest.TestCase):
    def test_zero_count_positive(self):
        self.assertAlmostEqual(zero_count(array('i', [0, 1, 0, 2, 0, 3])), 3/6, delta=0.01)

    def test_zero_count_negative(self):
        self.assertAlmostEqual(zero_count(array('i', [-1, -2, 0, -3])), 1/4, delta=0.01)

    def test_zero_count_empty(self):
        self.assertAlmostEqual(zero_count(array('i', [])), 0/0, delta=0.01)

    def test_zero_count_single_zero(self):
        self.assertAlmostEqual(zero_count(array('i', [0])), 1/1, delta=0.01)

    def test_zero_count_all_zeros(self):
        self.assertAlmostEqual(zero_count(array('i', [0, 0, 0])), 3/3, delta=0.01)

    def test_zero_count_all_non_zero(self):
        self.assertAlmostEqual(zero_count(array('i', [1, 2, 3])), 0/3, delta=0.01)

    def test_zero_count_invalid_input(self):
        with self.assertRaises(TypeError):
            zero_count('str')
