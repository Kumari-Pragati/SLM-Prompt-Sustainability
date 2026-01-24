import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):
    def test_typical(self):
        self.assertTrue(check_type((1, 2, 3)))

    def test_edge(self):
        self.assertFalse(check_type((1, 2, '3')))

    def test_edge2(self):
        self.assertFalse(check_type((1, 2, 3.0)))

    def test_edge3(self):
        self.assertFalse(check_type((1, 2, [3])))

    def test_edge4(self):
        self.assertFalse(check_type((1, 2, {'3'})))

    def test_edge5(self):
        self.assertFalse(check_type((1, 2, (3,))))

    def test_edge6(self):
        self.assertFalse(check_type((1, 2, {'a': 3})))

    def test_edge7(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4})))

    def test_edge8(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5})))

    def test_edge9(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5, 'd': 6})))

    def test_edge10(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7})))

    def test_edge11(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8})))

    def test_edge12(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9})))

    def test_edge13(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10})))

    def test_edge14(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11})))

    def test_edge15(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11, 'j': 12})))

    def test_edge16(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11, 'j': 12, 'k': 13})))

    def test_edge17(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14})))

    def test_edge18(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14,'m': 15})))

    def test_edge19(self):
        self.assertFalse(check_type((1, 2, {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11, 'j': 12, 'k':