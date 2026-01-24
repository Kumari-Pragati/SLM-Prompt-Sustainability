import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(move_num("Hello123World"), "Hello123World")

    def test_edge_case1(self):
        self.assertEqual(move_num("123abc"), "123abc")

    def test_edge_case2(self):
        self.assertEqual(move_num("abc123"), "abc123")

    def test_edge_case3(self):
        self.assertEqual(move_num("123"), "123")

    def test_edge_case4(self):
        self.assertEqual(move_num("abc"), "abc")

    def test_edge_case5(self):
        self.assertEqual(move_num(""), "")

    def test_edge_case6(self):
        self.assertEqual(move_num("123456"), "123456")

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            move_num(None)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            move_num("")
