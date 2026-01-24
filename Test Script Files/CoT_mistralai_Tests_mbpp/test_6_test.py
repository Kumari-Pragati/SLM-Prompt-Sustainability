import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):

    def test_differ_at_one_bit_pos_powers_of_two(self):
        self.assertEqual(differ_At_One_Bit_Pos(2, 4), True)
        self.assertEqual(differ_At_One_Bit_Pos(1, 3), True)
        self.assertEqual(differ_At_One_Bit_Pos(8, 16), True)
        self.assertEqual(differ_At_One_Bit_Pos(1, 2), False)
        self.assertEqual(differ_At_One_Bit_Pos(0, 1), False)

    def test_differ_at_one_bit_pos_non_powers_of_two(self):
        self.assertEqual(differ_At_One_Bit_Pos(5, 7), True)
        self.assertEqual(differ_At_One_Bit_Pos(13, 15), True)
        self.assertEqual(differ_At_One_Bit_Pos(25, 27), True)
        self.assertEqual(differ_At_One_Bit_Pos(10, 11), True)
        self.assertEqual(differ_At_One_Bit_Pos(100, 101), True)

    def test_differ_at_one_bit_pos_same_numbers(self):
        self.assertEqual(differ_At_One_Bit_Pos(2, 2), False)
        self.assertEqual(differ_At_One_Bit_Pos(10, 10), False)
        self.assertEqual(differ_At_One_Bit_Pos(100, 100), False)

    def test_differ_at_one_bit_pos_invalid_inputs(self):
        self.assertRaises(TypeError, differ_At_One_Bit_Pos, 'a', 1)
        self.assertRaises(TypeError, differ_At_One_Bit_Pos, 1, 'b')
        self.assertRaises(TypeError, differ_At_One_Bit_Pos, 'a', 'b')
        self.assertRaises(TypeError, differ_At_One_Bit_Pos, 0, 0)
