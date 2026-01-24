import unittest
from mbpp_823_code import check_substring

class TestCheckSubscription(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(check_substring("HelloWorld", "Hello"), "string starts with the given substring")
        self.assertEqual(check_substring("PythonRocks", "Python"), "string starts with the given substring")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(check_substring("", "Sample"), "entered string isnt a substring")
        self.assertEqual(check_substring("Sample", ""), "entered string isnt a substring")
        self.assertEqual(check_substring("Sample", "Sa"), "string doesnt start with the given substring")
        self.assertEqual(check_substring("SaSample", "Sample"), "string starts with the given substring")

    def test_starts_with_regex(self):
        self.assertEqual(check_substring("HelloWorld", "\AHello"), "string starts with the given substring")
        self.assertEqual(check_substring("PythonRocks", "\APython"), "string starts with the given substring")
        self.assertEqual(check_substring("", "\A"), "entered string isnt a substring")
        self.assertEqual(check_substring("Sample", "\ASample"), "string starts with the given substring")
