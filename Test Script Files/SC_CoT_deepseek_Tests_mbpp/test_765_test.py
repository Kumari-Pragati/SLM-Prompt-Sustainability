import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(is_polite(1), 3)
        self.assertEqual(is_polite(10), 12)
        self.assertEqual(is_polite(100), 103)

    def test_edge_cases(self):
        self.assertEqual(is_polite(0), 2)
        self.assertEqual(is_polite(1), 3)

    def test_corner_cases(self):
        self.assertEqual(is_polite(math.pow(2, 31) - 1), math.pow(2, 31))
        self.assertEqual(is_polite(math.pow(2, 31)), math.pow(2, 32))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_polite(-1)
        with self.assertRaises(TypeError):
            is_polite('a')
        with self.assertRaises(TypeError):
            is_polite(None)
        with self.assertRaises(TypeError):
            is_polite(math.nan)
        with self.assertRaises(TypeError):
            is_polite(math.inf)
        with self.assertRaises(TypeError):
            is_polite(-math.inf)
