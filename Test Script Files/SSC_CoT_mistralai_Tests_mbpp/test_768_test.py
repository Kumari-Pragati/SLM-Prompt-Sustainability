import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertTrue(check_Odd_Parity(1))
        self.assertTrue(check_Odd_Parity(3))
        self.assertTrue(check_Odd_Parity(5))
        self.assertFalse(check_Odd_Parity(0))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(check_Odd_Parity(-1))
        self.assertTrue(check_Odd_Parity(2 ** 31 - 1))  # max int
        self.assertFalse(check_Odd_Parity(2 ** 31))  # max int + 1
        self.assertFalse(check_Odd_Parity(-2 ** 31))  # min int

    def test_special_cases(self):
        self.assertTrue(check_Odd_Parity(1 << 63))  # largest odd number
        self.assertFalse(check_Odd_Parity(1 << 64))  # not a number
