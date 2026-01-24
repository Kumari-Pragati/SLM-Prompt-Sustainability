import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(move_num('hello123world'), 'helloworld123')

    def test_edge1(self):
        self.assertEqual(move_num('123hello'), '123hello')

    def test_edge2(self):
        self.assertEqual(move_num('hello123'), 'hello123')

    def test_edge3(self):
        self.assertEqual(move_num(''), '')

    def test_edge4(self):
        self.assertEqual(move_num('123'), '123')

    def test_edge5(self):
        self.assertEqual(move_num('hello'), 'hello')

    def test_edge6(self):
        self.assertEqual(move_num('123456'), '123456')

    def test_edge7(self):
        self.assertEqual(move_num('abcdefg'), 'abcdefg')

    def test_edge8(self):
        self.assertEqual(move_num('123abc'), '123abc')

    def test_edge9(self):
        self.assertEqual(move_num('hello123abc'), 'hello123abc')

    def test_edge10(self):
        self.assertEqual(move_num('123456abc'), '123456abc')

    def test_edge11(self):
        self.assertEqual(move_num('hello'), 'hello')

    def test_edge12(self):
        self.assertEqual(move_num('123'), '123')

    def test_edge13(self):
        self.assertEqual(move_num(''), '')

    def test_edge14(self):
        self.assertEqual(move_num('abc'), 'abc')

    def test_edge15(self):
        self.assertEqual(move_num('123abc'), '123abc')

    def test_edge16(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_edge17(self):
        self.assertEqual(move_num('123456'), '123456')

    def test_edge18(self):
        self.assertEqual(move_num('abc'), 'abc')

    def test_edge19(self):
        self.assertEqual(move_num('123abc'), '123abc')

    def test_edge20(self):
        self.assertEqual(move_num('123456abc'), '123456abc')

    def test_edge21(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_edge22(self):
        self.assertEqual(move_num('123abc'), '123abc')

    def test_edge23(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_edge24(self):
        self.assertEqual(move_num('123456'), '123456')

    def test_edge25(self):
        self.assertEqual(move_num('abc'), 'abc')

    def test_edge26(self):
        self.assertEqual(move_num('123abc'), '123abc')

    def test_edge27(self):
        self.assertEqual(move_num('123456abc'), '123456abc')

    def test_edge28(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_edge29(self):
        self.assertEqual(move_num('123abc'), '123abc')

    def test_edge30(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_edge31(self):
        self.assertEqual(move_num('123456'), '123456')

    def test_edge32(self):
        self.assertEqual(move_num('abc'), 'abc')

    def test_edge33(self):
        self.assertEqual(move_num('123abc'), '123abc')

    def test_edge34(self):
        self.assertEqual(move_num('123456abc'), '123456abc')

    def test_edge35(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_edge36(self):
        self.assertEqual(move_num('123abc'), '123abc')

    def test_edge37(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_edge38(self):
        self.assertEqual(move_num('123456'), '123456')

    def test_edge39(self):
        self.assertEqual(move_num('abc'), 'abc')

    def test_edge40(self):
        self.assertEqual(move_num('123abc'), '123abc')

    def test_edge41(self):
        self.assertEqual(move_num('123456abc'), '123456abc')

    def test_edge42(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_edge43(self):
        self.assertEqual(move_num('123abc'), '123abc')

    def test_edge44(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_edge45(self):
        self.assertEqual(move_num('123456'), '123456')

    def test_edge46(self):
        self.assertEqual(move_num('abc'), 'abc')

    def test_edge47(self):
        self.assertEqual(move_num('123abc'), '123abc')

    def test_edge48(self):
        self.assertEqual(move_num('123456abc'), '123456abc')

    def test_edge49(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_edge50(self):
        self.assertEqual(move_num('123abc'), '123abc')