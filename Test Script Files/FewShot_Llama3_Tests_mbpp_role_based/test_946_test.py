import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):
    def test_typical_use_case(self):
        s = "hellohellohello"
        a = 2
        expected_result = [('l', 3), ('o', 2), ('h', 3)]
        self.assertEqual(most_common_elem(s, a), expected_result)

    def test_edge_case_a_zero(self):
        s = "hellohellohello"
        a = 0
        expected_result = []
        self.assertEqual(most_common_elem(s, a), expected_result)

    def test_edge_case_a_one(self):
        s = "hellohellohello"
        a = 1
        expected_result = [('l', 3), ('o', 2), ('h', 3)]
        self.assertEqual(most_common_elem(s, a), expected_result)

    def test_edge_case_empty_string(self):
        s = ""
        a = 2
        expected_result = []
        self.assertEqual(most_common_elem(s, a), expected_result)

    def test_edge_case_a_greater_than_string_length(self):
        s = "hellohellohello"
        a = 5
        expected_result = [('l', 3), ('o', 2), ('h', 3)]
        self.assertEqual(most_common_elem(s, a), expected_result)
