import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(rectangle_area(5, 10), 50)

    def test_boundary_conditions(self):
        self.assertEqual(rectangle_area(0, 10), 0)
        self.assertEqual(rectangle_area(5, 0), 0)
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rectangle_area("5", 10)
        with self.assertRaises(TypeError):
            rectangle_area(5, "10")
        with self.assertRaises(TypeError):
            rectangle_area("5", "10")
