import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_lowercase("HelloWorld"), "HELLOWORLD")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_lowercase(""), "")

    def test_edge_case_single_uppercase(self):
        self.assertEqual(remove_lowercase("A"), "A")

    def test_edge_case_single_lowercase(self):
        self.assertEqual(remove_lowercase("a"), "")

    def test_edge_case_single_mixed(self):
        self.assertEqual(remove_lowercase("Aa"), "A")

    def test_edge_case_all_lowercase(self):
        self.assertEqual(remove_lowercase("helloWorld"), "")

    def test_edge_case_all_uppercase(self):
        self.assertEqual(remove_lowercase("HELLOWORLD"), "HELLOWORLD")
