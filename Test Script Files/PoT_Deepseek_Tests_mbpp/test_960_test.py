import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfways(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_noOfways(0), 0)
        self.assertEqual(get_noOfways(1), 1)
        self.assertEqual(get_noOfways(2), 2)
        self.assertEqual(get_noOfways(3), 3)
        self.assertEqual(get_noOfways(4), 5)

    def test_edge_cases(self):
        self.assertEqual(get_noOfways(-1), 0)
        self.assertEqual(get_noOfways(20), 6765)  # This is the 20th number in the Fibonacci sequence

    def test_corner_cases(self):
        self.assertEqual(get_noOfways(100), 354224848179261915075)  # This is the 100th number in the Fibonacci sequence
