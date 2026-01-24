import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(num_comm_div(12, 15), 2)
        self.assertEqual(num_comm_div(24, 30), 2)
        self.assertEqual(num_comm_div(36, 48), 2)

    def test_edge_cases(self):
        self.assertEqual(num_comm_div(1, 1), 2)
        self.assertEqual(num_comm_div(2, 3), 2)
        self.assertEqual(num_comm_div(3, 4), 2)

    def test_special_cases(self):
        self.assertEqual(num_comm_div(12, 12), 2)
        self.assertEqual(num_comm_div(24, 24), 2)
        self.assertEqual(num_comm_div(36, 36), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            num_comm_div('a', 2)
        with self.assertRaises(TypeError):
            num_comm_div(2, 'b')
