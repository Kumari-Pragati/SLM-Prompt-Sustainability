import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):
    def test_get_pell_typical(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(3), 2)
        self.assertEqual(get_pell(4), 3)
        self.assertEqual(get_pell(5), 5)
        self.assertEqual(get_pell(6), 7)
        self.assertEqual(get_pell(7), 11)
        self.assertEqual(get_pell(8), 13)
        self.assertEqual(get_pell(9), 17)

    def test_get_pell_edge_cases(self):
        self.assertEqual(get_pell(0), 0)
        self.assertEqual(get_pell(10), 31)
        self.assertEqual(get_pell(11), 37)
        self.assertEqual(get_pell(12), 49)
        self.assertEqual(get_pell(13), 61)
        self.assertEqual(get_pell(14), 77)
        self.assertEqual(get_pell(15), 95)
        self.assertEqual(get_pell(16), 113)
        self.assertEqual(get_pell(17), 133)
        self.assertEqual(get_pell(18), 157)
        self.assertEqual(get_pell(19), 181)
        self.assertEqual(get_pell(20), 205)
