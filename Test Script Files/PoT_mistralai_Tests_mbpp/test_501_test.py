import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(num_comm_div(4, 16), 4)
        self.assertEqual(num_comm_div(20, 40), 4)
        self.assertEqual(num_comm_div(12, 12), 1)
        self.assertEqual(num_comm_div(10, 25), 2)

    def test_edge_cases(self):
        self.assertEqual(num_comm_div(1, 1), 0)
        self.assertEqual(num_comm_div(0, 1), 0)
        self.assertEqual(num_comm_div(1, 0), 0)
        self.assertEqual(num_comm_div(-1, 1), 0)
        self.assertEqual(num_comm_div(1, -1), 0)

    def test_boundary_cases(self):
        self.assertEqual(num_comm_div(1, 2), 1)
        self.assertEqual(num_comm_div(2, 1), 1)
        self.assertEqual(num_comm_div(2, 2), 1)
