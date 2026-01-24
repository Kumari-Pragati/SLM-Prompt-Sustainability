import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(cube_Sum(1), 1)
        self.assertEqual(cube_Sum(2), 9 + 27)
        self.assertEqual(cube_Sum(3), 9 + 27 + 125)

    def test_edge_cases(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(-1), 0)
        self.assertEqual(cube_Sum(10), sum((2*i+1)**3 for i in range(10)))

    def test_explicitly_handled_error_cases(self):
        # Since the function does not handle any error cases, this test is just to ensure it doesn't crash
        self.assertIsNone(cube_Sum('a'))
        self.assertIsNone(cube_Sum(None))
