import unittest
from mbpp_522_code import lbs

class TestLbs(unittest.TestCase):
    def test_single_element_array(self):
        self.assertEqual(lbs([1]), 1)

    def test_two_element_array(self):
        self.assertEqual(lbs([1, 2]), 2)

    def test_three_element_array(self):
        self.assertEqual(lbs([1, 2, 3]), 3)

    def test_decreasing_array(self):
        self.assertEqual(lbs([3, 2, 1]), 3)

    def test_increasing_array(self):
        self.assertEqual(lbs([1, 2, 3, 4, 5]), 5)

    def test_mixed_array(self):
        self.assertEqual(lbs([1, 3, 2, 4, 5]), 5)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            lbs([])

    def test_array_with_duplicates(self):
        self.assertEqual(lbs([1, 2, 2, 3, 3, 3]), 4)

    def test_array_with_negative_numbers(self):
        self.assertEqual(lbs([-1, -2, -3, -4, -5]), 5)
