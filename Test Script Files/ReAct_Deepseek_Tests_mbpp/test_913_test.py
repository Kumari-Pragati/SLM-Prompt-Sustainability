import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(end_num("Hello1"))
        self.assertTrue(end_num("123"))
        self.assertTrue(end_num("abc9"))

    def test_edge_cases(self):
        self.assertFalse(end_num(""))
        self.assertFalse(end_num("NoDigits"))
        self.assertFalse(end_num("12345678901"))

    def test_explicitly_handled_error_cases(self):
        self.assertFalse(end_num(None))
        self.assertFalse(end_num(123))
        self.assertFalse(end_num(["Hello", "123"]))
