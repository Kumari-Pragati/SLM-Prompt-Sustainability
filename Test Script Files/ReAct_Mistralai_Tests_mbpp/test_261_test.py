import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_positive_integers(self):
        """Test division of two positive integers"""
        self.assertEqual(division_elements((3, 2, 5), (2, 1, 3)), (1, 2, 1))
        self.assertEqual(division_elements((10, 5, 2), (2, 1, 5)), (5, 5, 0))

    def test_zero_division(self):
        """Test division by zero"""
        self.assertRaises(ZeroDivisionError, lambda: division_elements((3, 2, 0), (2, 1, 1)))

    def test_negative_integers(self):
        """Test division of two negative integers"""
        self.assertEqual(division_elements((-3, -2, -5), (-2, -1, -3)), (1, 2, 1))
        self.assertEqual(division_elements((-10, -5, -2), (-2, -1, -5)), (5, 5, 0))

    def test_mixed_types(self):
        """Test division with mixed types"""
        self.assertRaises(TypeError, lambda: division_elements((3, 'a', 5), (2, 1, 3)))

    def test_empty_tuples(self):
        """Test division with empty tuples"""
        self.assertRaises(ValueError, lambda: division_elements((3,), (2,)))
        self.assertRaises(ValueError, lambda: division_elements((), (2,)))
