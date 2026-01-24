import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_input(self):
        self.assertEqual(sum_difference(5), 110)

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(0), 0)

    # Test for more complex or corner cases
    def test_large_input(self):
        self.assertGreater(sum_difference(100), 0)
