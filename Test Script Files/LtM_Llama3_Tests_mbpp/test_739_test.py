import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_Index(1), 10)
        self.assertEqual(find_Index(2), 31.622776601683793)
        self.assertEqual(find_Index(3), 100)

    def test_edge_cases(self):
        self.assertEqual(find_Index(-1), 10)
        self.assertEqual(find_Index(0), 10)
        self.assertEqual(find_Index(4), 141.4213562373095)

    def test_invalid_inputs(self):
        with self.assertRaises(OverflowError):
            find_Index(5)
