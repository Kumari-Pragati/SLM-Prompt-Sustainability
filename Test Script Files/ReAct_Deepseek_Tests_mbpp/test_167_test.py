import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(next_Power_Of_2(16), 16)
        self.assertEqual(next_Power_Of_2(32), 32)
        self.assertEqual(next_Power_Of_2(64), 64)
        self.assertEqual(next_Power_Of_2(128), 128)
        self.assertEqual(next_Power_Of_2(256), 256)

    def test_edge_cases(self):
        self.assertEqual(next_Power_Of_2(0), 1)
        self.assertEqual(next_Power_Of_2(1), 2)
        self.assertEqual(next_Power_Of_2(2), 4)
        self.assertEqual(next_Power_Of_2(3), 4)
        self.assertEqual(next_Power_Of_2(4), 4)
        self.assertEqual(next_Power_Of_2(5), 8)
        self.assertEqual(next_Power_Of_2(7), 8)
        self.assertEqual(next_Power_Of_2(8), 8)
        self.assertEqual(next_Power_Of_2(9), 16)
        self.assertEqual(next_Power_Of_2(15), 16)
        self.assertEqual(next_Power_Of_2(17), 32)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            next_Power_Of_2('16')
        with self.assertRaises(TypeError):
            next_Power_Of_2(None)
        with self.assertRaises(TypeError):
            next_Power_Of_2([])
        with self.assertRaises(TypeError):
            next_Power_Of_2({})
