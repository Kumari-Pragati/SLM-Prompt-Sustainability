import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(difference(3), 2)

    def test_zero(self):
        with self.assertRaises(TypeError):
            difference(0)

    def test_negative_numbers(self):
        with self.assertRaises(TypeError):
            difference(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            difference(3.5)

    def test_edge_case(self):
        self.assertEqual(difference(1), 0)

    def test_large_numbers(self):
        self.assertEqual(difference(100), 4950)
