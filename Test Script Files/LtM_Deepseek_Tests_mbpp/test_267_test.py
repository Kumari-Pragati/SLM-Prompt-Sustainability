import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 14)
        self.assertEqual(square_Sum(3), 44)

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(100), 833668)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(square_Sum(1000), 333833500)
        self.assertEqual(square_Sum(500), 8333350)
