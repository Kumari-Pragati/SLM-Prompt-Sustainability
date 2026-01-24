import unittest
from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_convert_typical(self):
        self.assertEqual(convert([1, 2, 3]), 123)

    def test_convert_edge(self):
        self.assertEqual(convert([0, 1, 2]), 012)

    def test_convert_edge2(self):
        self.assertEqual(convert([-1, 2, 3]), -123)

    def test_convert_edge3(self):
        self.assertEqual(convert([1, 0, 2]), 102)

    def test_convert_edge4(self):
        self.assertEqual(convert([1, 2, 0]), 120)

    def test_convert_edge5(self):
        self.assertEqual(convert([0, 0, 0]), 000)

    def test_convert_edge6(self):
        self.assertEqual(convert([1, 1, 1]), 111)

    def test_convert_edge7(self):
        self.assertEqual(convert([9, 9, 9]), 999)

    def test_convert_edge8(self):
        self.assertEqual(convert([1, 2, 3, 4, 5]), 12345)

    def test_convert_edge9(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6]), 123456)

    def test_convert_edge10(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7]), 1234567)

    def test_convert_edge11(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8]), 12345678)

    def test_convert_edge12(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9]), 123456789)

    def test_convert_edge13(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 1234567890)

    def test_convert_edge14(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]), 12345678901)

    def test_convert_edge15(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]), 123456789012)

    def test_convert_edge16(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3]), 1234567890123)

    def test_convert_edge17(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]), 12345678901234)

    def test_convert_edge18(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]), 123456789012345)

    def test_convert_edge19(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6]), 1234567890123456)

    def test_convert_edge20(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7]), 12345678901234567)

    def test_convert_edge21(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8]), 123456789012345678)

    def test_convert_edge22(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 1234567890123456789)