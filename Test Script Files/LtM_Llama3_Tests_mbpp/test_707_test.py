import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 2)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 3)
        self.assertEqual(count_Set_Bits(5), 3)
        self.assertEqual(count_Set_Bits(6), 4)

    def test_edge(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)
        self.assertEqual(count_Set_Bits(2**32), 32)

    def test_complex(self):
        self.assertEqual(count_Set_Bits(7), 3)
        self.assertEqual(count_Set_Bits(8), 4)
        self.assertEqual(count_Set_Bits(9), 4)
        self.assertEqual(count_Set_Bits(10), 5)
        self.assertEqual(count_Set_Bits(11), 5)
        self.assertEqual(count_Set_Bits(12), 6)
