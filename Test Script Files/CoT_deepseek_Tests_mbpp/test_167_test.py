import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(next_Power_Of_2(1), 2)
        self.assertEqual(next_Power_Of_2(2), 4)
        self.assertEqual(next_Power_Of_2(8), 8)
        self.assertEqual(next_Power_Of_2(16), 16)
        self.assertEqual(next_Power_Of_2(32), 32)
        self.assertEqual(next_Power_Of_2(64), 64)
        self.assertEqual(next_Power_Of_2(128), 128)

    def test_edge_cases(self):
        self.assertEqual(next_Power_Of_2(0), 1)
        self.assertEqual(next_Power_Of_2(1024), 1024)
        self.assertEqual(next_Power_Of_2(2048), 2048)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            next_Power_Of_2("10")
        with self.assertRaises(TypeError):
            next_Power_Of_2(None)
        with self.assertRaises(TypeError):
            next_Power_Of_2([])
        with self.assertRaises(TypeError):
            next_Power_Of_2({})
