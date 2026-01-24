import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):
    def test_concatenate_nested_typical(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))

    def test_concatenate_nested_empty(self):
        self.assertEqual(concatenate_nested((), ()), ())

    def test_concatenate_nested_single(self):
        self.assertEqual(concatenate_nested((1,), (2,)), (1, 2))

    def test_concatenate_nested_empty_and_single(self):
        self.assertEqual(concatenate_nested((), (1,)), (1,))

    def test_concatenate_nested_single_and_empty(self):
        self.assertEqual(concatenate_nested((1,), ()), (1,))

    def test_concatenate_nested_non_tuple(self):
        with self.assertRaises(TypeError):
            concatenate_nested(1, (2, 3))

    def test_concatenate_nested_non_tuple2(self):
        with self.assertRaises(TypeError):
            concatenate_nested((1, 2), 3)

    def test_concatenate_nested_non_tuple3(self):
        with self.assertRaises(TypeError):
            concatenate_nested(1, 2)
