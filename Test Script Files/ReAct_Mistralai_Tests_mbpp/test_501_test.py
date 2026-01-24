import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(num_comm_div(4, 16), 2)
        self.assertEqual(num_comm_div(20, 40), 2)
        self.assertEqual(num_comm_div(9, 36), 2)
        self.assertEqual(num_comm_div(18, 18), 0)
        self.assertEqual(num_comm_div(25, 125), 2)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(num_comm_div(0, 0), 0)
        self.assertEqual(num_comm_div(0, 5), 0)
        self.assertEqual(num_comm_div(-5, 0), None)
        self.assertEqual(num_comm_div(-5, -5), 0)
        self.assertEqual(num_comm_div(-5, 5), 0)

    def test_one_argument(self):
        self.assertEqual(num_comm_div(1), None)

    def test_large_numbers(self):
        self.assertEqual(num_comm_div(1000000, 2000000), 2)
        self.assertEqual(num_comm_div(2000000, 1000000), 2)
