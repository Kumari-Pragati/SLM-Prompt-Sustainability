import unittest
from mbpp_172_code import count_occurance

class TestCountOcurrence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_occurance("std"), 1)

    def test_edge_case(self):
        self.assertEqual(count_occurance("st"), 0)

    def test_edge_case2(self):
        self.assertEqual(count_occurance("stds"), 1)

    def test_edge_case3(self):
        self.assertEqual(count_occurance("stdsdt"), 2)

    def test_edge_case4(self):
        self.assertEqual(count_occurance("stdstd"), 2)

    def test_edge_case5(self):
        self.assertEqual(count_occurance("stdstdstd"), 3)

    def test_edge_case6(self):
        self.assertEqual(count_occurance(""), 0)

    def test_edge_case7(self):
        self.assertEqual(count_occurance("s"), 0)

    def test_edge_case8(self):
        self.assertEqual(count_occurance("stdsdt"), 2)

    def test_edge_case9(self):
        self.assertEqual(count_occurance("stdstdstd"), 3)

    def test_edge_case10(self):
        self.assertEqual(count_occurance("stdstdstds"), 3)
