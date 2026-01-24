import unittest
from501_code import num_comm_div, ngcd

class TestNumCommDiv(unittest.TestCase):

    def test_num_comm_div(self):
        self.assertEqual(num_comm_div(2, 4), 2)
        self.assertEqual(num_comm_div(6, 8), 2)
        self.assertEqual(num_comm_div(9, 36), 2)
        self.assertEqual(num_comm_div(10, 15), 2)
        self.assertEqual(num_comm_div(12, 18), 2)
        self.assertEqual(num_comm_div(20, 40), 2)
        self.assertEqual(num_comm_div(25, 125), 2)
        self.assertEqual(num_comm_div(36, 1296), 2)
        self.assertEqual(num_comm_div(49, 7849), 2)
        self.assertEqual(num_comm_div(100, 10000), 2)

    def test_ngcd(self):
        self.assertEqual(ngcd(2, 4), 2)
        self.assertEqual(ngcd(6, 8), 2)
        self.assertEqual(ngcd(9, 36), 3)
        self.assertEqual(ngcd(10, 15), 5)
        self.assertEqual(ngcd(12, 18), 6)
        self.assertEqual(ngcd(20, 40), 4)
        self.assertEqual(ngcd(25, 125), 5)
        self.assertEqual(ngcd(36, 1296), 36)
        self.assertEqual(ngcd(49, 7849), 49)
        self.assertEqual(ngcd(100, 10000), 100)
