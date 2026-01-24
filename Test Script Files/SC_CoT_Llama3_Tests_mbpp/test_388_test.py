import unittest
from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(32), 32)
        self.assertEqual(highest_Power_of_2(64), 64)

    def test_edge_cases(self):
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)

    def test_higher_values(self):
        self.assertEqual(highest_Power_of_2(128), 128)
        self.assertEqual(highest_Power_of_2(256), 256)
        self.assertEqual(highest_Power_of_2(512), 512)

    def test_low_values(self):
        self.assertEqual(highest_Power_of_2(3), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(5), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            highest_Power_of_2('a')
        with self.assertRaises(TypeError):
            highest_Power_of_2(None)
        with self.assertRaises(TypeError):
            highest_Power_of_2(1.5)
