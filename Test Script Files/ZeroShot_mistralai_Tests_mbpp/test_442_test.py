import unittest
from mbpp_442_code import array
from 442_code import positive_count

class TestPositiveCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(positive_count(array('i', [])), 0.0)

    def test_all_positive(self):
        self.assertEqual(positive_count(array('i', [1, 2, 3, 4, 5])), 1.0)

    def test_all_negative(self):
        self.assertEqual(positive_count(array('i', [-1, -2, -3, -4, -5])), 0.0)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(positive_count(array('i', [1, -2, 3, -4, 5])), 0.6, delta=0.01)
