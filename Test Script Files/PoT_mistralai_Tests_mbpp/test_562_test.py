import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Find_Max_Length([1, 2, 3, 4, 5]), 5)
        self.assertEqual(Find_Max_Length(["hello", "world"]), 5)
        self.assertEqual(Find_Max_Length([1, 2, 3, 4, 5, 6]), 6)

    def test_edge_case_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(Find_Max_Length([1]), 1)
        self.assertEqual(Find_Max_Length(["a"]), 1)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(Find_Max_Length([-1, -2, -3]), 3)

    def test_corner_case_mixed_types(self):
        self.assertEqual(Find_Max_Length([1, "two", 3]), 3)
        self.assertEqual(Find_Max_Length(["one", 2, 3]), 3)
