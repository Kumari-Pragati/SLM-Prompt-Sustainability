import unittest
from mbpp_555_code import difference

class TestDifferenceFunction(unittest.TestCase):

    def test_difference_function(self):
        self.assertEqual(difference(1), 0)
        self.assertEqual(difference(2), 0)
        self.assertEqual(difference(3), 2)
        self.assertEqual(difference(4), 6)
        self.assertEqual(difference(5), 10)
        self.assertEqual(difference(6), 15)
        self.assertEqual(difference(7), 21)
        self.assertEqual(difference(8), 28)
        self.assertEqual(difference(9), 36)
        self.assertEqual(difference(10), 45)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            difference(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            difference(1.5)
