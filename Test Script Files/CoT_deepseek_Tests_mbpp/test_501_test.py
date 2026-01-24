import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(num_comm_div(10, 20), 6)

    def test_typical_case_2(self):
        self.assertEqual(num_comm_div(30, 45), 9)

    def test_edge_case_1(self):
        self.assertEqual(num_comm_div(1, 1), 2)

    def test_edge_case_2(self):
        self.assertEqual(num_comm_div(0, 0), 0)

    def test_edge_case_3(self):
        self.assertEqual(num_comm_div(0, 10), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            num_comm_div("10", 20)
