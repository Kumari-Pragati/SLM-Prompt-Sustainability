import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(division_elements((10, 2), (20, 4)), (5, 5))

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((10, 0), (20, 4))

    def test_single_element_input(self):
        self.assertEqual(division_elements((10,), (20,)), (0,))

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            division_elements((), (20,))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            division_elements([10], (20,))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            division_elements((10.5, 20), (20.5, 4))
