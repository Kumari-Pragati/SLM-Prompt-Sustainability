import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):
    def test_typical_use_case(self):
        ar = [1, 2, 3, 5, 6, 7, 8, 9, 10]
        self.assertEqual(find_missing(ar, 10), 4)

    def test_edge_case(self):
        ar = [1, 2, 3, 4, 5]
        self.assertEqual(find_missing(ar, 5), 6)

    def test_edge_case2(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(find_missing(ar, 12), 13)

    def test_invalid_input(self):
        ar = [1, 2, 3]
        with self.assertRaises(TypeError):
            find_missing(ar, "invalid")
