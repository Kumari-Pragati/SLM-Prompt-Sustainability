import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Index(1), 3)
        self.assertEqual(find_Index(2), 14)
        self.assertEqual(find_Index(3), 45)
        self.assertEqual(find_Index(4), 142)

    def test_edge_cases(self):
        self.assertEqual(find_Index(0), 2)
        self.assertEqual(find_Index(5), 5142)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(ValueError):
            find_Index(-1)
        with self.assertRaises(ValueError):
            find_Index(0)
