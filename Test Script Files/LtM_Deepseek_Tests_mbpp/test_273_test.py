import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_simple_subtraction(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), (-3, -3, -3))

    def test_empty_tuples(self):
        self.assertEqual(substract_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(substract_elements((10), (5)), (5))

    def test_large_numbers(self):
        self.assertEqual(substract_elements((1000000, 2000000), (1000000, 2000000)), (0, 0))

    def test_negative_numbers(self):
        self.assertEqual(substract_elements((-1, -2, -3), (-4, -5, -6)), (3, 3, 3))

    def test_mixed_numbers(self):
        self.assertEqual(substract_elements((1, -2, 3), (4, -5, 6)), (-3, 7, -3))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            substract_elements((1, 2, 3), (4, 5))
