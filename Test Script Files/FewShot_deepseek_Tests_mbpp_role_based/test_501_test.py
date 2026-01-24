import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(num_comm_div(10, 20), 6)

    def test_boundary_conditions(self):
        self.assertEqual(num_comm_div(1, 1), 2)
        self.assertEqual(num_comm_div(0, 0), 1)

    def test_edge_cases(self):
        self.assertEqual(num_comm_div(100, 100), 3)
        self.assertEqual(num_comm_div(1000, 1000), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            num_comm_div("10", 20)
        with self.assertRaises(TypeError):
            num_comm_div(10, "20")
        with self.assertRaises(TypeError):
            num_comm_div("10", "20")
