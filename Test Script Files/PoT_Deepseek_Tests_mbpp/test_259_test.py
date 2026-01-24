import unittest
from mbpp_259_code import maximize_elements

class TestMaximizeElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximize_elements((1, 2, 3), (4, 5, 6)), ((4, 5, 6)))

    def test_edge_case(self):
        self.assertEqual(maximize_elements((10, 20, 30), (10, 20, 30)), ((10, 20, 30)))

    def test_boundary_case(self):
        self.assertEqual(maximize_elements((-100, 0, 100), (100, 0, -100)), ((100, 0, 100)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            maximize_elements((1, 2, 3), "not a tuple")
