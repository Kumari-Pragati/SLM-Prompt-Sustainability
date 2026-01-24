import unittest
from mbpp_522_code import lbs

class TestLbs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lbs([1, 5, 3, 4, 2]), 5)
        self.assertEqual(lbs([10, 22, 9, 33, 21, 50, 41, 11]), 62)

    def test_edge_case_single_element(self):
        self.assertEqual(lbs([1]), 1)
        self.assertEqual(lbs([10]), 10)

    def test_edge_case_two_elements(self):
        self.assertEqual(lbs([1, 2]), 2)
        self.assertEqual(lbs([10, 9]), 10)

    def test_edge_case_decreasing(self):
        self.assertEqual(lbs([5, 4, 3, 2, 1]), 5)
        self.assertEqual(lbs([10, 9, 8, 7, 6]), 16)

    def test_edge_case_increasing(self):
        self.assertEqual(lbs([1, 2, 3, 4, 5]), 5)
        self.assertEqual(lbs([1, 2, 3, 4, 5, 6]), 6)

    def test_edge_case_duplicates(self):
        self.assertEqual(lbs([1, 1, 2, 3, 4]), 5)
        self.assertEqual(lbs([10, 10, 9, 8, 7]), 16)

    def test_corner_case_empty(self):
        self.assertEqual(lbs([]), 0)
