import unittest
from mbpp_522_code import lbs

class TestLbs(unittest.TestCase):

    def test_lbs_positive_numbers(self):
        self.assertEqual(lbs([10, 22, 9, 33, 21, 50, 41, 60, 80]), 5)
        self.assertEqual(lbs([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
        self.assertEqual(lbs([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 1)

    def test_lbs_negative_numbers(self):
        self.assertEqual(lbs([-10, -22, -9, -33, -21, -50, -41, -60, -80]), 1)
        self.assertEqual(lbs([-1, -2, -3, -4, -5, -6, -7, -8, -9]), 1)
        self.assertEqual(lbs([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]), 1)

    def test_lbs_mixed_numbers(self):
        self.assertEqual(lbs([10, -22, 9, -33, 21, -50, 41, -60, 80]), 5)
        self.assertEqual(lbs([1, -2, 3, -4, 5, -6, 7, -8, 9]), 9)
        self.assertEqual(lbs([10, -9, 8, -7, 6, -5, 4, -3, 2, -1]), 1)

    def test_lbs_empty_list(self):
        self.assertEqual(lbs([]), 0)

    def test_lbs_single_element(self):
        self.assertEqual(lbs([1]), 1)
