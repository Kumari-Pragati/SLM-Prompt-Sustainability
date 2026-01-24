import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('1', '2.5'), ('3.4', '5'), ('6', '7.8')]
        expected_output = "[('1.0', '2.5'), ('3.4', '5.0'), ('6.0', '7.8')]"
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

    def test_invalid_input(self):
        test_list = [('1', '2.5'), ('3.4', 'five')]
        with self.assertRaises(ValueError):
            list_to_float(test_list)
