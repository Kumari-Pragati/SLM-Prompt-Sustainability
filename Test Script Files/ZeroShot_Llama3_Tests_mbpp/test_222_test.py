import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):
    def test_check_type(self):
        self.assertTrue(check_type((1, 1, 1)))
        self.assertFalse(check_type((1, '1', 1.0)))
        self.assertFalse(check_type((1, 1, '1')))
        self.assertFalse(check_type((1, 1, 1, '1')))
        self.assertTrue(check_type((1, 1, 1, 1)))
        self.assertFalse(check_type((1, 1, 1, 1.0)))
        self.assertFalse(check_type((1, 1, 1.0, 1)))
        self.assertFalse(check_type((1, 1, 1, 1.0, '1')))
        self.assertFalse(check_type((1, 1, 1, 1.0, 1)))
        self.assertFalse(check_type((1, 1, 1, 1.0, 1.0)))
        self.assertFalse(check_type((1, 1, 1, 1.0, 1.0, '1')))
