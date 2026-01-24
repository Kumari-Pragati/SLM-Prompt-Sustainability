import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):
    def test_minimum_equal_values(self):
        self.assertEqual(minimum(3, 3), 3)

    def test_minimum_positive_numbers(self):
        self.assertEqual(minimum(5, 2), 2)
        self.assertEqual(minimum(10, 7), 7)

    def test_minimum_negative_numbers(self):
        self.assertEqual(minimum(-5, -2), -5)
        self.assertEqual(minimum(-10, -7), -10)

    def test_minimum_zero_and_positive(self):
        self.assertEqual(minimum(0, 5), 0)

    def test_minimum_zero_and_negative(self):
        self.assertEqual(minimum(0, -5), 0)

    def test_minimum_mixed_signs(self):
        self.assertEqual(minimum(2, -3), 2)
        self.assertEqual(minimum(-2, 3), -2)

    def test_minimum_large_numbers(self):
        self.assertEqual(minimum(1000000000, 999999999), 999999999)
        self.assertEqual(minimum(999999999, 1000000000), 999999999)

    def test_minimum_floats(self):
        self.assertAlmostEqual(minimum(3.14, 2.71), 2.71)
        self.assertAlmostEqual(minimum(2.71, 3.14), 2.71)

    def test_minimum_invalid_inputs(self):
        self.assertRaises(TypeError, minimum, 'a', 'b')
        self.assertRaises(TypeError, minimum, 1, 'b')
        self.assertRaises(TypeError, minimum, 'a', 1)
