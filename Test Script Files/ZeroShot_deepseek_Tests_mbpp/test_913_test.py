import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):

    def test_end_num_positive(self):
        self.assertTrue(end_num("Hello1"))
        self.assertTrue(end_num("123"))
        self.assertTrue(end_num("abc456"))

    def test_end_num_negative(self):
        self.assertFalse(end_num("Hello"))
        self.assertFalse(end_num("123abc"))
        self.assertFalse(end_num(""))
