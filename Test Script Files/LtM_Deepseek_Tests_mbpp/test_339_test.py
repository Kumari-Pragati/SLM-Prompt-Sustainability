import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Divisor(10, 10), 10)
        self.assertEqual(find_Divisor(15, 15), 15)

    def test_edge_conditions(self):
        self.assertEqual(find_Divisor(0, 0), 0)
        self.assertEqual(find_Divisor(0, 10), 2)
        self.assertEqual(find_Divisor(10, 0), 2)

    def test_complex_cases(self):
        self.assertEqual(find_Divisor(10, 20), 2)
        self.assertEqual(find_Divisor(-10, -20), 2)
        self.assertEqual(find_Divisor(-10, 20), 2)
        self.assertEqual(find_Divisor(20, -10), 2)
