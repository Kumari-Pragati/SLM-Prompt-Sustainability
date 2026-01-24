import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):

    def test_get_pell_1(self):
        self.assertEqual(get_pell(1), 1)

    def test_get_pell_2(self):
        self.assertEqual(get_pell(2), 2)

    def test_get_pell_3(self):
        self.assertEqual(get_pell(3), 2)

    def test_get_pell_4(self):
        self.assertEqual(get_pell(4), 5)

    def test_get_pell_5(self):
        self.assertEqual(get_pell(5), 7)

    def test_get_pell_6(self):
        self.assertEqual(get_pell(6), 12)

    def test_get_pell_7(self):
        self.assertEqual(get_pell(7), 17)

    def test_get_pell_8(self):
        self.assertEqual(get_pell(8), 29)

    def test_get_pell_9(self):
        self.assertEqual(get_pell(9), 47)

    def test_get_pell_10(self):
        self.assertEqual(get_pell(10), 77)
