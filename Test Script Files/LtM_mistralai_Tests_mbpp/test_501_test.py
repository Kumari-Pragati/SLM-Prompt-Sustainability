import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(num_comm_div(4, 2), 2)
        self.assertEqual(num_comm_div(8, 4), 2)
        self.assertEqual(num_comm_div(12, 6), 2)

    def test_edge_cases(self):
        self.assertEqual(num_comm_div(1, 1), 0)
        self.assertEqual(num_comm_div(2, 1), 1)
        self.assertEqual(num_comm_div(0, 0), 0)
        self.assertEqual(num_comm_div(1, 2), 1)
        self.assertEqual(num_comm_div(2, 3), 1)

    def test_boundary(self):
        self.assertEqual(num_comm_div(2**31, 1), 2**30)
        self.assertEqual(num_comm_div(1, 2**31), 1)

    def test_complex(self):
        self.assertEqual(num_comm_div(1000000000, 1000000001), 1)
        self.assertEqual(num_comm_div(1000000001, 1000000000), 1)
        self.assertEqual(num_comm_div(1000000000, 1000000002), 2)
        self.assertEqual(num_comm_div(1000000002, 1000000000), 2)
