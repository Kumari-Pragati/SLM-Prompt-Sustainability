import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(odd_Num_Sum(5), 625)

    def test_edge_case_n_1(self):
        self.assertEqual(odd_Num_Sum(1), 0)

    def test_edge_case_n_2(self):
        self.assertEqual(odd_Num_Sum(2), 0)

    def test_edge_case_n_3(self):
        self.assertEqual(odd_Num_Sum(3), 1)

    def test_edge_case_n_4(self):
        self.assertEqual(odd_Num_Sum(4), 0)

    def test_edge_case_n_5(self):
        self.assertEqual(odd_Num_Sum(5), 625)

    def test_edge_case_n_10(self):
        self.assertEqual(odd_Num_Sum(10), 2500)

    def test_edge_case_n_20(self):
        self.assertEqual(odd_Num_Sum(20), 25000)

    def test_edge_case_n_100(self):
        self.assertEqual(odd_Num_Sum(100), 250000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum("a")
