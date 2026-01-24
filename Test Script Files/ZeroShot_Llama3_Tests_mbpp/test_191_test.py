import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthnumber(unittest.TestCase):

    def test_april(self):
        self.assertTrue(check_monthnumber("April"))

    def test_june(self):
        self.assertTrue(check_monthnumber("June"))

    def test_september(self):
        self.assertTrue(check_monthnumber("September"))

    def test_november(self):
        self.assertTrue(check_monthnumber("November"))

    def test_may(self):
        self.assertFalse(check_monthnumber("May"))

    def test_july(self):
        self.assertFalse(check_monthnumber("July"))

    def test_august(self):
        self.assertFalse(check_monthnumber("August"))

    def test_october(self):
        self.assertFalse(check_monthnumber("October"))

    def test_february(self):
        self.assertFalse(check_monthnumber("February"))
