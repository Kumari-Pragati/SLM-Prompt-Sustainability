import unittest
from mbpp_686_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 2, 3, 3, 3)
        expected_output = "{'1': '1', '2': '2', '3': '3'}"
        self.assertEqual(freq_element(test_tup), expected_output)

    def test_empty_input(self):
        test_tup = ()
        expected_output = "{}"
        self.assertEqual(freq_element(test_tup), expected_output)

    def test_single_element_input(self):
        test_tup = (1,)
        expected_output = "'1': '1'"
        self.assertEqual(freq_element(test_tup), expected_output)

    def test_duplicates(self):
        test_tup = (1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5)
        expected_output = "{'1': '1', '2': '2', '3': '3', '4': '4', '5': '5'}"
        self.assertEqual(freq_element(test_tup), expected_output)

    def test_non_integer_elements(self):
        test_tup = ('a', 'b', 'c', 'a', 'b', 'c')
        expected_output = "{'a': '2', 'b': '2', 'c': '2'}"
        self.assertEqual(freq_element(test_tup), expected_output)
