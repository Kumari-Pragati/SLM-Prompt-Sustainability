import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(difference(1), 0)
        self.assertEqual(difference(2), 1)
        self.assertEqual(difference(5), 12)
        self.assertEqual(difference(10), 90)

    def test_zero(self):
        self.assertEqual(difference(0), 0)

    def test_negative_integer(self):
        self.assertEqual(difference(-1), 0)
        self.assertEqual(difference(-2), 2)
        self.assertEqual(difference(-5), 20)
        self.assertEqual(difference(-10), 90)

    def test_edge_cases(self):
        self.assertEqual(difference(1000000), 499999500000)
        self.assertEqual(difference(-1000000), -499999500000)

    def test_invalid_input(self):
        self.assertRaises(TypeError, difference, 'not_an_integer')
        self.assertRaises(TypeError, difference, 3.14)
