import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):

    # Test for simple / typical inputs
    def test_simple_inputs(self):
        self.assertEqual(smallest_Divisor(7), 7)
        self.assertEqual(smallest_Divisor(10), 2)
        self.assertEqual(smallest_Divisor(13), 13)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(smallest_Divisor(2), 2)
        self.assertEqual(smallest_Divisor(1), 1)
        self.assertEqual(smallest_Divisor(0), 0)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(smallest_Divisor(35), 5)
        self.assertEqual(smallest_Divisor(97), 97)
        self.assertEqual(smallest_Divisor(100), 2)
