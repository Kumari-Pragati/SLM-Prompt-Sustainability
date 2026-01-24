import unittest
from mbpp_259_code import maximize_elements

class TestMaximizeElements(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(maximize_elements((1, 2, 3), (4, 5, 6)), ((4, 5, 6)))

    def test_negative_numbers(self):
        self.assertEqual(maximize_elements((-1, -2, -3), (-4, -5, -6)), ((-1, -2, -3)))

    def test_mixed_numbers(self):
        self.assertEqual(maximize_elements((1, -2, 3), (-4, 5, -6)), ((1, 5, 3)))

    def test_equal_numbers(self):
        self.assertEqual(maximize_elements((1, 2, 3), (1, 2, 3)), ((1, 2, 3)))

    def test_empty_tuples(self):
        self.assertEqual(maximize_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(maximize_elements((1,), (2,)), ((2,)))
