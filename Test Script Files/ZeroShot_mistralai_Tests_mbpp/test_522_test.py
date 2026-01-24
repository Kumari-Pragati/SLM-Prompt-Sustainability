import unittest
from mbpp_522_code import lbs

class TestLbsFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(lbs([]), 0)

    def test_single_element_list(self):
        self.assertEqual(lbs([1]), 1)

    def test_increasing_list(self):
        self.assertEqual(lbs([1, 2, 3, 4]), 4)

    def test_decreasing_list(self):
        self.assertEqual(lbs([4, 3, 2, 1]), 4)

    def test_mixed_list(self):
        self.assertEqual(lbs([1, 5, 2, 3, 4]), 5)

    def test_negative_list(self):
        self.assertEqual(lbs([-1, -2, -3, -4]), 4)

    def test_duplicates_increasing_list(self):
        self.assertEqual(lbs([1, 1, 2, 3, 4]), 4)

    def test_duplicates_decreasing_list(self):
        self.assertEqual(lbs([4, 4, 3, 2, 1]), 4)
