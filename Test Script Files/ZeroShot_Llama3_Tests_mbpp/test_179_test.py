import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):

    def test_is_num_keith_true(self):
        self.assertTrue(is_num_keith(123))

    def test_is_num_keith_false(self):
        self.assertFalse(is_num_keith(123456))

    def test_is_num_keith_edge_case(self):
        self.assertTrue(is_num_keith(1))

    def test_is_num_keith_edge_case2(self):
        self.assertFalse(is_num_keith(0))

    def test_is_num_keith_edge_case3(self):
        self.assertFalse(is_num_keith(123456789))

    def test_is_num_keith_edge_case4(self):
        self.assertTrue(is_num_keith(1234567890))

    def test_is_num_keith_edge_case5(self):
        self.assertFalse(is_num_keith(123456789012))
