import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(closest_num(5), 4)
        self.assertEqual(closest_num(10), 9)
        self.assertEqual(closest_num(15), 14)

    def test_edge_cases(self):
        self.assertEqual(closest_num(1), 0)
        self.assertEqual(closest_num(2), 1)

    def test_negative_inputs(self):
        self.assertEqual(closest_num(-5), -6)
        self.assertEqual(closest_num(-10), -11)

    def test_zero_input(self):
        self.assertEqual(closest_num(0), -1)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            closest_num("test")
