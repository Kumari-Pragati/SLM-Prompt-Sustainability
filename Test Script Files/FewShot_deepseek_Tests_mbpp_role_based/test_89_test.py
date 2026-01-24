import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(closest_num(10), 9)

    def test_boundary_condition(self):
        self.assertEqual(closest_num(0), -1)

    def test_negative_number(self):
        self.assertEqual(closest_num(-5), -6)

    def test_large_number(self):
        self.assertEqual(closest_num(1000000), 999999)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            closest_num('a')
