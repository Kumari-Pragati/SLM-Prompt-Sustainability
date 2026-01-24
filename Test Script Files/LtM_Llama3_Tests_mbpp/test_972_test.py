import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):
    def test_simple_concatenation(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))

    def test_empty_inputs(self):
        self.assertEqual(concatenate_nested((), ()), ())

    def test_single_tuple(self):
        self.assertEqual(concatenate_nested((1, 2), ()), (1, 2))

    def test_empty_first(self):
        self.assertEqual(concatenate_nested((), (1, 2)), (1, 2))

    def test_empty_second(self):
        self.assertEqual(concatenate_nested((1, 2), ()), (1, 2))

    def test_concatenation_of_tuples_with_duplicates(self):
        self.assertEqual(concatenate_nested((1, 1, 2), (2, 2, 3)), (1, 1, 2, 2, 2, 3))
