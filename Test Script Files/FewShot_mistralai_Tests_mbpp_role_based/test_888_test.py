import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(substract_elements((1, 2, 3), (3, 2, 1)), (0, 0, 0))
        self.assertEqual(substract_elements((4, 5, 6), (1, 2, 3)), (3, 3, 3))

    def test_zero(self):
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), (0, 0, 0))

    def test_negative_numbers(self):
        self.assertEqual(substract_elements((-1, -2, -3), (-3, -2, -1)), (4, 4, 4))
        self.assertEqual(substract_elements((-4, -5, -6), (-1, -2, -3)), (-5, -7, -9))

    def test_mixed_numbers(self):
        self.assertEqual(substract_elements((1, -2, 3), (-3, 2, 1)), (4, 0, 4))
        self.assertEqual(substract_elements((-1, 2, -3), (3, -2, 1)), (-4, 0, -4))

    def test_empty_tuples(self):
        self.assertEqual(substract_elements((), ()), ())
        self.assertEqual(substract_elements((1,), ()), ())
        self.assertEqual(substract_elements((), (1,)) , ())

    def test_different_length_tuples(self):
        self.assertRaises(ValueError, substract_elements, (1, 2, 3), (1, 2))
        self.assertRaises(ValueError, substract_elements, (1, 2), (1, 2, 3))
