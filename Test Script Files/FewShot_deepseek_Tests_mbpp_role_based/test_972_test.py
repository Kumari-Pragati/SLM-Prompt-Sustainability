import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))

    def test_edge_condition(self):
        self.assertEqual(concatenate_nested((), (3, 4)), (3, 4))
        self.assertEqual(concatenate_nested((1, 2), ()), (1, 2))

    def test_boundary_condition(self):
        self.assertEqual(concatenate_nested((1,), (2,)), (1, 2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            concatenate_nested((1, 2), '3, 4')
