import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfWays(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(get_noOfways(3), 2)
        self.assertEqual(get_noOfways(4), 3)
        self.assertEqual(get_noOfways(5), 5)

    def test_edge_cases(self):
        self.assertEqual(get_noOfways(0), 0)
        self.assertEqual(get_noOfways(1), 1)
        self.assertEqual(get_noOfways(2), 1)

    def test_negative_input(self):
        self.assertRaises(ValueError, get_noOfways, -1)
        self.assertRaises(ValueError, get_noOfways, -2)
