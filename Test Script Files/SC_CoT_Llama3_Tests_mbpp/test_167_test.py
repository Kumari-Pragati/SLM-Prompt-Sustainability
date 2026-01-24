import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):

    def test_power_of_2(self):
        self.assertEqual(next_Power_Of_2(8), 8)

    def test_next_power_of_2(self):
        self.assertEqual(next_Power_Of_2(7), 8)

    def test_zero(self):
        self.assertEqual(next_Power_Of_2(0), 1)

    def test_one(self):
        self.assertEqual(next_Power_Of_2(1), 1)

    def test_negative(self):
        with self.assertRaises(TypeError):
            next_Power_Of_2(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            next_Power_Of_2(3.5)

    def test_large_number(self):
        self.assertEqual(next_Power_Of_2(1024), 2048)

    def test_max_int(self):
        self.assertEqual(next_Power_Of_2(2147483647), 2147483648)

    def test_max_int_plus_one(self):
        self.assertEqual(next_Power_Of_2(2147483648), 4294967296)

    def test_max_int_plus_two(self):
        self.assertEqual(next_Power_Of_2(4294967295), 4294967296)

    def test_max_int_plus_three(self):
        self.assertEqual(next_Power_Of_2(4294967296), 4294967296)
