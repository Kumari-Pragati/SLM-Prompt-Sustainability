import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_simple_accepted(self):
        self.assertEqual(check("AaEiouU"), 'accepted')

    def test_simple_not_accepted(self):
        self.assertEqual(check("AbCdEf"), 'not accepted')

    def test_edge_case_min_length(self):
        self.assertEqual(check("AaEiou"), 'not accepted')

    def test_edge_case_max_length(self):
        self.assertEqual(check("AaEiouAaEiouAaEiouAaEiouAaEiou"), 'accepted')

    def test_edge_case_special_characters(self):
        self.assertEqual(check("AaEiou!@#$%^&*()"), 'not accepted')

    def test_edge_case_only_vowels(self):
        self.assertEqual(check("AaEiou"), 'accepted')

    def test_edge_case_only_consonants(self):
        self.assertEqual(check("AbCdEf"), 'not accepted')

    def test_edge_case_empty_string(self):
        self.assertEqual(check(""), 'not accepted')
