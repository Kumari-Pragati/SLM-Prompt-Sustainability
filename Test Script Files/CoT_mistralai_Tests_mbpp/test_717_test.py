import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(avg_calc([]), 0.0)

    def test_single_element_list(self):
        self.assertEqual(avg_calc([1]), 1.0)

    def test_multiple_elements_list(self):
        self.assertAlmostEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(avg_calc([1, -2, 3, -4, 5]), 1.0)

    def test_floats(self):
        self.assertAlmostEqual(avg_calc([1.1, 2.2, 3.3, 4.4, 5.5]), 3.3)

    def test_large_numbers(self):
        self.assertAlmostEqual(avg_calc([sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize]), sys.maxsize)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            avg_calc("not a number")
