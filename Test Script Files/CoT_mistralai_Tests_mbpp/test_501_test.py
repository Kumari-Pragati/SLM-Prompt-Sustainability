import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(num_comm_div(4, 16), 2)
        self.assertEqual(num_comm_div(8, 24), 2)
        self.assertEqual(num_comm_div(9, 36), 2)
        self.assertEqual(num_comm_div(10, 25), 2)
        self.assertEqual(num_comm_div(15, 50), 2)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(num_comm_div(0, 0), 0)
        self.assertEqual(num_comm_div(0, 4), 0)
        self.assertEqual(num_comm_div(-4, 0), 0)
        self.assertEqual(num_comm_div(-4, -4), 0)
        self.assertEqual(num_comm_div(-4, 4), 0)

    def test_one_argument(self):
        self.assertEqual(num_comm_div(1), 0)

    def test_large_numbers(self):
        self.assertEqual(num_comm_div(1000000, 2000000), 2)
        self.assertEqual(num_comm_div(2000000, 1000000), 2)
