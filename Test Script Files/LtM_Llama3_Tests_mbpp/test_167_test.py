import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(next_Power_Of_2(1), 1)
        self.assertEqual(next_Power_Of_2(2), 2)
        self.assertEqual(next_Power_Of_2(4), 4)
        self.assertEqual(next_Power_Of_2(8), 8)
        self.assertEqual(next_Power_Of_2(16), 16)

    def test_edge_cases(self):
        self.assertEqual(next_Power_Of_2(0), 1)
        self.assertEqual(next_Power_Of_2(3), 4)
        self.assertEqual(next_Power_Of_2(5), 8)
        self.assertEqual(next_Power_Of_2(15), 16)
        self.assertEqual(next_Power_Of_2(31), 32)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            next_Power_Of_2(None)
        with self.assertRaises(TypeError):
            next_Power_Of_2("hello")
