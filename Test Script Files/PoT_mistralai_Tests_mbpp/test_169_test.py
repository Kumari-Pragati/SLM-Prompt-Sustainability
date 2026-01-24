import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)

    def test_typical_cases(self):
        self.assertEqual(get_pell(3), 7)
        self.assertEqual(get_pell(4), 23)
        self.assertEqual(get_pell(5), 47)
        self.assertEqual(get_pell(6), 94)
        self.assertEqual(get_pell(7), 188)
        self.assertEqual(get_pell(8), 341)
        self.assertEqual(get_pell(9), 610)
        self.assertEqual(get_pell(10), 1099)

    def test_edge_cases(self):
        self.assertEqual(get_pell(0), None)
        self.assertEqual(get_pell(-1), None)
        self.assertEqual(get_pell(11), 2039)
        self.assertEqual(get_pell(12), 3779)
        self.assertEqual(get_pell(13), 7168)
        self.assertEqual(get_pell(14), 13095)
        self.assertEqual(get_pell(15), 23866)
        self.assertEqual(get_pell(16), 42283)
        self.assertEqual(get_pell(17), 74340)
        self.assertEqual(get_pell(18), 130499)
        self.assertEqual(get_pell(19), 221782)
        self.assertEqual(get_pell(20), 382589)
