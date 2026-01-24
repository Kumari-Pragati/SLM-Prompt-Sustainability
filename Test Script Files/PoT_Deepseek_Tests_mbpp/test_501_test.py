import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(num_comm_div(10, 20), 6)
        self.assertEqual(num_comm_div(30, 45), 9)
        self.assertEqual(num_comm_div(100, 200), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(num_comm_div(0, 20), 2)
        self.assertEqual(num_comm_div(20, 0), 2)
        self.assertEqual(num_comm_div(0, 0), 1)
        self.assertEqual(num_comm_div(1, 1), 1)

    def test_corner_cases(self):
        self.assertEqual(num_comm_div(1, 2), 1)
        self.assertEqual(num_comm_div(2, 1), 1)
        self.assertEqual(num_comm_div(10, 25), 3)
        self.assertEqual(num_comm_div(25, 10), 3)
