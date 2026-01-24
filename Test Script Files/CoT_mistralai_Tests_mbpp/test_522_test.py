import unittest
from mbpp_522_code import lbs

class TestLbsFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(lbs([]), 0)

    def test_single_element_list(self):
        self.assertEqual(lbs([1]), 1)

    def test_increasing_list(self):
        self.assertEqual(lbs([1, 2, 3, 4]), 3)

    def test_decreasing_list(self):
        self.assertEqual(lbs([4, 3, 2, 1]), 3)

    def test_duplicate_elements(self):
        self.assertEqual(lbs([1, 1, 2, 2, 3, 3]), 4)

    def test_alternating_list(self):
        self.assertEqual(lbs([1, 2, 1, 2, 1, 2]), 3)

    def test_negative_numbers(self):
        self.assertEqual(lbs([-1, -2, -3]), 2)

    def test_mixed_numbers(self):
        self.assertEqual(lbs([1, -2, 3, -4, 5]), 4)

    def test_invalid_input(self):
        self.assertRaises(TypeError, lbs, "string")
