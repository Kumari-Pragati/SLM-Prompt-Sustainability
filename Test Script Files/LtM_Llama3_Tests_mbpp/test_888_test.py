import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_empty_inputs(self):
        self.assertEqual(substract_elements((), (1,)), ())
        self.assertEqual(substract_elements((1,), ()), ())
        self.assertEqual(substract_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(substract_elements((1,), (1,)), ())
        self.assertEqual(substract_elements((1, 2), (1, 2)), ())
        self.assertEqual(substract_elements((1, 2, 3), (1, 2, 3)), ())

    def test_tuples_of_different_lengths(self):
        self.assertEqual(substract_elements((1, 2), (1, 2, 3)), ((0, 1),))
        self.assertEqual(substract_elements((1, 2, 3), (1, 2)), ((1, 2), (2, 3)))
        self.assertEqual(substract_elements((1, 2, 3, 4), (1, 2, 3)), ((1, 1), (2, 2), (3,)))

    def test_tuples_with_negative_numbers(self):
        self.assertEqual(substract_elements((-1, 1), (-1, 1)), (0,))
        self.assertEqual(substract_elements((-1, -2), (-1, -2)), (1,))

    def test_tuples_with_zero(self):
        self.assertEqual(substract_elements((0, 1), (0, 1)), (1,))
        self.assertEqual(substract_elements((0, 1, 2), (0, 1, 2)), (1, 2))
