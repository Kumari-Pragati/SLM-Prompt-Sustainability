import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(does_Contain_B(1, 2, 1))

    def test_edge_case_a_equals_b(self):
        self.assertTrue(does_Contain_B(1, 1, 1))

    def test_edge_case_b_minus_a_equals_zero(self):
        self.assertFalse(does_Contain_B(1, 1, 0))

    def test_edge_case_c_equals_zero(self):
        self.assertFalse(does_Contain_B(1, 2, 0))

    def test_edge_case_negative_values(self):
        self.assertFalse(does_Contain_B(-1, 0, 1))

    def test_explicitly_handled_error_case_c_greater_than_b_minus_a(self):
        self.assertFalse(does_Contain_B(1, 2, 3))

    def test_explicitly_handled_error_case_c_less_than_b_minus_a(self):
        self.assertFalse(does_Contain_B(2, 3, 4))
