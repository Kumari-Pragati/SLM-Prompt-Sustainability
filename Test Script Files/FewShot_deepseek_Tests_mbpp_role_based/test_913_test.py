import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(end_num("Hello1"))

    def test_edge_condition(self):
        self.assertTrue(end_num("1"))

    def test_boundary_condition(self):
        self.assertFalse(end_num("Hello"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            end_num(123)
