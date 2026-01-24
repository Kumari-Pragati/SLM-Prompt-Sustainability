import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5, 6)
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), (1, 2, 3, 4, 5, 6))

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), ())

    def test_single_tuple(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = ()
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), (1, 2, 3))

    def test_non_tuple_input(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = "not a tuple"
        with self.assertRaises(TypeError):
            concatenate_nested(test_tup1, test_tup2)
