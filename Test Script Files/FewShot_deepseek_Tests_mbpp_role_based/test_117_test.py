import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('1', '2'), ('3', '4')]
        expected_output = "[('1.0', '2.0'), ('3.0', '4.0')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_edge_case_with_single_element(self):
        test_list = [('5',)]
        expected_output = "[('5.0',)]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_boundary_condition_with_empty_list(self):
        test_list = []
        expected_output = "[]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_error_handling_with_invalid_input(self):
        test_list = [('1', 'two'), ('three', '4')]
        with self.assertRaises(ValueError):
            list_to_float(test_list)
