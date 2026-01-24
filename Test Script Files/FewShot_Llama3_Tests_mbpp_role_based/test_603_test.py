import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_case_n_1(self):
        self.assertEqual(get_ludic(1), [1])

    def test_edge_case_n_2(self):
        self.assertEqual(get_ludic(2), [1, 2])

    def test_edge_case_n_3(self):
        self.assertEqual(get_ludic(3), [1, 2, 3])

    def test_edge_case_n_4(self):
        self.assertEqual(get_ludic(4), [1, 2, 3, 4])

    def test_edge_case_n_5(self):
        self.assertEqual(get_ludic(5), [1, 2, 3, 4, 5])

    def test_edge_case_n_10(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_case_n_20(self):
        self.assertEqual(get_ludic(20), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            get_ludic("string")
