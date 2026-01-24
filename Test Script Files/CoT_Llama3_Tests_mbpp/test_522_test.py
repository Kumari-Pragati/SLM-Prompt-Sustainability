import unittest
from mbpp_522_code import lbs

class TestLbs(unittest.TestCase):
    def test_lbs_empty_array(self):
        self.assertEqual(lbs([]), 0)

    def test_lbs_single_element_array(self):
        self.assertEqual(lbs([1]), 1)

    def test_lbs_two_element_array(self):
        self.assertEqual(lbs([1, 2]), 2)

    def test_lbs_increasing_array(self):
        self.assertEqual(lbs([1, 2, 3, 4, 5]), 5)

    def test_lbs_decreasing_array(self):
        self.assertEqual(lbs([5, 4, 3, 2, 1]), 5)

    def test_lbs_mixed_array(self):
        self.assertEqual(lbs([1, 3, 2, 4, 5]), 5)

    def test_lbs_repeated_elements_array(self):
        self.assertEqual(lbs([1, 2, 2, 3, 3, 3, 4, 5]), 5)

    def test_lbs_negative_elements_array(self):
        self.assertEqual(lbs([-1, -2, -3, -4, -5]), 5)

    def test_lbs_large_array(self):
        self.assertEqual(lbs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
