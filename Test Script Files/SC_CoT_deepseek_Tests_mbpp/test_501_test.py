import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(num_comm_div(10, 20), 6)
        self.assertEqual(num_comm_div(36, 60), 6)

    def test_edge_cases(self):
        self.assertEqual(num_comm_div(1, 1), 2)
        self.assertEqual(num_comm_div(0, 0), 0)

    def test_corner_cases(self):
        self.assertEqual(num_comm_div(100, 100), 1)
        self.assertEqual(num_comm_div(1000, 1000), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            num_comm_div("10", 20)
        with self.assertRaises(TypeError):
            num_comm_div(10, "20")
        with self.assertRaises(TypeError):
            num_comm_div("10", "20")
