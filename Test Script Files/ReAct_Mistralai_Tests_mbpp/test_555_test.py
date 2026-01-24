import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(difference(5), 24)
        self.assertEqual(difference(10), 90)
        self.assertEqual(difference(20), 380)

    def test_zero(self):
        self.assertEqual(difference(0), 0)

    def test_negative_integer(self):
        self.assertEqual(difference(-1), -1)
        self.assertEqual(difference(-5), 10)
        self.assertEqual(difference(-20), -780)

    def test_large_positive_integer(self):
        self.assertEqual(difference(100000), 5000050000)

    def test_large_negative_integer(self):
        self.assertEqual(difference(-100000), -5000050000)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            difference(3.14)
