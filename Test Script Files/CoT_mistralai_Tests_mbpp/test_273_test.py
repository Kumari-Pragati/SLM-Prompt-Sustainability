import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(substract_elements((1, 2, 3), (2, 3, 4)), (-1, 1, -1))
        self.assertEqual(substract_elements((5, 10, 15), (3, 6, 9)), (-2, -4, -6))

    def test_zero_numbers(self):
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), (0, 0, 0))

    def test_negative_numbers(self):
        self.assertEqual(substract_elements((-1, -2, -3), (-2, -3, -4)), (1, 1, 1))
        self.assertEqual(substract_elements((-5, -10, -15), (-3, -6, -9)), (2, 4, 6))

    def test_mixed_numbers(self):
        self.assertEqual(substract_elements((1, -2, 3), (-2, 2, 4)), (3, -4, 7))
        self.assertEqual(substract_elements((-1, 2, -3), (2, -2, 4)), (-3, 4, -1))

    def test_empty_tuples(self):
        self.assertEqual(substract_elements((), ()), ())

    def test_different_length_tuples(self):
        with self.assertRaises(ValueError):
            substract_elements((1, 2, 3), (1, 2))

    def test_non_tuple_inputs(self):
        with self.assertRaises(TypeError):
            substract_elements(1, 2)
        with self.assertRaises(TypeError):
            substract_elements([1, 2, 3], [4, 5, 6])
