import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(num_comm_div(12, 15), 2)
        self.assertEqual(num_comm_div(24, 30), 2)
        self.assertEqual(num_comm_div(36, 48), 2)
        self.assertEqual(num_comm_div(50, 75), 2)
        self.assertEqual(num_comm_div(100, 200), 2)

    def test_edge(self):
        self.assertEqual(num_comm_div(1, 1), 2)
        self.assertEqual(num_comm_div(2, 3), 2)
        self.assertEqual(num_comm_div(4, 6), 2)
        self.assertEqual(num_comm_div(8, 8), 2)
        self.assertEqual(num_comm_div(10, 20), 2)

    def test_divisor(self):
        self.assertEqual(num_comm_div(12, 12), 2)
        self.assertEqual(num_comm_div(24, 24), 2)
        self.assertEqual(num_comm_div(36, 36), 2)
        self.assertEqual(num_comm_div(50, 50), 2)
        self.assertEqual(num_comm_div(100, 100), 2)

    def test_zero(self):
        self.assertEqual(num_comm_div(0, 0), 2)
        self.assertEqual(num_comm_div(0, 1), 1)
        self.assertEqual(num_comm_div(1, 0), 0)
        self.assertEqual(num_comm_div(0, 2), 0)

    def test_negative(self):
        self.assertEqual(num_comm_div(-12, -15), 2)
        self.assertEqual(num_comm_div(-24, -30), 2)
        self.assertEqual(num_comm_div(-36, -48), 2)
        self.assertEqual(num_comm_div(-50, -75), 2)
        self.assertEqual(num_comm_div(-100, -200), 2)
