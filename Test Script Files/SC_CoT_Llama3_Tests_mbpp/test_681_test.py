import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(smallest_Divisor(10), 2)
        self.assertEqual(smallest_Divisor(12), 2)
        self.assertEqual(smallest_Divisor(15), 3)
        self.assertEqual(smallest_Divisor(20), 2)
        self.assertEqual(smallest_Divisor(25), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(smallest_Divisor(1), 1)
        self.assertEqual(smallest_Divisor(2), 2)
        self.assertEqual(smallest_Divisor(3), 2)
        self.assertEqual(smallest_Divisor(4), 2)
        self.assertEqual(smallest_Divisor(9), 3)

    def test_special_and_corner_cases(self):
        self.assertEqual(smallest_Divisor(6), 2)
        self.assertEqual(smallest_Divisor(8), 2)
        self.assertEqual(smallest_Divisor(11), 2)
        self.assertEqual(smallest_Divisor(16), 2)
        self.assertEqual(smallest_Divisor(21), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            smallest_Divisor(None)
        with self.assertRaises(TypeError):
            smallest_Divisor("hello")
