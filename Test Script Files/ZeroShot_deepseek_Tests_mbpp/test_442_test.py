import unittest
from mbpp_442_code import array
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_positive_count(self):
        # Test with a list of positive numbers
        self.assertAlmostEqual(positive_count([1, 2, 3, 4, 5]), 1.0)

        # Test with a list of negative numbers
        self.assertAlmostEqual(positive_count([-1, -2, -3, -4, -5]), 0.0)

        # Test with a mix of positive and negative numbers
        self.assertAlmostEqual(positive_count([-1, 2, -3, 4, -5]), 0.2)

        # Test with an empty list
        self.assertAlmostEqual(positive_count([]), 0.0)

        # Test with a list of one positive number
        self.assertAlmostEqual(positive_count([1]), 1.0)

        # Test with a list of one negative number
        self.assertAlmostEqual(positive_count([-1]), 0.0)

        # Test with a list of zeros and positive numbers
        self.assertAlmostEqual(positive_count([0, 1, 2, 3, 4]), 0.4)

        # Test with a list of zeros and negative numbers
        self.assertAlmostEqual(positive_count([0, -1, -2, -3, -4]), 0.0)

        # Test with a list of zeros and mixed positive and negative numbers
        self.assertAlmostEqual(positive_count([0, -1, 2, -3, 4]), 0.2)
