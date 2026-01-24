import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_equal_A_B(self):
        self.assertEqual(compute_Last_Digit(1, 1), 1)

    def test_B_A_greater_than_5(self):
        self.assertEqual(compute_Last_Digit(10, 15), 0)

    def test_B_A_less_than_5(self):
        self.assertEqual(compute_Last_Digit(1, 5), 5)

    def test_B_A_greater_than_5_with_loop(self):
        self.assertEqual(compute_Last_Digit(1, 10), 1)

    def test_B_A_less_than_5_with_loop(self):
        self.assertEqual(compute_Last_Digit(1, 6), 1)

    def test_B_A_equal_to_5(self):
        self.assertEqual(compute_Last_Digit(5, 5), 1)
