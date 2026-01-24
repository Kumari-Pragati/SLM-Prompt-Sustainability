import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(num_comm_div(12, 15), 2)
        self.assertEqual(num_comm_div(24, 30), 2)
        self.assertEqual(num_comm_div(36, 48), 2)

    def test_edge_cases(self):
        self.assertEqual(num_comm_div(1, 1), 2)
        self.assertEqual(num_comm_div(2, 3), 2)
        self.assertEqual(num_comm_div(4, 4), 2)

    def test_zero_divisor(self):
        self.assertEqual(num_comm_div(12, 0), 0)
        self.assertEqual(num_comm_div(0, 15), 0)
        self.assertEqual(num_comm_div(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(num_comm_div(-12, 15), 2)
        self.assertEqual(num_comm_div(12, -15), 2)
        self.assertEqual(num_comm_div(-12, -15), 2)

    def test_non_integer_divisors(self):
        self.assertEqual(num_comm_div(12, 15.5), 2)
        self.assertEqual(num_comm_div(24, 30.5), 2)
        self.assertEqual(num_comm_div(36, 48.5), 2)
