import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(multiply_int(2, 3), 6)
        self.assertEqual(multiply_int(5, 4), 20)
        self.assertEqual(multiply_int(-3, 4), -12)

    def test_edge_cases(self):
        self.assertEqual(multiply_int(0, 100), 0)
        self.assertEqual(multiply_int(-5, 0), 0)
        self.assertEqual(multiply_int(1, 1), 1)

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(multiply_int(3, -1), -3)
        self.assertEqual(multiply_int(-2, -3), 6)
