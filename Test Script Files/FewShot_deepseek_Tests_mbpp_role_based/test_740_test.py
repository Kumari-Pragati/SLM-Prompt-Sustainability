import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (('a', 1), ('b', 2), ('c', 3))
        expected_output = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(tuple_to_dict(test_tup), expected_output)

    def test_edge_condition(self):
        test_tup = (('a', 1))
        expected_output = {'a': 1}
        self.assertEqual(tuple_to_dict(test_tup), expected_output)

    def test_boundary_condition(self):
        test_tup = ()
        expected_output = {}
        self.assertEqual(tuple_to_dict(test_tup), expected_output)

    def test_invalid_input(self):
        test_tup = (1, 2, 3)
        with self.assertRaises(TypeError):
            tuple_to_dict(test_tup)
