import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(min_Operations(4, 16), 3)
        self.assertEqual(min_Operations(8, 24), 6)
        self.assertEqual(min_Operations(1, 2), 0)

    def test_zero(self):
        self.assertEqual(min_Operations(0, 0), -1)

    def test_negative_numbers(self):
        self.assertEqual(min_Operations(-4, -16), 3)
        self.assertEqual(min_Operations(-8, -24), 6)
        self.assertEqual(min_Operations(-1, -2), 0)

    def test_gcd_edge_case(self):
        self.assertEqual(min_Operations(12, 18), 1)
        self.assertEqual(min_Operations(20, 10), 1)
        self.assertEqual(min_Operations(30, 20), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Operations('a', 'b')
        with self.assertRaises(TypeError):
            min_Operations([1, 2, 3], [4, 5, 6])
