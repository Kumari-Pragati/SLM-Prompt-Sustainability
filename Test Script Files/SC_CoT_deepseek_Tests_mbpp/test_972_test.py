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
        large_tuple = (i for i in range(1000))
        self.assertEqual(concatenate_nested(large_tuple, large_tuple), large_tuple)

    def test_mixed_types(self):
        self.assertEqual(concatenate_nested((1, 'a'), (2, 'b')), (1, 'a', 2, 'b'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            concatenate_nested(1, 2)
