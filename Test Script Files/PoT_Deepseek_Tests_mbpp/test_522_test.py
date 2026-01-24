import unittest
from mbpp_522_code import lbs

class TestLBS(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lbs([0, 8, 4, 12, 2, 10, 6, 14, 1, 9]), 7)

    def test_single_element(self):
        self.assertEqual(lbs([5]), 1)

    def test_empty_list(self):
        self.assertEqual(lbs([]), 0)

    def test_decreasing_sequence(self):
        self.assertEqual(lbs([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 1)

    def test_increasing_sequence(self):
        self.assertEqual(lbs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

    def test_all_same_elements(self):
        self.assertEqual(lbs([5, 5, 5, 5, 5]), 1)

    def test_negative_numbers(self):
        self.assertEqual(lbs([-7, 0, 5, -2, 8, -1, 9]), 4)

    def test_large_numbers(self):
        self.assertEqual(lbs([1000, 2000, 1500, 2500, 3000]), 4)

    def test_large_sequence(self):
        self.assertEqual(lbs(list(range(1, 1001))), 1000)
