import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))

    def test_edge_cases(self):
        self.assertEqual(concatenate_nested((1, 2), ()), (1, 2))
        self.assertEqual(concatenate_nested((), (3, 4)), (3, 4))

    def test_empty_inputs(self):
        self.assertEqual(concatenate_nested((), ()), ())

    def test_single_element_inputs(self):
        self.assertEqual(concatenate_nested((1,), (2,)), (1, 2))
        self.assertEqual(concatenate_nested((1,),), (1,))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            concatenate_nested("a", (1, 2))
        with self.assertRaises(TypeError):
            concatenate_nested((1, 2), "a")
