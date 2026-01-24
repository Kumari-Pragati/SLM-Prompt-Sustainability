import unittest
from mbpp_252_code import convert

class TestConvert(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(convert([1, 2, 3]), ([1.0, 0.0, 3.14159265359]))

    def test_edge(self):
        self.assertEqual(convert([0, 0, 0]), ([0.0, 0.0, 0.0]))

    def test_edge2(self):
        self.assertEqual(convert([1, 1, 1]), ([1.0, 0.0, 3.14159265359]))

    def test_edge3(self):
        self.assertEqual(convert([1j, 1j, 1j]), ([1.0, 0.0, 3.14159265359]))

    def test_edge4(self):
        self.assertEqual(convert([1, 2j, 3j]), ([1.0, 0.0, 3.14159265359]))

    def test_edge5(self):
        self.assertEqual(convert([1, 2, 3j]), ([1.0, 0.0, 3.14159265359]))

    def test_edge6(self):
        self.assertEqual(convert([1j, 2, 3j]), ([1.0, 0.0, 3.14159265359]))

    def test_edge7(self):
        self.assertEqual(convert([1j, 2j, 3j]), ([1.0, 0.0, 3.14159265359]))

    def test_edge8(self):
        self.assertEqual(convert([1, 2j, 3j, 4j]), ([1.0, 0.0, 3.14159265359]))

    def test_edge9(self):
        self.assertEqual(convert([1j, 2, 3, 4j]), ([1.0, 0.0, 3.14159265359]))

    def test_edge10(self):
        self.assertEqual(convert([1j, 2j, 3, 4j]), ([1.0, 0.0, 3.14159265359]))
