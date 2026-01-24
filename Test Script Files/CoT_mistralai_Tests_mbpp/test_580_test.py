import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):
    def test_empty_list(self):
        self.assertTupleEqual(extract_even([]), ())

    def test_single_even_number(self):
        self.assertTupleEqual(extract_even([2]), (2,))

    def test_single_odd_number(self):
        self.assertTupleEqual(extract_even([1]), ())

    def test_mixed_numbers(self):
        self.assertTupleEqual(extract_even([1, 2, 3, 4, 5, 6]), (2, 4,))

    def test_single_even_tuple(self):
        self.assertTupleEqual(extract_even(((2,),)), ((2,),))

    def test_mixed_tuples(self):
        self.assertTupleEqual(extract_even([(1,), (2,), (3,), (4,)]), ((2,),))

    def test_nesting(self):
        self.assertTupleEqual(extract_even([(1,), (2,), (3, (4,))]), ((2,), (3, (4,))))

    def test_invalid_input(self):
        self.assertRaises(TypeError, extract_even, [1.2, "str"])
