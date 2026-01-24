import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(closest_num(10), 9)
        self.assertEqual(closest_num(20), 19)
        self.assertEqual(closest_num(30), 29)

    def test_negative_numbers(self):
        self.assertEqual(closest_num(-10), -11)
        self.assertEqual(closest_num(-20), -21)
        self.assertEqual(closest_num(-30), -31)

    def test_zero(self):
        self.assertEqual(closest_num(0), -1)

    def test_boundary_conditions(self):
        self.assertEqual(closest_num(1), 0)
        self.assertEqual(closest_num(-1), -2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            closest_num('10')
        with self.assertRaises(TypeError):
            closest_num(None)
