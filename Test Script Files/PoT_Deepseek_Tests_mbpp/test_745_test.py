import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 12, 14, 15, 18, 20])
        self.assertEqual(divisible_by_digits(100, 200), [100, 102, 105, 110, 111, 112, 114, 115, 118, 120, 126, 132, 140, 142, 144, 150, 153, 154, 160, 162, 170, 171, 175, 176, 180, 182, 183, 184, 186, 187, 188, 190, 195, 198, 200])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(divisible_by_digits(0, 0), [0])
        self.assertEqual(divisible_by_digits(1, 1), [])
        self.assertEqual(divisible_by_digits(10, 9), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            divisible_by_digits("10", 20)
        with self.assertRaises(TypeError):
            divisible_by_digits(10, "20")
        with self.assertRaises(TypeError):
            divisible_by_digits("10", "20")
        with self.assertRaises(ValueError):
            divisible_by_digits(10, -20)
