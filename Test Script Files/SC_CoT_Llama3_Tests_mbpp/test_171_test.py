import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(perimeter_pentagon(5), 25)

    def test_edge_case_zero(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon(0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon(-5)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon('five')

    def test_edge_case_string(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon('abc')

    def test_edge_case_list(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon([1, 2, 3])

    def test_edge_case_dict(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon({'a': 1, 'b': 2})

    def test_edge_case_tuple(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon((1, 2, 3))

    def test_edge_case_set(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon({1, 2, 3})

    def test_edge_case_complex(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon(5+3j)

    def test_edge_case_floating_point(self):
        self.assertEqual(perimeter_pentagon(5.5), 27.5)

    def test_edge_case_large_number(self):
        self.assertEqual(perimeter_pentagon(1000), 5000)
