import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Index(1), 3)
        self.assertEqual(find_Index(2), 10)

    def test_edge_conditions(self):
        self.assertEqual(find_Index(0), 3)
        self.assertEqual(find_Index(-1), 3)
        self.assertEqual(find_Index(100), 141)

    def test_complex_cases(self):
        self.assertEqual(find_Index(1.5), 5)
        self.assertEqual(find_Index(2.5), 14)
