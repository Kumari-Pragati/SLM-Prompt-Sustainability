import unittest
from mbpp_259_code import maximize_elements

class TestMaximizeElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(maximize_elements((1, 2), (3, 4)), ((3, 4)))
        self.assertEqual(maximize_elements((5, 6), (7, 8)), ((7, 8)))

    def test_zero_and_negative_numbers(self):
        self.assertEqual(maximize_elements((-1, 0), (0, -2)), ((0, -2)))
        self.assertEqual(maximize_elements((-3, -4), (-5, -6)), ((-5, -6)))

    def test_mixed_numbers(self):
        self.assertEqual(maximize_elements((-1, 0, 1), (0, -2, 3)), ((0, -2, 3)))
        self.assertEqual(maximize_elements((-3, -2, 1), (-5, -4, 0)), ((-5, -4, 0)))

    def test_empty_tuples(self):
        self.assertEqual(maximize_elements((), ()), ())
        self.assertEqual(maximize_elements((1,), (2,)), ((2,)))
        self.assertEqual(maximize_elements((1,), ((2,))), ((2,)))
