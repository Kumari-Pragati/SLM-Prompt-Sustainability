import unittest
from mbpp_241_code import array_3d

class TestArray3d(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(array_3d(2, 3, 4), [[[ '*' for _ in range(3)] for _ in range(2)] for _ in range(4)])

    def test_edge_case_m(self):
        self.assertEqual(array_3d(1, 3, 4), [[[ '*' for _ in range(3)] for _ in range(1)] for _ in range(4)])

    def test_edge_case_n(self):
        self.assertEqual(array_3d(2, 1, 4), [[[ '*' for _ in range(1)] for _ in range(2)] for _ in range(4)])

    def test_edge_case_o(self):
        self.assertEqual(array_3d(2, 3, 1), [[[ '*' for _ in range(3)] for _ in range(2)] for _ in range(1)])

    def test_edge_case_m_n_o(self):
        self.assertEqual(array_3d(1, 1, 1), [[[ '*' for _ in range(1)] for _ in range(1)] for _ in range(1)])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            array_3d('a', 3, 4)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            array_3d(-1, 3, 4)
