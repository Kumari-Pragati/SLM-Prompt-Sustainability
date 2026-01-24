import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):
    def test_num_comm_div(self):
        self.assertEqual(num_comm_div(21, 7), 4)
        self.assertEqual(num_comm_div(10, 15), 2)
        self.assertEqual(num_comm_div(36, 48), 6)
        self.assertEqual(num_comm_div(1, 1), 2)
        self.assertEqual(num_comm_div(0, 0), 1)
        self.assertEqual(num_comm_div(100, 200), 6)
