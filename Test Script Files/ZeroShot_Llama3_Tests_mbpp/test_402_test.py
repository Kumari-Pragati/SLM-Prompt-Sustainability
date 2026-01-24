import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):

    def test_ncr_modp(self):
        self.assertEqual(ncr_modp(5, 2, 7), 6)
        self.assertEqual(ncr_modp(10, 3, 11), 4)
        self.assertEqual(ncr_modp(20, 10, 13), 123)
        self.assertEqual(ncr_modp(25, 15, 17), 4368)
        self.assertEqual(ncr_modp(30, 20, 23), 15504)
        self.assertEqual(ncr_modp(40, 25, 29), 1425064)
        self.assertEqual(ncr_modp(50, 30, 31), 1964180)
        self.assertEqual(ncr_modp(60, 35, 37), 65574704)
        self.assertEqual(ncr_modp(70, 40, 41), 37199306)
        self.assertEqual(ncr_modp(80, 45, 43), 20922789848)
        self.assertEqual(ncr_modp(90, 50, 47), 2432902008176640000)
        self.assertEqual(ncr_modp(100, 55, 53), 259896491197495106300515235)
        self.assertEqual(ncr_modp(100, 60, 59), 317811576351227795713827)
        self.assertEqual(ncr_modp(100, 65, 61), 103486560056655297516833)
        self.assertEqual(ncr_modp(100, 70, 67), 317811576351227795713827)
        self.assertEqual(ncr_modp(100, 75, 71), 317811576351227795713827)
        self.assertEqual(ncr_modp(100, 80, 73), 317811576351227795713827)
        self.assertEqual(ncr_modp(100, 85, 79), 317811576351227795713827)
        self.assertEqual(ncr_modp(100, 90, 83), 317811576351227795713827)
        self.assertEqual(ncr_modp(100, 95, 89), 317811576351227795713827)
        self.assertEqual(ncr_modp(100, 98, 97), 317811576351227795713827)
        self.assertEqual(ncr_modp(100, 99, 101), 1)
        self.assertEqual(ncr_modp(100, 100, 103), 1)
