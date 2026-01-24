import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('1', '2.2'), ('3.3', '4'), ('5', '6.6')]
        expected_output = "[('1.0', '2.2'), ('3.3', '4.0'), ('5.0', '6.6')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_edge_case_with_zero(self):
        test_list = [('0', '0'), ('0', '0')]
        expected_output = "[('0.0', '0.0'), ('0.0', '0.0')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_edge_case_with_negative_numbers(self):
        test_list = [('-1', '-2.2'), ('-3.3', '-4'), ('-5', '-6.6')]
        expected_output = "[('-1.0', '-2.2'), ('-3.3', '-4.0'), ('-5.0', '-6.6')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_corner_case_with_alphabets(self):
        test_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
        expected_output = "[('a', 'b'), ('c', 'd'), ('e', 'f')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [('1', '2.2'), ('3.3', '4'), ('invalid', '6.6')]
        with self.assertRaises(ValueError):
            list_to_float(test_list)
