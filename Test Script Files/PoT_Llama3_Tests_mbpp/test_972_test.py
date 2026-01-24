import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))

    def test_empty_tuples(self):
        self.assertEqual(concatenate_nested((), ()), ())

    def test_single_tuple(self):
        self.assertEqual(concatenate_nested((1, 2), ()), (1, 2))

    def test_empty_tuple_on_left(self):
        self.assertEqual(concatenate_nested((), (1, 2)), (1, 2))

    def test_empty_tuple_on_right(self):
        self.assertEqual(concatenate_nested((1, 2), ()), (1, 2))

    def test_concatenating_tuples_of_diff_lengths(self):
        self.assertEqual(concatenate_nested((1, 2, 3), (4, 5)), (1, 2, 3, 4, 5))

    def test_concatenating_tuples_of_same_length(self):
        self.assertEqual(concatenate_nested((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))
