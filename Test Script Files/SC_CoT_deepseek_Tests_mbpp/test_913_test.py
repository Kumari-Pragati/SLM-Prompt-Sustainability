import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(end_num('Hello1'))
        self.assertTrue(end_num('123'))
        self.assertTrue(end_num('abc9'))

    def test_edge_cases(self):
        self.assertTrue(end_num('9'))
        self.assertTrue(end_num(''))

    def test_boundary_cases(self):
        self.assertFalse(end_num('Hello'))
        self.assertFalse(end_num('1234'))
        self.assertFalse(end_num('abc'))

    def test_invalid_inputs(self):
        self.assertFalse(end_num(123))
        self.assertFalse(end_num(None))
        self.assertFalse(end_num(True))
        self.assertFalse(end_num(False))
        self.assertFalse(end_num(['Hello', '123']))
        self.assertFalse(end_num({'key': 'value'}))
