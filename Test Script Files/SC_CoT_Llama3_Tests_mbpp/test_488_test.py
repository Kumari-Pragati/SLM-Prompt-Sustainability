import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):
    def test_typical_input(self):
        self.assertAlmostEqual(area_pentagon(5), 12.5)

    def test_edge_case_zero(self):
        self.assertAlmostEqual(area_pentagon(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(-5)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            area_pentagon('five')

    def test_edge_case_zero_input(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_input2(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0.0)

    def test_edge_case_zero_input3(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0.0001)

    def test_edge_case_zero_input4(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(-0.0001)

    def test_edge_case_zero_input5(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0.00001)

    def test_edge_case_zero_input6(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(-0.00001)

    def test_edge_case_zero_input7(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0.000001)

    def test_edge_case_zero_input8(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(-0.000001)

    def test_edge_case_zero_input9(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0.0000001)

    def test_edge_case_zero_input10(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(-0.0000001)

    def test_edge_case_zero_input11(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0.00000001)

    def test_edge_case_zero_input12(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(-0.00000001)

    def test_edge_case_zero_input13(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0.000000001)

    def test_edge_case_zero_input14(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(-0.000000001)

    def test_edge_case_zero_input15(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0.0000000001)

    def test_edge_case_zero_input16(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(-0.0000000001)

    def test_edge_case_zero_input17(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0.00000000001)

    def test_edge_case_zero_input18(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(-0.00000000001)

    def test_edge_case_zero_input19(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0.000000000001)

    def test_edge_case_zero_input20(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(-0.000000000001)
