import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(num_comm_div(4, 16), 4)
        self.assertEqual(num_comm_div(20, 40), 4)
        self.assertEqual(num_comm_div(12, 36), 6)

    def test_edge_cases(self):
        self.assertEqual(num_comm_div(1, 1), 0)
        self.assertEqual(num_comm_div(2, 2), 0)
        self.assertEqual(num_comm_div(0, 0), 0)
        self.assertEqual(num_comm_div(1, 2), 1)
        self.assertEqual(num_comm_div(2, 1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(num_comm_div(123456789, 123456789), 1)
        self.assertEqual(num_comm_div(123456789, 123456788), 2)
        self.assertEqual(num_comm_div(123456789, 123456787), 2)

    def test_special_cases(self):
        self.assertEqual(num_comm_div(28, 496), 4)
        self.assertEqual(num_comm_div(1024, 1024), 0)
        self.assertEqual(num_comm_div(2**31 - 1, 2**31 - 1), 1)
