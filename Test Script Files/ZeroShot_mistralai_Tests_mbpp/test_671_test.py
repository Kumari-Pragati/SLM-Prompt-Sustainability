import unittest
from mbpp_671_code import set_Right_most_Unset_Bit, get_Pos_Of_Right_most_Set_Bit

class TestSetRightMostUnsetBit(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_one(self):
        self.assertEqual(set_Right_most_Unset_Bit(1), 2)

    def test_powers_of_two(self):
        for i in range(1, 32):
            self.assertEqual(set_Right_most_Unset_Bit(1 << i), 1 << (i - 1) | 1 << i)

    def test_negative_numbers(self):
        self.assertEqual(set_Right_most_Unset_Bit(-1), -2)

    def test_large_numbers(self):
        self.assertEqual(set_Right_most_Unset_Bit(2 ** 31 - 1), 2 ** 31 - 2)

    def test_edge_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(math.inf), math.inf)
        self.assertEqual(set_Right_most_Unset_Bit(-math.inf), -math.inf)
