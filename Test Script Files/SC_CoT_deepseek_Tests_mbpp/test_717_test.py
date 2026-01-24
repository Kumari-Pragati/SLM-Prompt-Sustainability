import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)

    def test_single_element(self):
        self.assertEqual(avg_calc([1]), 1)

    def test_empty_list(self):
        self.assertEqual(avg_calc([]), 0.0)

    def test_float_elements(self):
        self.assertAlmostEqual(avg_calc([1.5, 2.5, 3.5]), 2.5)

    def test_negative_elements(self):
        self.assertAlmostEqual(avg_calc([-1, -2, -3, -4, -5]), -3.0)

    def test_large_numbers(self):
        self.assertAlmostEqual(avg_calc(list(range(1, 10001))), 5000.5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            avg_calc('1,2,3,4,5')

        with self.assertRaises(TypeError):
            avg_calc([1, '2', 3, 4, 5])

        with self.assertRaises(TypeError):
            avg_calc(123)
