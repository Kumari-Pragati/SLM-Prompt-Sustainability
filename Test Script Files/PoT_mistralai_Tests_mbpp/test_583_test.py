import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):
    def test_catalan_number_0(self):
        self.assertEqual(catalan_number(0), 1)

    def test_catalan_number_1(self):
        self.assertEqual(catalan_number(1), 1)

    def test_catalan_number_2(self):
        self.assertEqual(catalan_number(2), 2)

    def test_catalan_number_3(self):
        self.assertEqual(catalan_number(3), 5)

    def test_catalan_number_4(self):
        self.assertEqual(catalan_number(4), 14)

    def test_catalan_number_5(self):
        self.assertEqual(catalan_number(5), 42)

    def test_catalan_number_large(self):
        self.assertEqual(catalan_number(100), 30645693)
