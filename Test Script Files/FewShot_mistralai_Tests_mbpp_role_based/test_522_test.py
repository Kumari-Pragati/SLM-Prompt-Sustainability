import unittest
from mbpp_522_code import lbs

class TestLbs(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(lbs([1, 2, 3, 4]), 5)

    def test_empty_list(self):
        self.assertEqual(lbs([]), 0)

    def test_single_element_list(self):
        self.assertEqual(lbs([1]), 1)

    def test_decreasing_list(self):
        self.assertEqual(lbs([4, 3, 2, 1]), 3)

    def test_increasing_list(self):
        self.assertEqual(lbs([1, 2, 3, 4]), 5)

    def test_alternating_list(self):
        self.assertEqual(lbs([1, 2, 3, 4, 5]), 6)

    def test_negative_numbers(self):
        self.assertEqual(lbs([-1, -2, -3, -4]), 3)

    def test_duplicate_numbers(self):
        self.assertEqual(lbs([1, 1, 2, 3]), 5)
