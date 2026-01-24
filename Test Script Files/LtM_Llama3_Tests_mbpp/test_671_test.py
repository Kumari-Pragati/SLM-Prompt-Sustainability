import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_single_set_bit(self):
        self.assertEqual(set_Right_most_Unset_Bit(1), 1)

    def test_multiple_set_bits(self):
        self.assertEqual(set_Right_most_Unset_Bit(3), 3)

    def test_edge_case_zero(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_one(self):
        self.assertEqual(set_Right_most_Unset_Bit(1), 1)

    def test_edge_case_power_of_two(self):
        self.assertEqual(set_Right_most_Unset_Bit(2), 2)

    def test_edge_case_power_of_two_plus_one(self):
        self.assertEqual(set_Right_most_Unset_Bit(3), 3)

    def test_edge_case_power_of_two_minus_one(self):
        self.assertEqual(set_Right_most_Unset_Bit(1), 1)

    def test_edge_case_power_of_two_minus_two(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_three(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_four(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_five(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_six(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_seven(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_eight(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_nine(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_ten(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_eleven(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_twelve(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_thirteen(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_fourteen(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_fifteen(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_sixteen(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_seventeen(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_eighteen(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_nineteen(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_twenty(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_twenty_one(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_twenty_two(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_twenty_three(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_twenty_four(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_twenty_five(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_twenty_six(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_twenty_seven(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_edge_case_power_of_two_minus_twenty_eight(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)