import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        self.assertAlmostEqual(div_even_odd([]), float('nan'))

    def test_single_even_number(self):
        self.assertAlmostEqual(div_even_odd([2]), 2)

    def test_single_odd_number(self):
        self.assertAlmostEqual(div_even_odd([3]), 1)

    def test_mixed_list_even_first(self):
        self.assertAlmostEqual(div_even_odd([2, 3]), 2/3)

    def test_mixed_list_odd_first(self):
        self.assertAlmostEqual(div_even_odd([3, 2]), 3/2)

    def test_all_even_numbers(self):
        self.assertAlmostEqual(div_even_odd([2, 4, 6]), 2/6)

    def test_all_odd_numbers(self):
        self.assertAlmostEqual(div_even_odd([1, 3, 5]), 1/5)

    def test_invalid_input_empty_list_raise_ValueError(self):
        with self.assertRaises(ValueError):
            div_even_odd([])

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            div_even_odd(['a', 2, 3])
