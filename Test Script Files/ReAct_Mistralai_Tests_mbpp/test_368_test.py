import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):

    def test_empty_tuple(self):
        """Test repeating an empty tuple."""
        self.assertTupleEqual(repeat_tuples((), 3), ((), (), ()))

    def test_single_element_tuple(self):
        """Test repeating a single-element tuple."""
        self.assertTupleEqual(repeat_tuples((1,), 3), ((1,), (1,), (1,)))

    def test_multiple_elements_tuple(self):
        """Test repeating a multiple-elements tuple."""
        self.assertTupleEqual(repeat_tuples((1, 2, 3), 3), ((1, 2, 3), (1, 2, 3), (1, 2, 3)))

    def test_negative_N(self):
        """Test handling negative N."""
        with self.assertRaises(ValueError):
            repeat_tuples((1, 2, 3), -1)

    def test_zero_N(self):
        """Test handling zero N."""
        self.assertTupleEqual(repeat_tuples((1, 2, 3), 0), ())
