import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_division_elements(self):
        self.assertEqual(division_elements((10, 20, 30), (2, 4, 6)), ((5, 5, 5)))
        self.assertEqual(division_elements((15, 25, 35), (3, 5, 7)), ((5, 5, 5)))
        self.assertEqual(division_elements((100, 200, 300), (10, 20, 30)), ((10, 10, 10)))

    def test_division_elements_with_zero(self):
        self.assertEqual(division_elements((10, 20, 30), (0, 4, 6)), ((float('inf'), 5, 5)))

    def test_division_elements_with_negative_numbers(self):
        self.assertEqual(division_elements((-10, -20, -30), (2, 4, 6)), ((-5, -5, -5)))
        self.assertEqual(division_elements((10, 20, 30), (-2, -4, -6)), ((-5, -5, -5)))

    def test_division_elements_with_different_lengths(self):
        with self.assertRaises(ValueError):
            division_elements((1, 2, 3, 4), (1, 2))
