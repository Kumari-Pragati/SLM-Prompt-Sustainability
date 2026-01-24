import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(last_Digit(123), 3)
        self.assertEqual(last_Digit(456), 6)
        self.assertEqual(last_Digit(789), 9)

    def test_edge_cases(self):
        self.assertEqual(last_Digit(0), 0)
        self.assertEqual(last_Digit(-123), 3)

    def test_boundary_cases(self):
        self.assertEqual(last_Digit(10), 0)
        self.assertEqual(last_Digit(-10), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            last_Digit('123')
        with self.assertRaises(TypeError):
            last_Digit(None)
