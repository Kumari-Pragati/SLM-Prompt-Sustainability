import unittest
from mbpp_888_code import substract_elements

class TestSubtractElements(unittest.TestCase):

    def test_simple_subtraction(self):
        self.assertEqual(subtract_elements((1, 2, 3), (4, 5, 6)), ((-3, -3, -3),))

    def test_empty_tuples(self):
        self.assertEqual(subtract_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(subtract_elements((10), (5)), ((5),))

    def test_negative_numbers(self):
        self.assertEqual(subtract_elements((10, -5, 0), (5, 0, -5)), ((5, -5, 5),))

    def test_maximum_and_minimum_values(self):
        self.assertEqual(subtract_elements((1000000000, -1000000000), (1, -1)), ((999999999, -999999999),))

    def test_different_length_tuples(self):
        self.assertEqual(subtract_elements((1, 2, 3), (1, 2)), ((0, 0),))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            subtract_elements((1, 2, 3), "not a tuple")
