import unittest
from mbpp_126_code import sum

class TestSumFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum(12, 18), 6)

    def test_typical_case_2(self):
        self.assertEqual(sum(25, 50), 10)

    def test_boundary_case_1(self):
        self.assertEqual(sum(1, 1), 1)

    def test_boundary_case_2(self):
        self.assertEqual(sum(0, 0), 0)

    def test_edge_case_1(self):
        self.assertEqual(sum(100, 200), 10)

    def test_edge_case_2(self):
        self.assertEqual(sum(300, 400), 10)

    def test_edge_case_3(self):
        self.assertEqual(sum(500, 500), 50)

    def test_error_case_1(self):
        with self.assertRaises(TypeError):
            sum("12", 18)

    def test_error_case_2(self):
        with self.assertRaises(TypeError):
            sum(12, "18")

    def test_error_case_3(self):
        with self.assertRaises(TypeError):
            sum("12", "18")
