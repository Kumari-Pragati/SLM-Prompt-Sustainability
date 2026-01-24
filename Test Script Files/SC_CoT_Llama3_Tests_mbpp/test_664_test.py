import unittest
from mbpp_664_code import average_Even

class TestAverageEven(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(average_Even(10), 5)

    def test_edge_case_zero(self):
        self.assertEqual(average_Even(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(average_Even(1), -1)

    def test_edge_case_even(self):
        self.assertEqual(average_Even(4), 2)

    def test_edge_case_odd(self):
        self.assertEqual(average_Even(5), -1)

    def test_edge_case_large(self):
        self.assertEqual(average_Even(100), 50)

    def test_edge_case_negative(self):
        with self.assertRaises(ZeroDivisionError):
            average_Even(-10)

    def test_invalid_input(self):
        self.assertEqual(average_Even(3), -1)
