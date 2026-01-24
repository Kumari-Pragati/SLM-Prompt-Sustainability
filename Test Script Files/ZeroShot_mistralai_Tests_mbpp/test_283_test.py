import unittest
from mbpp_283_code import validate

class TestValidate(unittest.TestCase):

    def test_validate_zero(self):
        self.assertTrue(validate(0))

    def test_validate_one(self):
        self.assertTrue(validate(1))
        self.assertTrue(validate(10))
        self.assertTrue(validate(100))
        self.assertTrue(validate(1000))
        self.assertTrue(validate(10000))

    def test_validate_two(self):
        self.assertFalse(validate(2))
        self.assertFalse(validate(20))
        self.assertFalse(validate(200))
        self.assertFalse(validate(2000))
        self.assertFalse(validate(20000))

    def test_validate_three(self):
        self.assertFalse(validate(3))
        self.assertFalse(validate(30))
        self.assertFalse(validate(300))
        self.assertFalse(validate(3000))
        self.assertFalse(validate(30000))

    def test_validate_four(self):
        self.assertFalse(validate(4))
        self.assertFalse(validate(40))
        self.assertFalse(validate(400))
        self.assertFalse(validate(4000))
        self.assertFalse(validate(40000))

    def test_validate_five(self):
        self.assertFalse(validate(5))
        self.assertFalse(validate(50))
        self.assertFalse(validate(500))
        self.assertFalse(validate(5000))
        self.assertFalse(validate(50000))

    def test_validate_six(self):
        self.assertFalse(validate(6))
        self.assertFalse(validate(60))
        self.assertFalse(validate(600))
        self.assertFalse(validate(6000))
        self.assertFalse(validate(60000))

    def test_validate_seven(self):
        self.assertFalse(validate(7))
        self.assertFalse(validate(70))
        self.assertFalse(validate(700))
        self.assertFalse(validate(7000))
        self.assertFalse(validate(70000))

    def test_validate_eight(self):
        self.assertFalse(validate(8))
        self.assertFalse(validate(80))
        self.assertFalse(validate(800))
        self.assertFalse(validate(8000))
        self.assertFalse(validate(80000))

    def test_validate_nine(self):
        self.assertFalse(validate(9))
        self.assertFalse(validate(90))
        self.assertFalse(validate(900))
        self.assertFalse(validate(9000))
        self.assertFalse(validate(90000))
