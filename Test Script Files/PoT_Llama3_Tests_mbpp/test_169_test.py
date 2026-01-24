import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_pell(3), 2)
        self.assertEqual(get_pell(4), 3)
        self.assertEqual(get_pell(5), 5)
        self.assertEqual(get_pell(6), 8)

    def test_edge_case(self):
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(1), 1)

    def test_boundary_case(self):
        self.assertEqual(get_pell(10), 55)
        self.assertEqual(get_pell(20), 177)
        self.assertEqual(get_pell(30), 610)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_pell("a")
