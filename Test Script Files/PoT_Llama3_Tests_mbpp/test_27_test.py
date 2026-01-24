import unittest
from mbpp_27_code import remove

class TestRemove(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(remove(['hello1', 'world2', 'python3']), ['hello', 'world', 'python'])

    def test_edge(self):
        self.assertEqual(remove(['hello', 'world', 'python']), ['hello', 'world', 'python'])

    def test_edge2(self):
        self.assertEqual(remove(['123456']), [])

    def test_edge3(self):
        self.assertEqual(remove(['hello123', 'world456']), ['hello', 'world'])

    def test_edge4(self):
        self.assertEqual(remove(['123hello', 'world456']), ['hello', 'world'])

    def test_edge5(self):
        self.assertEqual(remove(['hello', '123world', 'python456']), ['hello', 'world', 'python'])

    def test_edge6(self):
        self.assertEqual(remove(['123456789']), [])

    def test_edge7(self):
        self.assertEqual(remove(['1234567890']), [])

    def test_edge8(self):
        self.assertEqual(remove(['1234567890', 'hello']), ['hello'])

    def test_edge9(self):
        self.assertEqual(remove(['1234567890', 'world']), [])

    def test_edge10(self):
        self.assertEqual(remove(['1234567890', 'python']), [])

    def test_edge11(self):
        self.assertEqual(remove(['1234567890', 'hello', 'world', 'python']), [])

    def test_edge12(self):
        self.assertEqual(remove(['1234567890', 'hello', 'world', 'python', '123']), [])

    def test_edge13(self):
        self.assertEqual(remove(['1234567890', 'hello', 'world', 'python', '456']), [])

    def test_edge14(self):
        self.assertEqual(remove(['1234567890', 'hello', 'world', 'python', '789']), [])

    def test_edge15(self):
        self.assertEqual(remove(['1234567890', 'hello', 'world', 'python', '123456']), [])
