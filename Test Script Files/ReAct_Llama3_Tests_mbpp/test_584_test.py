import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_adverbs("I am going to the store slowly"), "0-10: slowly")

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverbs("I am going to the store slowly and quickly"), "0-10: slowly")
        self.assertEqual(find_adverbs("0-10: slowly"), "0-10: slowly")

    def test_no_adverbs(self):
        self.assertIsNone(find_adverbs("I am going to the store"))

    def test_edge_case(self):
        self.assertEqual(find_adverbs("I am going to the store slowly slowly"), "0-10: slowly")

    def test_error_case(self):
        with self.assertRaises(TypeError):
            find_adverbs(123)
