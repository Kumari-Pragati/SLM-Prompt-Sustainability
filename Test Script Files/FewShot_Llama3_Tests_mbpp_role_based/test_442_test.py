import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(positive_count([]), 0.0)

    def test_single_positive(self):
        self.assertEqual(positive_count([1]), 1.0)

    def test_single_negative(self):
        self.assertEqual(positive_count([-1]), 0.0)

    def test_multiple_positive(self):
        self.assertEqual(positive_count([1, 2, 3]), 1.0)

    def test_multiple_negative(self):
        self.assertEqual(positive_count([-1, -2, -3]), 0.0)

    def test_mixed_positive_negative(self):
        self.assertEqual(positive_count([1, -2, 3, -4]), 0.5)

    def test_large_list(self):
        self.assertEqual(positive_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.0)
