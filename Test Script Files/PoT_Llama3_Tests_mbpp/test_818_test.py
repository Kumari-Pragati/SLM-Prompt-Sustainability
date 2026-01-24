import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lower_ctr("hello"), 2)

    def test_edge_case(self):
        self.assertEqual(lower_ctr("HELLO"), 0)

    def test_boundary_case(self):
        self.assertEqual(lower_ctr("HelloWorld"), 3)

    def test_corner_case(self):
        self.assertEqual(lower_ctr("ABC123"), 0)

    def test_tricky_case(self):
        self.assertEqual(lower_ctr("aBc"), 2)
