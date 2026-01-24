import unittest
from mbpp_555_code import difference

class TestDifferenceFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(difference(1), 0)
        self.assertEqual(difference(2), 1)
        self.assertEqual(difference(3), 3)
        self.assertEqual(difference(4), 6)
        self.assertEqual(difference(5), 10)

    def test_negative_numbers(self):
        with self.assertRaises(TypeError):
            difference(-1)
        with self.assertRaises(TypeError):
            difference(-2)

    def test_zero(self):
        self.assertEqual(difference(0), 0)

    def test_large_numbers(self):
        self.assertEqual(difference(100), 4950)
        self.assertEqual(difference(200), 20100)
