import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_simple_concatenation(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))

    def test_concatenation_with_empty_tuples(self):
        self.assertEqual(concatenate_nested((1, 2), ()), (1, 2))
        self.assertEqual(concatenate_nested((), (3, 4)), (3, 4))

    def test_concatenation_with_single_element_tuples(self):
        self.assertEqual(concatenate_nested((1,), (2, 3)), (1, 2, 3))
        self.assertEqual(concatenate_nested((1,), (2,)), (1, 2))

    def test_concatenation_with_longer_tuples(self):
        self.assertEqual(concatenate_nested((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))
        self.assertEqual(concatenate_nested((1, 2, 3), (4,)), (1, 2, 3, 4))
