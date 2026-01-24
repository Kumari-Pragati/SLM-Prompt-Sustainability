import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_Index(1), 3)
        self.assertEqual(find_Index(2), 5)
        self.assertEqual(find_Index(3), 7)

    def test_edge_cases(self):
        self.assertEqual(find_Index(-1), None)
        self.assertEqual(find_Index(0), None)
        self.assertEqual(find_Index(4), 8)

    def test_invalid_inputs(self):
        with self.assertRaises(OverflowError):
            find_Index(5)

    def test_rounding(self):
        self.assertEqual(find_Index(1.5), 5)
