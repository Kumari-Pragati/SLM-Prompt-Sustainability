import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_typical_input(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(tuple_to_dict(test_tup), {1: 2, 3: 4, 5: 6, 7: 8, 9: 10})

    def test_edge_case_empty_tuple(self):
        test_tup = ()
        self.assertEqual(tuple_to_dict(test_tup), {})

    def test_edge_case_single_element_tuple(self):
        test_tup = (1,)
        self.assertRaises(TypeError, tuple_to_dict, test_tup)

    def test_edge_case_tuple_with_one_element_per_two(self):
        test_tup = (1, 2, 3, 4)
        self.assertEqual(tuple_to_dict(test_tup), {1: 2, 3: 4})

    def test_edge_case_tuple_with_one_element_per_three(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7)
        self.assertRaises(TypeError, tuple_to_dict, test_tup)

    def test_invalid_input_non_tuple(self):
        test_tup = "not a tuple"
        self.assertRaises(TypeError, tuple_to_dict, test_tup)
