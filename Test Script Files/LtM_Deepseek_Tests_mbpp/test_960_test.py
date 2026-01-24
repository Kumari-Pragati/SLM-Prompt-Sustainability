import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfways(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_noOfways(0), 0)
        self.assertEqual(get_noOfways(1), 1)

    def test_edge_conditions(self):
        self.assertEqual(get_noOfways(-1), get_noOfways(-1))
        self.assertEqual(get_noOfways(2), get_noOfways(1) + get_noOfways(0))

    def test_complex_cases(self):
        self.assertEqual(get_noOfways(3), get_noOfways(2) + get_noOfways(1))
        self.assertEqual(get_noOfways(4), get_noOfways(3) + get_noOfways(2))
