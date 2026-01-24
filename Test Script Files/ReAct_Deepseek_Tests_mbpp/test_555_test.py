import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(difference(1), 1)
        self.assertEqual(difference(2), 6)
        self.assertEqual(difference(3), 20)
        self.assertEqual(difference(4), 42)

    def test_edge_cases(self):
        self.assertEqual(difference(0), 0)
        self.assertEqual(difference(-1), 0)

    def test_large_numbers(self):
        self.assertEqual(difference(10), 10*11*12//6)
        self.assertEqual(difference(100), 100*101*102//6)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            difference('a')
        with self.assertRaises(TypeError):
            difference(None)
