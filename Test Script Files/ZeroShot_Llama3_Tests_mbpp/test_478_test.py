import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_remove_lowercase(self):
        self.assertEqual(remove_lowercase("Hello World"), "HW")
        self.assertEqual(remove_lowercase("hello world"), "HW")
        self.assertEqual(remove_lowercase("HELLO WORLD"), "HW")
        self.assertEqual(remove_lowercase("123 ABC"), "123 ABC")
        self.assertEqual(remove_lowercase("abc def"), "")
        self.assertEqual(remove_lowercase("ABC DEF"), "ABC DEF")
        self.assertEqual(remove_lowercase("abc def ghi"), "def ghi")
        self.assertEqual(remove_lowercase("ABC DEF GHI"), "DEF GHI")
        self.assertEqual(remove_lowercase("abc def ghi jkl"), "def ghi jkl")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL"), "DEF GHI JKL")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno"), "def ghi jkl mno")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL MNO"), "DEF GHI JKL MNO")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno pqr"), "def ghi jkl mno pqr")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL MNO PQR"), "DEF GHI JKL MNO PQR")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno pqr stu"), "def ghi jkl mno pqr stu")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL MNO PQR STU"), "DEF GHI JKL MNO PQR STU")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno pqr stu vwx"), "def ghi jkl mno pqr stu vwx")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL MNO PQR STU VWX"), "DEF GHI JKL MNO PQR STU VWX")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno pqr stu vwx yz"), "def ghi jkl mno pqr stu vwx yz")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL MNO PQR STU VWX YZ"), "DEF GHI JKL MNO PQR STU VWX YZ")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno pqr stu vwx yz abc"), "def ghi jkl mno pqr stu vwx yz")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL MNO PQR STU VWX YZ ABC"), "DEF GHI JKL MNO PQR STU VWX YZ")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno pqr stu vwx yz abc def"), "def ghi jkl mno pqr stu vwx yz")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL MNO PQR STU VWX YZ ABC DEF"), "DEF GHI JKL MNO PQR STU VWX YZ")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno pqr stu vwx yz abc def ghi"), "def ghi jkl mno pqr stu vwx yz")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL MNO PQR STU VWX YZ ABC DEF GHI"), "DEF GHI JKL MNO PQR STU VWX YZ")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno pqr stu vwx yz abc def ghi jkl"), "def ghi jkl mno pqr stu vwx yz")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL MNO PQR STU VWX YZ ABC DEF GHI JKL"), "DEF GHI JKL MNO PQR STU VWX YZ")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno pqr stu vwx yz abc def ghi jkl mno"), "def ghi jkl mno pqr stu vwx yz")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL MNO PQR STU VWX YZ ABC DEF GHI JKL MNO"), "DEF GHI JKL MNO PQR STU VWX YZ")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno pqr stu vwx yz abc def ghi jkl mno pqr"), "def ghi jkl mno pqr stu vwx yz")
        self.assertEqual(remove_lowercase("ABC DEF GHI JKL MNO PQR STU VWX YZ ABC DEF GHI JKL MNO PQR"), "DEF GHI JKL MNO PQR STU VWX YZ")
        self.assertEqual(remove_lowercase("abc def ghi jkl mno pqr stu vwx yz abc def ghi jkl mno pqr stu"), "def ghi jkl m