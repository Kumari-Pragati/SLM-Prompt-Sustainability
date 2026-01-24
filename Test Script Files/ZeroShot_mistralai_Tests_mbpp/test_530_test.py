import unittest
from mbpp_530_code import array
from 530_code import negative_count

class TestNegativeCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertAlmostEqual(negative_count([]), 0.00)

    def test_all_positive(self):
        self.assertAlmostEqual(negative_count(array('i', [1, 2, 3, 4, 5])), 0.00)

    def test_all_negative(self):
        self.assertAlmostEqual(negative_count(array('i', [-1, -2, -3, -4, -5])), 1.00)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(negative_count(array('i', [-1, 0, 1, -2, 3])), 2/5, delta=0.01)
