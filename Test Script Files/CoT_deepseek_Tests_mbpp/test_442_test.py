import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(positive_count([1, -2, 3, -4, 5]), 0.6, places=2)

    def test_empty_list(self):
        self.assertEqual(positive_count([]), 0)

    def test_all_positive(self):
        self.assertEqual(positive_count([1, 2, 3]), 1)

    def test_all_negative(self):
        self.assertEqual(positive_count([-1, -2, -3]), 0)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(positive_count([-1, 2, -3, 4]), 0.5, places=2)

    def test_large_numbers(self):
        self.assertAlmostEqual(positive_count([1000, -2000, 3000]), 0.33, places=2)

    def test_zero(self):
        self.assertEqual(positive_count([0]), 0)

    def test_single_positive(self):
        self.assertEqual(positive_count([5]), 1)

    def test_single_negative(self):
        self.assertEqual(positive_count([-5]), 0)

    def test_array_input(self):
        self.assertAlmostEqual(positive_count(array('i', [1, -2, 3, -4, 5])), 0.6, places=2)
