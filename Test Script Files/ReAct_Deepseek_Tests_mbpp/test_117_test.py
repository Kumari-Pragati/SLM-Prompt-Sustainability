import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('1', '2.5'), ('3.4', '5.6')]
        expected_output = "[('1.0', '2.5'), ('3.4', '5.6')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_edge_case_with_alpha(self):
        test_list = [('a', '2.5'), ('3.4', 'b')]
        expected_output = "[('a', '2.5'), ('3.4', 'b')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = "[]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_single_element(self):
        test_list = [('1', '2.5')]
        expected_output = "[('1.0', '2.5')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_all_alpha(self):
        test_list = [('a', 'b'), ('c', 'd')]
        expected_output = "[('a', 'b'), ('c', 'd')]"
        self.assertEqual(list_to_float(test_list), expected_output)

    def test_all_numeric(self):
        test_list = [(1, 2), (3, 4)]
        expected_output = "[('1.0', '2.0'), ('3.0', '4.0')]"
        self.assertEqual(list_to_float(test_list), expected_output)
