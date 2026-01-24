import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_count_Set_Bits(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 1)
        self.assertEqual(count_Set_Bits(5), 2)
        self.assertEqual(count_Set_Bits(6), 2)
        self.assertEqual(count_Set_Bits(7), 3)
        self.assertEqual(count_Set_Bits(8), 1)
        self.assertEqual(count_Set_Bits(9), 2)
        self.assertEqual(count_Set_Bits(10), 2)
        self.assertEqual(count_Set_Bits(11), 3)
        self.assertEqual(count_Set_Bits(12), 2)
        self.assertEqual(count_Set_Bits(13), 3)
        self.assertEqual(count_Set_Bits(14), 3)
        self.assertEqual(count_Set_Bits(15), 4)
        self.assertEqual(count_Set_Bits(16), 1)
