import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))

    def test_edge_case_empty_tuples(self):
        self.assertEqual(concatenate_nested(()), ())
        self.assertEqual(concatenate_nested((), (1, 2, 3)), (1, 2, 3))

    def test_edge_case_single_element_tuples(self):
        self.assertEqual(concatenate_nested((1,), (2, 3)), (1, 2, 3))
        self.assertEqual(concatenate_nested((1,), (2,)), (1, 2))

    def test_corner_case_mixed_types(self):
        self.assertRaises(TypeError, concatenate_nested, (1, 2), [3, 4])
