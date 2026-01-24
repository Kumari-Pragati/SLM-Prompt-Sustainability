import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(even_Power_Sum(1), 16)
        self.assertEqual(even_Power_Sum(2), 16*16 + 32*32*32*32)
        self.assertEqual(even_Power_Sum(3), 16*16 + 32*32*32*32 + 48*48*48*48)

    def test_boundary_cases(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(10), 160*160 + 176*176*176*176 + 192*192*192*192 + 208*208*208*208 + 224*224*224*224 + 240*240*240*240 + 256*256*256*256 + 272*272*272*272 + 288*288*288*288 + 304*304*304*304)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')
        with self.assertRaises(ValueError):
            even_Power_Sum(-1)
