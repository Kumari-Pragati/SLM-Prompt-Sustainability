import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 3, 4, 5, 6)
        expected_result = {1: 2, 3: 4}
        self.assertEqual(tuple_to_dict(test_tup), expected_result)

    def test_edge_case_empty_tuple(self):
        test_tup = ()
        expected_result = {}
        self.assertEqual(tuple_to_dict(test_tup), expected_result)

    def test_edge_case_single_element_tuple(self):
        test_tup = (1,)
        expected_result = {}
        self.assertEqual(tuple_to_dict(test_tup), expected_result)

    def test_edge_case_tuple_with_one_element_group(self):
        test_tup = (1, 2, 3)
        expected_result = {1: 2}
        self.assertEqual(tuple_to_dict(test_tup), expected_result)

    def test_edge_case_tuple_with_two_element_group(self):
        test_tup = (1, 2, 3, 4)
        expected_result = {1: 2, 3: 4}
        self.assertEqual(tuple_to_dict(test_tup), expected_result)

    def test_edge_case_tuple_with_three_element_group(self):
        test_tup = (1, 2, 3, 4, 5, 6)
        expected_result = {1: 2, 3: 4, 5: 6}
        self.assertEqual(tuple_to_dict(test_tup), expected_result)

    def test_invalid_input_non_tuple(self):
        test_tup = "Invalid input"
        with self.assertRaises(TypeError):
            tuple_to_dict(test_tup)
