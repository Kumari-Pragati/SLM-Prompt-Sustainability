import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_division_elements_positive(self):
        self.assertTupleEqual(division_elements((5, 2, 3), (2, 3, 1)), (2, 1, 3))
        self.assertTupleEqual(division_elements((10, 5, 2), (2, 5, 10)), (5, 1, 2))

    def test_division_elements_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: division_elements((0, 2, 3), (2, 3, 1)))
        self.assertRaises(ZeroDivisionError, lambda: division_elements((2, 0, 3), (2, 3, 1)))

    def test_division_elements_mixed_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: division_elements((0, 2, 3), (2, 0, 1)))
        self.assertRaises(ZeroDivisionError, lambda: division_elements((2, 0, 3), (2, 3, 0)))

    def test_division_elements_length_mismatch(self):
        self.assertRaises(ValueError, lambda: division_elements((5, 2, 3), (2, 3)))
        self.assertRaises(ValueError, lambda: division_elements((5, 2, 3), (2, 3, 4)))
