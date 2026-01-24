import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        self.assertEqual(sum_of_square(3), 14)
        self.assertEqual(sum_of_square(4), 42)

    def test_edge_cases(self):
        self.assertEqual(sum_of_square(0), 1)
        self.assertEqual(sum_of_square(-1), 1)
        self.assertEqual(sum_of_square(10), 9707252334407561)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            sum_of_square('a')
        with self.assertRaises(TypeError):
            sum_of_square(None)
