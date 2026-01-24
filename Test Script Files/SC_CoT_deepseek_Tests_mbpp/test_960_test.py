import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfways(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_noOfways(2), 2)
        self.assertEqual(get_noOfways(3), 3)
        self.assertEqual(get_noOfways(4), 5)

    def test_boundary_conditions(self):
        self.assertEqual(get_noOfways(0), 0)
        self.assertEqual(get_noOfways(1), 1)

    def test_edge_cases(self):
        self.assertEqual(get_noOfways(20), 6765)

    def test_invalid_inputs(self):
        with self.assertRaises(RecursionError):
            get_noOfways(-1)
        with self.assertRaises(RecursionError):
            get_noOfways(21)
