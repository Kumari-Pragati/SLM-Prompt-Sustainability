import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_substract_elements_positive(self):
        """Test substract_elements with positive numbers"""
        self.assertEqual(substract_elements((1, 2, 3), (2, 1, 0)), (1, 1, -3))
        self.assertEqual(substract_elements((5, -3, 0), (3, -2, 1)), (8, -5, -1))

    def test_substract_elements_zero(self):
        """Test substract_elements with zero elements"""
        self.assertEqual(substract_elements((0,), (0,)), (0,))
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), (0, 0, 0))

    def test_substract_elements_negative(self):
        """Test substract_elements with negative numbers"""
        self.assertEqual(substract_elements((-3, -2, -1), (-1, -2, -3)), (4, 3, 4))
        self.assertEqual(substract_elements((-5, -3, 0), (-3, -2, 1)), (-8, -5, -1))

    def test_substract_elements_mixed_signs(self):
        """Test substract_elements with mixed signs"""
        self.assertEqual(substract_elements((1, -2, 3), (-1, 2, -3)), (2, 4, 6))
        self.assertEqual(substract_elements((-1, 2, -3), (1, -2, 3)), (-2, 4, -6))

    def test_substract_elements_empty_tuples(self):
        """Test substract_elements with empty tuples"""
        self.assertEqual(substract_elements((), ()), ())
        self.assertEqual(substract_elements((1, 2, 3), ()), (1, 2, 3))
        self.assertEqual(substract_elements((), (1, 2, 3)), (0, 0, 0))

    def test_substract_elements_different_lengths(self):
        """Test substract_elements with tuples of different lengths"""
        self.assertEqual(substract_elements((1, 2, 3), (1, 2)), (0, 0, 3))
        self.assertRaises(ValueError, substract_elements, (1, 2, 3), (1, 2, 3, 4))
