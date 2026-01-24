import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_Min_Sum(6), 2)
        self.assertEqual(find_Min_Sum(12), 3)
        self.assertEqual(find_Min_Sum(24), 8)

    def test_edge_input(self):
        self.assertEqual(find_Min_Sum(1), 1)
        self.assertEqual(find_Min_Sum(2), 2)
        self.assertEqual(find_Min_Sum(3), 3)
        self.assertEqual(find_Min_Sum(4), 2)
        self.assertEqual(find_Min_Sum(5), 1)

    def test_boundary_input(self):
        self.assertEqual(find_Min_Sum(10**5), 10**5)
        self.assertEqual(find_Min_Sum(10**6), 10**6)
        self.assertEqual(find_Min_Sum(10**7), 10**7)

    def test_complex_input(self):
        self.assertEqual(find_Min_Sum(10), 2)
        self.assertEqual(find_Min_Sum(15), 2)
        self.assertEqual(find_Min_Sum(20), 4)
        self.assertEqual(find_Min_Sum(28), 6)
        self.assertEqual(find_Min_Sum(42), 6)
