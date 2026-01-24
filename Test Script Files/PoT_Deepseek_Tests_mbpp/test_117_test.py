import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('1', '2.5'), ('3.4', '5.6')]
        expected_output = "[('1.0', '2.5'), ('3.4', '5.6')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_edge_case_with_zero(self):
        test_list = [('0', '0.0'), ('0.0', '0')]
        expected_output = "[('0.0', '0.0'), ('0.0', '0.0')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_boundary_case_with_negative_numbers(self):
        test_list = [('-1', '-2.5'), ('-3.4', '-5.6')]
        expected_output = "[('-1.0', '-2.5'), ('-3.4', '-5.6')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_corner_case_with_large_numbers(self):
        test_list = [('1000000', '2000000.5'), ('3000000.4', '5000000.6')]
        expected_output = "[('1000000.0', '2000000.5'), ('3000000.4', '5000000.6')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [('1', '2.5'), ('3.4', 'five')]
        with self.assertRaises(ValueError):
            list_to_float(test_list)
