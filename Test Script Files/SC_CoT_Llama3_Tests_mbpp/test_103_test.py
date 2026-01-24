import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(eulerian_num(5, 3), 10)

    def test_edge_case_n_zero(self):
        self.assertEqual(eulerian_num(0, 3), 0)

    def test_edge_case_m_zero(self):
        self.assertEqual(eulerian_num(5, 0), 1)

    def test_edge_case_m_greater_than_n(self):
        self.assertEqual(eulerian_num(3, 5), 0)

    def test_recursive_call(self):
        self.assertEqual(eulerian_num(4, 2), 5)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            eulerian_num('a', 3)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            eulerian_num(-1, 3)
