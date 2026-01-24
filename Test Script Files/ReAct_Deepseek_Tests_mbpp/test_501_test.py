import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(num_comm_div(10, 20), 6)
        self.assertEqual(num_comm_div(30, 45), 9)
        self.assertEqual(num_comm_div(100, 100), 11)

    def test_edge_cases(self):
        self.assertEqual(num_comm_div(0, 20), 2)
        self.assertEqual(num_comm_div(20, 0), 2)
        self.assertEqual(num_comm_div(0, 0), 1)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            num_comm_div("10", 20)
        with self.assertRaises(TypeError):
            num_comm_div(10, "20")
        with self.assertRaises(TypeError):
            num_comm_div("10", "20")
