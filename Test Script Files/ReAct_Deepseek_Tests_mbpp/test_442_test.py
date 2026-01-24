import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):

    def test_typical_case(self):
        nums = array('d', [1.0, 2.0, -3.0, 4.0, -5.0])
        self.assertAlmostEqual(positive_count(nums), 0.6, places=2)

    def test_all_positive(self):
        nums = array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertAlmostEqual(positive_count(nums), 1.0, places=2)

    def test_all_negative(self):
        nums = array('d', [-1.0, -2.0, -3.0, -4.0, -5.0])
        self.assertAlmostEqual(positive_count(nums), 0.0, places=2)

    def test_empty_array(self):
        nums = array('d', [])
        self.assertIsNone(positive_count(nums))

    def test_mixed_positive_negative(self):
        nums = array('d', [1.0, -2.0, 3.0, -4.0, 5.0])
        self.assertAlmostEqual(positive_count(nums), 0.6, places=2)

    def test_zero_in_array(self):
        nums = array('d', [0.0, 2.0, -3.0, 4.0, -5.0])
        self.assertAlmostEqual(positive_count(nums), 0.4, places=2)
