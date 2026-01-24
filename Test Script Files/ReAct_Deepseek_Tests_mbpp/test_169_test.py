import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(5), 10)
        self.assertEqual(get_pell(10), 34)

    def test_edge_cases(self):
        self.assertEqual(get_pell(0), 0)
        self.assertEqual(get_pell(-1), None)
        self.assertEqual(get_pell(30), 1074)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            get_pell('a')
        with self.assertRaises(TypeError):
            get_pell(None)
