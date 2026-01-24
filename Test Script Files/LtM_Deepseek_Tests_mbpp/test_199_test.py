import unittest
from mbpp_199_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(highest_Power_of_2(10), 8)
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(31), 16)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(32), 32)

    # Test for more complex or corner cases
    def test_corner_cases(self):
        self.assertEqual(highest_Power_of_2(2147483647), 2147483648)
        self.assertEqual(highest_Power_of_2(-1), 0)
