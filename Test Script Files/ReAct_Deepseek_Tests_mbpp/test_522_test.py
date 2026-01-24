import unittest
from mbpp_522_code import lbs

class TestLbs(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lbs([0, 8, 4, 12, 2, 10, 6, 14, 1, 9]), 7)

    def test_empty_array(self):
        self.assertEqual(lbs([]), 0)

    def test_single_element(self):
        self.assertEqual(lbs([5]), 1)

    def test_sorted_array(self):
        self.assertEqual(lbs([1, 2, 3, 4, 5]), 5)

    def test_reverse_sorted_array(self):
        self.assertEqual(lbs([5, 4, 3, 2, 1]), 5)

    def test_duplicate_elements(self):
        self.assertEqual(lbs([1, 2, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(lbs([-5, -3, -1, 0, 2]), 3)

    def test_large_numbers(self):
        self.assertEqual(lbs([10**6, 2*10**6, 3*10**6, 4*10**6, 5*10**6]), 5)

    def test_large_array(self):
        self.assertEqual(lbs(list(range(1, 1001))), 999)
