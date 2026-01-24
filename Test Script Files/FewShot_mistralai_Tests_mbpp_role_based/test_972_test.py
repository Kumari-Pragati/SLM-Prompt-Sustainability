import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(concatenate_nested((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_empty_tuples(self):
        self.assertEqual(concatenate_nested((), (1, 2, 3)), (1, 2, 3))
        self.assertEqual(concatenate_nested((1, 2, 3),()), (1, 2, 3))

    def test_single_element_tuples(self):
        self.assertEqual(concatenate_nested((1,), (2, 3)), (1, 2, 3))
        self.assertEqual(concatenate_nested((1, 2), (3,)), (1, 2, 3))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            concatenate_nested((1, 2, 3), 'abc')
