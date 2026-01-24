import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):

    def test_get_pell_typical_cases(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(5), 10)
        self.assertEqual(get_pell(10), 144)

    def test_get_pell_edge_cases(self):
        self.assertEqual(get_pell(0), 0)
        self.assertEqual(get_pell(-1), None)
        self.assertEqual(get_pell(30), 10747055048768)

    def test_get_pell_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_pell('a')
        with self.assertRaises(TypeError):
            get_pell(None)
        with self.assertRaises(TypeError):
            get_pell([])
