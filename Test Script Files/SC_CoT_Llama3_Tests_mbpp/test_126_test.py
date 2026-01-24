import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(sum(12, 15), 6)

    def test_edge_cases(self):
        self.assertEqual(sum(1, 1), 0)
        self.assertEqual(sum(2, 2), 0)
        self.assertEqual(sum(3, 3), 0)
        self.assertEqual(sum(4, 4), 2)
        self.assertEqual(sum(5, 5), 4)
        self.assertEqual(sum(6, 6), 6)

    def test_edge_cases_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            sum(0, 10)

    def test_edge_cases_with_negative(self):
        self.assertEqual(sum(-2, 3), 1)
        self.assertEqual(sum(-3, 3), 0)
        self.assertEqual(sum(-4, 4), 2)
        self.assertEqual(sum(-5, 5), 4)
        self.assertEqual(sum(-6, 6), 6)

    def test_edge_cases_with_zero_and_negative(self):
        with self.assertRaises(ZeroDivisionError):
            sum(0, -10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum("a", 10)
