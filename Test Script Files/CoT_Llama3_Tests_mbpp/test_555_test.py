import unittest
from mbpp_555_code import difference

class TestDifferenceFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(difference(3), 6)

    def test_negative_numbers(self):
        with self.assertRaises(TypeError):
            difference(-1)

    def test_zero(self):
        self.assertEqual(difference(0), 0)

    def test_large_numbers(self):
        self.assertEqual(difference(100), 49995000)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            difference(3.5)

    def test_edge_case(self):
        self.assertEqual(difference(1), 0)
