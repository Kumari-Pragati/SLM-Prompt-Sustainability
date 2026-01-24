import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_Digit(123), 3)
        self.assertEqual(count_Digit(456), 3)
        self.assertEqual(count_Digit(789), 3)

    def test_edge_cases(self):
        self.assertEqual(count_Digit(0), 1)
        self.assertEqual(count_Digit(10), 1)
        self.assertEqual(count_Digit(100), 3)

    def test_boundary_cases(self):
        self.assertEqual(count_Digit(99), 2)
        self.assertEqual(count_Digit(999), 3)
        self.assertEqual(count_Digit(9999), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Digit('abc')
        with self.assertRaises(TypeError):
            count_Digit(None)
