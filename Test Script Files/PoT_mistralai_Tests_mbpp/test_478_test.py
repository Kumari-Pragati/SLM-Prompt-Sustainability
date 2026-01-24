import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_lowercase("ABCabc123"), "ABC123")
        self.assertEqual(remove_lowercase("ABC_123"), "ABC_123")
        self.assertEqual(remove_lowercase("ABC-123"), "ABC-123")

    def test_edge_case(self):
        self.assertEqual(remove_lowercase("A"), "A")
        self.assertEqual(remove_lowercase(""), "")
        self.assertEqual(remove_lowercase("a"), "")
        self.assertEqual(remove_lowercase("Aa"), "A")
        self.assertEqual(remove_lowercase("A123"), "A123")
        self.assertEqual(remove_lowercase("123"), "123")
