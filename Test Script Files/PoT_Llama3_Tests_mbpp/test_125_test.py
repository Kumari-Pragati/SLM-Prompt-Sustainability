import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_length('110100', 6), 2)

    def test_edge_case_zero(self):
        self.assertEqual(find_length('000000', 6), 0)

    def test_edge_case_all_one(self):
        self.assertEqual(find_length('111111', 6), 6)

    def test_edge_case_all_zero(self):
        self.assertEqual(find_length('000000', 6), 0)

    def test_edge_case_mixed(self):
        self.assertEqual(find_length('101010', 6), 2)

    def test_edge_case_mixed_long(self):
        self.assertEqual(find_length('101010101010', 12), 4)

    def test_edge_case_mixed_longer(self):
        self.assertEqual(find_length('1010101010101010', 12), 4)

    def test_edge_case_mixed_longest(self):
        self.assertEqual(find_length('101010101010101010', 12), 4)

    def test_edge_case_mixed_longest_longer(self):
        self.assertEqual(find_length('101010101010101010101010', 12), 4)

    def test_edge_case_mixed_longest_longest(self):
        self.assertEqual(find_length('1010101010101010101010101010', 12), 4)

    def test_edge_case_mixed_longest_longest_longer(self):
        self.assertEqual(find_length('1010101010101010101010101010101010', 12), 4)

    def test_edge_case_mixed_longest_longest_longest(self):
        self.assertEqual(find_length('101010101010101010101010101010101010', 12), 4)

    def test_edge_case_mixed_longest_longest_longest_longer(self):
        self.assertEqual(find_length('1010101010101010101010101010101010101010', 12), 4)

    def test_edge_case_mixed_longest_longest_longest_longest_longer(self):
        self.assertEqual(find_length('101010101010101010101010101010101010101010', 12), 4)
