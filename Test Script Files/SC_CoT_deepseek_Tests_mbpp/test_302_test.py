import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(set_Bit_Number(0), 0)
        self.assertEqual(set_Bit_Number(1), 1)
        self.assertEqual(set_Bit_Number(2), 2)
        self.assertEqual(set_Bit_Number(4), 4)
        self.assertEqual(set_Bit_Number(8), 8)

    def test_edge_cases(self):
        self.assertEqual(set_Bit_Number(1024), 512)
        self.assertEqual(set_Bit_Number(2048), 1024)

    def test_boundary_cases(self):
        self.assertEqual(set_Bit_Number(1025), 2048)
        self.assertEqual(set_Bit_Number(2049), 4096)

    def test_special_cases(self):
        self.assertEqual(set_Bit_Number(32), 16)
        self.assertEqual(set_Bit_Number(64), 32)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            set_Bit_Number("string")
        with self.assertRaises(TypeError):
            set_Bit_Number(None)
        with self.assertRaises(TypeError):
            set_Bit_Number([1, 2, 3])
