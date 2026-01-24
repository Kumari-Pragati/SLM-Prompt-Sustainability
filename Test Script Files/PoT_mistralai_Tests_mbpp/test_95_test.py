import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Find_Min_Length([1, 2, 3, 4]), 1)
        self.assertEqual(Find_Min_Length(["a", "b", "c", "d"]), 3)
        self.assertEqual(Find_Min_Length([1, 1, 1, 1]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(Find_Min_Length([1]), 1)
        self.assertEqual(Find_Min_Length(["a"]), 1)

    def test_corner_case_mixed_types(self):
        self.assertEqual(Find_Min_Length([1, "a", 3]), 1)
        self.assertEqual(Find_Min_Length(["a", 1, "b"]), 2)
