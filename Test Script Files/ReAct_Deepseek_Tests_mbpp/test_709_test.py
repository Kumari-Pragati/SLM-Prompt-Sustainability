import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('apple', 'fruit'), ('banana', 'fruit'), ('carrot', 'vegetable')]
        expected_output = "{'fruit': 2, 'vegetable': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = "{}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_single_element(self):
        test_list = [('apple', 'fruit')]
        expected_output = "{'fruit': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_duplicate_elements(self):
        test_list = [('apple', 'fruit'), ('banana', 'fruit'), ('apple', 'fruit')]
        expected_output = "{'fruit': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_large_input(self):
        test_list = [(str(i), 'group'+str(i%5)) for i in range(1000)]
        expected_output = "{'group0': 334, 'group1': 334, 'group2': 334, 'group3': 334, 'group4': 333}"
        self.assertEqual(get_unique(test_list), expected_output)
