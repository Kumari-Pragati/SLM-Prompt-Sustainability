import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(num_comm_div(4, 2), 2)
        self.assertEqual(num_comm_div(8, 4), 2)
        self.assertEqual(num_comm_div(12, 6), 2)
        self.assertEqual(num_comm_div(18, 6), 4)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(num_comm_div(0, 0), 0)
        self.assertEqual(num_comm_div(-4, 2), 2)
        self.assertEqual(num_comm_div(-4, -2), 0)
        self.assertEqual(num_comm_div(-4, 0), 0)

    def test_one(self):
        self.assertEqual(num_comm_div(1, 1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            num_comm_div('a', 'b')
        with self.assertRaises(TypeError):
            num_comm_div(1.5, 2)
