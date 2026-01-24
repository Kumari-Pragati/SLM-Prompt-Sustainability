import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Isomorphic("egg", "add"))

    def test_edge_case(self):
        self.assertTrue(is_Isomorphic("foo", "bar"))

    def test_edge_case2(self):
        self.assertFalse(is_Isomorphic("foo", "foo"))

    def test_edge_case3(self):
        self.assertFalse(is_Isomorphic("egg", "egg"))

    def test_edge_case4(self):
        self.assertFalse(is_Isomorphic("egg", "adda"))

    def test_edge_case5(self):
        self.assertFalse(is_Isomorphic("egg", "addx"))

    def test_edge_case6(self):
        self.assertFalse(is_Isomorphic("egg", "add"))

    def test_edge_case7(self):
        self.assertFalse(is_Isomorphic("egg", "add"))

    def test_edge_case8(self):
        self.assertFalse(is_Isomorphic("egg", "add"))
