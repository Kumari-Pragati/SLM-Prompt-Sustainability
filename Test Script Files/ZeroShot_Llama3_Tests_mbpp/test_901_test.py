import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_smallest_multiple(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 60)
        self.assertEqual(smallest_multiple(6), 12)
        self.assertEqual(smallest_multiple(7), 84)
        self.assertEqual(smallest_multiple(8), 24)
        self.assertEqual(smallest_multiple(9), 18)
        self.assertEqual(smallest_multiple(10), 60)
        self.assertEqual(smallest_multiple(11), 132)
        self.assertEqual(smallest_multiple(12), 12)
        self.assertEqual(smallest_multiple(13), 546)
        self.assertEqual(smallest_multiple(14), 84)
        self.assertEqual(smallest_multiple(15), 60)
        self.assertEqual(smallest_multiple(16), 48)
        self.assertEqual(smallest_multiple(17), 2040)
        self.assertEqual(smallest_multiple(18), 36)
        self.assertEqual(smallest_multiple(19), 6840)
        self.assertEqual(smallest_multiple(20), 60)

    def test_edge_cases(self):
        self.assertRaises(ValueError, smallest_multiple, 0)
