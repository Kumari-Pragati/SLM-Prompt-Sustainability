import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(smallest_Divisor(7), 7)
        self.assertEqual(smallest_Divisor(10), 2)
        self.assertEqual(smallest_Divisor(13), 13)
        self.assertEqual(smallest_Divisor(15), 3)

    def test_edge_cases(self):
        self.assertEqual(smallest_Divisor(2), 2)
        self.assertEqual(smallest_Divisor(1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(smallest_Divisor(0), 0)
        self.assertEqual(smallest_Divisor(-1), -1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            smallest_Divisor("string")
        with self.assertRaises(TypeError):
            smallest_Divisor(None)
