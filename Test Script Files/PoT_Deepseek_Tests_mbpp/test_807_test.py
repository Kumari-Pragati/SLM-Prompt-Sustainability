import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_odd([2, 4, 6]), -1)
        self.assertEqual(first_odd([1, 2, 3, 4, 5]), 1)
        self.assertEqual(first_odd([10, 20, 30]), -1)

    def test_edge_cases(self):
        self.assertEqual(first_odd([]), -1)
        self.assertEqual(first_odd([2]), -1)
        self.assertEqual(first_odd([2, 4, 6, 8, 10]), -1)

    def test_corner_cases(self):
        self.assertEqual(first_odd([1]), 1)
        self.assertEqual(first_odd([2, 1]), 1)
        self.assertEqual(first_odd([2, 4, 1]), 1)
