import unittest
from752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):
    def test_jacobsthal_num_positive_integer(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 3)
        self.assertEqual(jacobsthal_num(3), 5)
        self.assertEqual(jacobsthal_num(4), 9)
        self.assertEqual(jacobsthal_num(5), 17)
        self.assertEqual(jacobsthal_num(6), 29)
        self.assertEqual(jacobsthal_num(7), 47)
        self.assertEqual(jacobsthal_num(8), 73)
        self.assertEqual(jacobsthal_num(9), 115)

    def test_jacobsthal_num_large_integer(self):
        self.assertEqual(jacobsthal_num(100), 16796337)
        self.assertEqual(jacobsthal_num(1000), 288016801)
        self.assertEqual(jacobsthal_num(10000), 5142292617)
        self.assertEqual(jacobsthal_num(100000), 93320575809)
        self.assertEqual(jacobsthal_num(1000000), 1703665833937)

    def test_jacobsthal_num_negative_integer(self):
        self.assertRaises(ValueError, jacobsthal_num, -1)

    def test_jacobsthal_num_zero_or_one(self):
        self.assertRaises(ValueError, jacobsthal_num, 0)
        self.assertRaises(ValueError, jacobsthal_num, 1)
