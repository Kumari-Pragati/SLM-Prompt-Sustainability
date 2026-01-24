import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(4), 3)
        self.assertEqual(Sum(5), 5)
        self.assertEqual(Sum(6), 6)
        self.assertEqual(Sum(7), 7)
        self.assertEqual(Sum(8), 7)
        self.assertEqual(Sum(9), 9)
        self.assertEqual(Sum(10), 8)

    def test_edge_cases(self):
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(0), 0)
        self.assertEqual(Sum(-1), 0)
        self.assertEqual(Sum(100), 100)
        self.assertEqual(Sum(200), 200)

    def test_explicitly_handled_error_cases(self):
        # Since the function does not handle any error cases, this test is empty
        pass
