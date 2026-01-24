import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_smallest_multiple_typical_cases(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 60)
        self.assertEqual(smallest_multiple(6), 60)
        self.assertEqual(smallest_multiple(7), 420)
        self.assertEqual(smallest_multiple(8), 840)
        self.assertEqual(smallest_multiple(9), 2520)
        self.assertEqual(smallest_multiple(10), 2520)

    def test_smallest_multiple_edge_cases(self):
        self.assertEqual(smallest_multiple(0), 0)
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)

    def test_smallest_multiple_error_cases(self):
        with self.assertRaises(TypeError):
            smallest_multiple('a')
        with self.assertRaises(ValueError):
            smallest_multiple(-1)
