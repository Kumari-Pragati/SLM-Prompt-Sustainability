import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_substract_elements_positive(self):
        """Test substract_elements with positive numbers"""
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-4, -3, -3)))
        self.assertEqual(substract_elements((10, 20, 30), (40, 50, 60)), ((-30, -30, -30)))

    def test_substract_elements_zero(self):
        """Test substract_elements with zero"""
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), ((0, 0, 0)))
        self.assertEqual(substract_elements((0, 0, 1), (0, 0, 0)), ((0, 0, 1)))

    def test_substract_elements_negative(self):
        """Test substract_elements with negative numbers"""
        self.assertEqual(substract_elements((-1, -2, -3), (4, 5, 6)), ((5, 7, 9)))
        self.assertEqual(substract_elements((-10, -20, -30), (40, 50, 60)), ((-50, -70, -90)))

    def test_substract_elements_mixed(self):
        """Test substract_elements with mixed numbers"""
        self.assertEqual(substract_elements((1, -2, 3), (4, 5, 6)), ((-3, 3, -3)))
        self.assertEqual(substract_elements((10, -20, 30), (40, 50, 60)), ((-30, -30, 30)))

    def test_substract_elements_empty_tuples(self):
        """Test substract_elements with empty tuples"""
        self.assertEqual(substract_elements((), ()), ())
        self.assertEqual(substract_elements((1, 2, 3), ()), ((1, 2, 3)))
        self.assertEqual(substract_elements((), (1, 2, 3)), ((-1, -2, -3)))

    def test_substract_elements_different_lengths(self):
        """Test substract_elements with tuples of different lengths"""
        with self.assertRaises(ValueError):
            substract_elements((1, 2, 3), (1, 2))
        with self.assertRaises(ValueError):
            substract_elements((1, 2), (1, 2, 3))
