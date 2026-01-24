import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(substract_elements((10, 20, 30), (5, 10, 15)), (5, 10, 15))

    def test_empty_tuples(self):
        self.assertEqual(substract_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(substract_elements((10,), (5,)), (5,))

    def test_negative_numbers(self):
        self.assertEqual(substract_elements((10, 20, 30), (50, 40, 30)), (-40, -20, 0))

    def test_zero_elements(self):
        self.assertEqual(substract_elements((0, 0, 0), (10, 20, 30)), (-10, -20, -30))

    def test_mismatch_length_tuples(self):
        with self.assertRaises(ValueError):
            substract_elements((10, 20, 30), (5, 10))
