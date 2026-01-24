import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_count_Fac_1(self):
        self.assertEqual(count_Fac(1), 0)

    def test_count_Fac_2(self):
        self.assertEqual(count_Fac(2), 1)

    def test_count_Fac_3(self):
        self.assertEqual(count_Fac(3), 1)

    def test_count_Fac_4(self):
        self.assertEqual(count_Fac(4), 2)

    def test_count_Fac_5(self):
        self.assertEqual(count_Fac(5), 2)

    def test_count_Fac_6(self):
        self.assertEqual(count_Fac(6), 2)

    def test_count_Fac_7(self):
        self.assertEqual(count_Fac(7), 2)

    def test_count_Fac_8(self):
        self.assertEqual(count_Fac(8), 3)

    def test_count_Fac_9(self):
        self.assertEqual(count_Fac(9), 2)

    def test_count_Fac_10(self):
        self.assertEqual(count_Fac(10), 2)

    def test_count_Fac_11(self):
        self.assertEqual(count_Fac(11), 2)

    def test_count_Fac_12(self):
        self.assertEqual(count_Fac(12), 3)

    def test_count_Fac_13(self):
        self.assertEqual(count_Fac(13), 2)

    def test_count_Fac_14(self):
        self.assertEqual(count_Fac(14), 3)

    def test_count_Fac_15(self):
        self.assertEqual(count_Fac(15), 3)
