import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(upper_ctr('HelloWorld'), 2)

    def test_edge_case(self):
        self.assertEqual(upper_ctr(''), 0)
        self.assertEqual(upper_ctr('a'), 0)
        self.assertEqual(upper_ctr('A'), 1)
        self.assertEqual(upper_ctr('1234567890'), 0)
        self.assertEqual(upper_ctr('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)

    def test_corner_case(self):
        self.assertEqual(upper_ctr('ABCabc123'), 2)
        self.assertEqual(upper_ctr('ABCabc!@#'), 2)
        self.assertEqual(upper_ctr('ABCabc?<>:;'), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            upper_ctr(123)
        with self.assertRaises(TypeError):
            upper_ctr(None)
        with self.assertRaises(TypeError):
            upper_ctr(['a', 'b', 'c'])
