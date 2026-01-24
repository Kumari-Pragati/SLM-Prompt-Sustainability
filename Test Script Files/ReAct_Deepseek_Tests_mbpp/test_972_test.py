import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))

    def test_empty_tuples(self):
        self.assertEqual(concatenate_nested((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(concatenate_nested((1,), (2,)), (1, 2))

    def test_large_tuples(self):
        self.assertEqual(concatenate_nested(tuple(range(1, 10)), tuple(range(10, 20))), 
                         tuple(range(1, 20)))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            concatenate_nested((1, 'a'), (2, 3))
