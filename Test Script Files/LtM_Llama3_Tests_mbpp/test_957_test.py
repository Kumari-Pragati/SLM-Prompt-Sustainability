import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2), 2)
        self.assertEqual(get_First_Set_Bit_Pos(3), 2)
        self.assertEqual(get_First_Set_Bit_Pos(4), 2)
        self.assertEqual(get_First_Set_Bit_Pos(5), 2)
        self.assertEqual(get_First_Set_Bit_Pos(6), 3)
        self.assertEqual(get_First_Set_Bit_Pos(7), 3)
        self.assertEqual(get_First_Set_Bit_Pos(8), 3)
        self.assertEqual(get_First_Set_Bit_Pos(9), 3)
        self.assertEqual(get_First_Set_Bit_Pos(10), 3)
        self.assertEqual(get_First_Set_Bit_Pos(11), 3)
        self.assertEqual(get_First_Set_Bit_Pos(12), 3)
        self.assertEqual(get_First_Set_Bit_Pos(13), 3)
        self.assertEqual(get_First_Set_Bit_Pos(14), 3)
        self.assertEqual(get_First_Set_Bit_Pos(15), 3)
        self.assertEqual(get_First_Set_Bit_Pos(16), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 0)
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2**31-1), 31)
        self.assertEqual(get_First_Set_Bit_Pos(2**32-1), 32)
        self.assertEqual(get_First_Set_Bit_Pos(-1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(-2), 2)
        self.assertEqual(get_First_Set_Bit_Pos(-3), 2)
        self.assertEqual(get_First_Set_Bit_Pos(-4), 2)
        self.assertEqual(get_First_Set_Bit_Pos(-5), 2)
        self.assertEqual(get_First_Set_Bit_Pos(-6), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-7), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-8), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-9), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-10), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-11), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-12), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-13), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-14), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-15), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-16), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos(None)
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos("hello")
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos({"a": 1})
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos([1, 2, 3])
