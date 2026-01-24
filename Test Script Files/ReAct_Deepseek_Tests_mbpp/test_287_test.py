import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 9)
        self.assertEqual(square_Sum(3), 36)
        self.assertEqual(square_Sum(4), 100)

    def test_edge_cases(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(-1), 0)
        self.assertEqual(square_Sum(100), 328350)

    def test_explicitly_handled_error_cases(self):
        # Since the function does not handle any error cases, 
        # we can assume that it will raise a TypeError if a non-integer is passed.
        with self.assertRaises(TypeError):
            square_Sum("1")
