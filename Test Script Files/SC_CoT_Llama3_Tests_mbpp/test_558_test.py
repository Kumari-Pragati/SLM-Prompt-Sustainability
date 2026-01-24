import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(digit_distance_nums(10, 20), 1)
        self.assertEqual(digit_distance_nums(50, 25), 2)
        self.assertEqual(digit_distance_nums(100, 50), 1)

    def test_edge_cases(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)
        self.assertEqual(digit_distance_nums(-10, 10), 1)
        self.assertEqual(digit_distance_nums(10, -10), 1)

    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-10, 10), 1)
        self.assertEqual(digit_distance_nums(-50, 25), 2)
        self.assertEqual(digit_distance_nums(-100, 50), 1)

    def test_zero(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)
        self.assertEqual(digit_distance_nums(0, 10), 1)
        self.assertEqual(digit_distance_nums(10, 0), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            digit_distance_nums('a', 10)
        with self.assertRaises(TypeError):
            digit_distance_nums(10, 'a')
