import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(smallest_Divisor(1), 1)
        self.assertEqual(smallest_Divisor(2), 2)
        self.assertEqual(smallest_Divisor(3), 2)
        self.assertEqual(smallest_Divisor(4), 2)
        self.assertEqual(smallest_Divisor(5), 2)
        self.assertEqual(smallest_Divisor(6), 2)
        self.assertEqual(smallest_Divisor(7), 2)
        self.assertEqual(smallest_Divisor(8), 2)
        self.assertEqual(smallest_Divisor(9), 2)
        self.assertEqual(smallest_Divisor(10), 2)

    def test_edge_cases(self):
        self.assertEqual(smallest_Divisor(11), 2)
        self.assertEqual(smallest_Divisor(12), 2)
        self.assertEqual(smallest_Divisor(13), 2)
        self.assertEqual(smallest_Divisor(14), 2)
        self.assertEqual(smallest_Divisor(15), 2)
        self.assertEqual(smallest_Divisor(16), 2)
        self.assertEqual(smallest_Divisor(17), 2)
        self.assertEqual(smallest_Divisor(18), 2)
        self.assertEqual(smallest_Divisor(19), 2)
        self.assertEqual(smallest_Divisor(20), 2)

    def test_complex_cases(self):
        self.assertEqual(smallest_Divisor(21), 2)
        self.assertEqual(smallest_Divisor(22), 2)
        self.assertEqual(smallest_Divisor(23), 2)
        self.assertEqual(smallest_Divisor(24), 2)
        self.assertEqual(smallest_Divisor(25), 2)
        self.assertEqual(smallest_Divisor(26), 2)
        self.assertEqual(smallest_Divisor(27), 2)
        self.assertEqual(smallest_Divisor(28), 2)
        self.assertEqual(smallest_Divisor(29), 2)
        self.assertEqual(smallest_Divisor(30), 2)
