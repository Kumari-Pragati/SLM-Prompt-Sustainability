import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):

    def test_count_occurance(self):
        self.assertEqual(count_occurance("std"), 1)
        self.assertEqual(count_occurance("stds"), 1)
        self.assertEqual(count_occurance("stdstd"), 2)
        self.assertEqual(count_occurance("stdstds"), 2)
        self.assertEqual(count_occurance("stdstdstd"), 3)
        self.assertEqual(count_occurance(""), 0)
        self.assertEqual(count_occurance("st"), 0)
        self.assertEqual(count_occurance("stda"), 0)
        self.assertEqual(count_occurance("stdsdf"), 1)
        self.assertEqual(count_occurance("stdstdsdf"), 2)

    def test_count_occurance_edge_cases(self):
        self.assertEqual(count_occurance("st"), 0)
        self.assertEqual(count_occurance("std"), 1)
        self.assertEqual(count_occurance("stds"), 1)
        self.assertEqual(count_occurance("stdstd"), 2)
        self.assertEqual(count_occurance("stdstds"), 2)
        self.assertEqual(count_occurance("stdstdstd"), 3)
        self.assertEqual(count_occurance("stdstdstds"), 3)
        self.assertEqual(count_occurance("stdstdstdsdf"), 3)
