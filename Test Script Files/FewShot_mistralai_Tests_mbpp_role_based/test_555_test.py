import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(difference(5), 24)

    def test_zero(self):
        self.assertEqual(difference(0), 0)

    def test_negative_integer(self):
        self.assertEqual(difference(-5), 24)

    def test_large_integer(self):
        self.assertEqual(difference(100), 5050)

    def test_floating_point(self):
        with self.assertRaises(TypeError):
            difference(3.14)
