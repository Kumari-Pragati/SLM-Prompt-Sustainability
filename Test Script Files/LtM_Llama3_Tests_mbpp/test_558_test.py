import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(digit_distance_nums(10, 20), 1)
        self.assertEqual(digit_distance_nums(-10, 20), 1)
        self.assertEqual(digit_distance_nums(10, -20), 1)
        self.assertEqual(digit_distance_nums(10, 10), 0)
        self.assertEqual(digit_distance_nums(-10, -10), 0)

    def test_edge_cases(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)
        self.assertEqual(digit_distance_nums(0, 1), 1)
        self.assertEqual(digit_distance_nums(1, 0), 1)
        self.assertEqual(digit_distance_nums(-1, 1), 2)
        self.assertEqual(digit_distance_nums(1, -1), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            digit_distance_nums('a', 10)
        with self.assertRaises(TypeError):
            digit_distance_nums(10, 'a')
        with self.assertRaises(TypeError):
            digit_distance_nums('a', 'b')
