import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_lowercase("HelloWorld"), "HELLOWORLD")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_lowercase(""), "")

    def test_edge_case_single_uppercase_letter(self):
        self.assertEqual(remove_lowercase("A"), "A")

    def test_edge_case_single_lowercase_letter(self):
        self.assertEqual(remove_lowercase("a"), "")

    def test_edge_case_mixed_case(self):
        self.assertEqual(remove_lowercase("HeLlOwOrLd"), "HELLOWRD")

    def test_boundary_case_long_string(self):
        self.assertEqual(remove_lowercase("ThisIsALongStringWithMixedCasesAndSpecialCharacters123!@#$%^&*()_+-={}[\]:;'<,>.?"), "THISISALONGSTRINGWITHMIXEDCASSESANDSPECIALCHARACTERS123!@#$%^&*()_+-={}[\]:;'<,>.?")
