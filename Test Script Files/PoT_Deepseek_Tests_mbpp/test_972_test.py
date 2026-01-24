import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_nested((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_empty_tuples(self):
        self.assertEqual(concatenate_nested((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(concatenate_nested((1,), (2,)), (1, 2))

    def test_large_tuples(self):
        self.assertEqual(concatenate_nested((1, 2, 3) * 1000, (4, 5, 6) * 1000), (1, 2, 3) * 2000)

    def test_mixed_types(self):
        self.assertEqual(concatenate_nested((1, 'a', [1, 2]), (3, 'b', [3, 4])), (1, 'a', [1, 2], 3, 'b', [3, 4]))

    def test_nested_tuples(self):
        self.assertEqual(concatenate_nested((1, (2, 3)), ((4, 5), 6)), (1, (2, 3), (4, 5), 6))
