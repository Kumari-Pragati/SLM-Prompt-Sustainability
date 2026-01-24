import unittest
from mbpp_673_code import convert

class TestConvert(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(convert([1, 2, 3]), 123)

    def test_edge(self):
        self.assertEqual(convert([0]), 0)
        self.assertEqual(convert([10]), 10)
        self.assertEqual(convert([100]), 100)

    def test_edge2(self):
        self.assertEqual(convert([-1, 2, 3]), -123)
        self.assertEqual(convert([1, -2, 3]), -23)
        self.assertEqual(convert([-1, -2, -3]), -123)

    def test_edge3(self):
        self.assertEqual(convert([1, 2, 3, 4, 5]), 12345)
        self.assertEqual(convert([1, 2, 3, 4, 5, 6]), 123456)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            convert("abc")
