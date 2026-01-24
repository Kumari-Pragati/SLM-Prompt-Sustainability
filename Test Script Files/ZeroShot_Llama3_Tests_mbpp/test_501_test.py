import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_num_comm_div(self):
        self.assertEqual(num_comm_div(12, 15), 2)
        self.assertEqual(num_comm_div(24, 30), 4)
        self.assertEqual(num_comm_div(36, 48), 4)
        self.assertEqual(num_comm_div(10, 20), 2)
        self.assertEqual(num_comm_div(100, 200), 4)
        self.assertEqual(num_comm_div(1, 1), 0)
        self.assertEqual(num_comm_div(2, 3), 2)
        self.assertEqual(num_comm_div(4, 6), 2)
        self.assertEqual(num_comm_div(8, 12), 2)
        self.assertEqual(num_comm_div(9, 15), 2)
