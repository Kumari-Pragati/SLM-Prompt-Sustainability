import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_adverbs("Hello world slowly"), "0-9: slowly")

    def test_edge_case(self):
        self.assertEqual(find_adverbs(""), "")

    def test_edge_case2(self):
        self.assertEqual(find_adverbs("Hello world"), "")

    def test_edge_case3(self):
        self.assertEqual(find_adverbs("Slowly"), "0-6: Slowly")

    def test_edge_case4(self):
        self.assertEqual(find_adverbs("Slowly slowly"), "0-7: Slowly 8-11: slowly")

    def test_edge_case5(self):
        self.assertEqual(find_adverbs("Slowly slowly slowly"), "0-7: Slowly 8-11: slowly 12-15: slowly")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_adverbs(123)
