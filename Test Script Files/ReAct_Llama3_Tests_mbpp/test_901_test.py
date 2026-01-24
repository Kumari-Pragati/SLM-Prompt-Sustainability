import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):
    def test_smallest_multiple_for_small_numbers(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 60)

    def test_smallest_multiple_for_larger_numbers(self):
        self.assertEqual(smallest_multiple(6), 12)
        self.assertEqual(smallest_multiple(7), 84)
        self.assertEqual(smallest_multiple(8), 24)
        self.assertEqual(smallest_multiple(9), 18)
        self.assertEqual(smallest_multiple(10), 2520)

    def test_smallest_multiple_for_edge_cases(self):
        self.assertEqual(smallest_multiple(11), 4620)
        self.assertEqual(smallest_multiple(12), 1320)
        self.assertEqual(smallest_multiple(13), 5460)
        self.assertEqual(smallest_multiple(14), 10920)
        self.assertEqual(smallest_multiple(15), 360360)

    def test_smallest_multiple_for_explicitly_handled_error_cases(self):
        self.assertEqual(smallest_multiple(16), 122880)
