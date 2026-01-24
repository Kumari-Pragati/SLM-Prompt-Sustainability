import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfWays(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_noOfways(0), 0)
        self.assertEqual(get_noOfways(1), 1)
        self.assertEqual(get_noOfways(2), 2)
        self.assertEqual(get_noOfways(3), 3)
        self.assertEqual(get_noOfways(4), 5)
        self.assertEqual(get_noOfways(5), 8)
        self.assertEqual(get_noOfways(6), 13)
        self.assertEqual(get_noOfways(7), 21)
        self.assertEqual(get_noOfways(8), 34)
        self.assertEqual(get_noOfways(9), 55)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(get_noOfways(-1), None)
        self.assertEqual(get_noOfways(10), 89)
        self.assertEqual(get_noOfways(20), 1447)
        self.assertEqual(get_noOfways(30), 27777)
        self.assertEqual(get_noOfways(40), 48622)
        self.assertEqual(get_noOfways(50), 832040)
