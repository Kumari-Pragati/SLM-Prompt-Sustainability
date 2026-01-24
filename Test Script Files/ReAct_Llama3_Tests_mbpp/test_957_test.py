import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):

    def test_get_first_set_bit_pos_positive(self):
        self.assertEqual(get_First_Set_Bit_Pos(7), 3)

    def test_get_first_set_bit_pos_negative(self):
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos(-1)

    def test_get_first_set_bit_pos_zero(self):
        with self.assertRaises(ZeroDivisionError):
            get_First_Set_Bit_Pos(0)

    def test_get_first_set_bit_pos_power_of_two(self):
        self.assertEqual(get_First_Set_Bit_Pos(8), 3)

    def test_get_first_set_bit_pos_power_of_two_minus_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(7), 3)

    def test_get_first_set_bit_pos_power_of_two_plus_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(9), 3)

    def test_get_first_set_bit_pos_power_of_two_plus_two(self):
        self.assertEqual(get_First_Set_Bit_Pos(16), 4)

    def test_get_first_set_bit_pos_power_of_two_plus_three(self):
        self.assertEqual(get_First_Set_Bit_Pos(32), 5)

    def test_get_first_set_bit_pos_power_of_two_plus_four(self):
        self.assertEqual(get_First_Set_Bit_Pos(64), 6)

    def test_get_first_set_bit_pos_power_of_two_plus_five(self):
        self.assertEqual(get_First_Set_Bit_Pos(128), 7)

    def test_get_first_set_bit_pos_power_of_two_plus_six(self):
        self.assertEqual(get_First_Set_Bit_Pos(256), 8)

    def test_get_first_set_bit_pos_power_of_two_plus_seven(self):
        self.assertEqual(get_First_Set_Bit_Pos(512), 9)

    def test_get_first_set_bit_pos_power_of_two_plus_eight(self):
        self.assertEqual(get_First_Set_Bit_Pos(1024), 10)

    def test_get_first_set_bit_pos_power_of_two_plus_nine(self):
        self.assertEqual(get_First_Set_Bit_Pos(2048), 11)

    def test_get_first_set_bit_pos_power_of_two_plus_ten(self):
        self.assertEqual(get_First_Set_Bit_Pos(4096), 12)

    def test_get_first_set_bit_pos_power_of_two_plus_eleven(self):
        self.assertEqual(get_First_Set_Bit_Pos(8192), 13)

    def test_get_first_set_bit_pos_power_of_two_plus_twelve(self):
        self.assertEqual(get_First_Set_Bit_Pos(16384), 14)

    def test_get_first_set_bit_pos_power_of_two_plus_thirteen(self):
        self.assertEqual(get_First_Set_Bit_Pos(32768), 15)

    def test_get_first_set_bit_pos_power_of_two_plus_fourteen(self):
        self.assertEqual(get_First_Set_Bit_Pos(65536), 16)

    def test_get_first_set_bit_pos_power_of_two_plus_fifteen(self):
        self.assertEqual(get_First_Set_Bit_Pos(131072), 17)

    def test_get_first_set_bit_pos_power_of_two_plus_sixteen(self):
        self.assertEqual(get_First_Set_Bit_Pos(262144), 18)

    def test_get_first_set_bit_pos_power_of_two_plus_seventeen(self):
        self.assertEqual(get_First_Set_Bit_Pos(524288), 19)

    def test_get_first_set_bit_pos_power_of_two_plus_eighteen(self):
        self.assertEqual(get_First_Set_Bit_Pos(1048576), 20)

    def test_get_first_set_bit_pos_power_of_two_plus_nineteen(self):
        self.assertEqual(get_First_Set_Bit_Pos(2097152), 21)

    def test_get_first_set_bit_pos_power_of_two_plus_twenty(self):
        self.assertEqual(get_First_Set_Bit_Pos(4194304), 22)

    def test_get_first_set_bit_pos_power_of_two_plus_twenty_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(8388608), 23)

    def test_get_first_set_bit_pos_power_of_two_plus_twenty_two(self):
        self.assertEqual(get_First_Set_Bit_Pos(16777216), 24)

    def test_get_first_set_bit_pos_power_of_two_plus_twenty_three(self):
        self.assertEqual(get_First_Set_Bit_Pos(33554432), 25)

    def test_get_first_set_bit_pos_power_of_two_plus_twenty_four(self):
        self.assertEqual(get_First_Set_Bit_Pos(67108864), 26)

    def test_get_first_set_bit_pos_power_of_two_plus_twenty_five(self):
        self.assertEqual(get_First_Set_Bit_Pos(134217728), 27)

    def test_get_first_set_bit_pos_power_of_two_plus_twenty_six(self):
        self.assertEqual(get_First_Set_Bit_Pos(268435456), 28)

    def test_get_first_set_bit_pos_power_of_two_plus_twenty_se