import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):

    def test_lobb_num(self):
        self.assertEqual(lobb_num(1, 1), 1)
        self.assertEqual(lobb_num(2, 1), 3)
        self.assertEqual(lobb_num(3, 1), 5)
        self.assertEqual(lobb_num(4, 1), 7)
        self.assertEqual(lobb_num(5, 1), 9)
        self.assertEqual(lobb_num(1, 2), 2)
        self.assertEqual(lobb_num(2, 2), 4)
        self.assertEqual(lobb_num(3, 2), 6)
        self.assertEqual(lobb_num(4, 2), 8)
        self.assertEqual(lobb_num(5, 2), 10)
        self.assertEqual(lobb_num(1, 3), 3)
        self.assertEqual(lobb_num(2, 3), 5)
        self.assertEqual(lobb_num(3, 3), 7)
        self.assertEqual(lobb_num(4, 3), 9)
        self.assertEqual(lobb_num(5, 3), 11)
        self.assertEqual(lobb_num(1, 4), 4)
        self.assertEqual(lobb_num(2, 4), 6)
        self.assertEqual(lobb_num(3, 4), 8)
        self.assertEqual(lobb_num(4, 4), 10)
        self.assertEqual(lobb_num(5, 4), 12)
        self.assertEqual(lobb_num(1, 5), 5)
        self.assertEqual(lobb_num(2, 5), 7)
        self.assertEqual(lobb_num(3, 5), 9)
        self.assertEqual(lobb_num(4, 5), 11)
        self.assertEqual(lobb_num(5, 5), 13)
