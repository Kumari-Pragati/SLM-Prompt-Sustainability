import unittest
from mbpp_812_code import road_rd

class TestRoadRdFunction(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(road_rd("123 Main Road"), "123 Main Rd.")
        self.assertEqual(road_rd("456 Elm Road"), "456 Elm Rd.")
        self.assertEqual(road_rd("789 Oak Road"), "789 Oak Rd.")

    def test_edge_cases(self):
        self.assertEqual(road_rd("123 Main Roadway"), "123 Main Rdway")
        self.assertEqual(road_rd("456 Elm Driveway"), "456 Elm Drivway")
        self.assertEqual(road_rd("789 Oak Boulevard"), "789 Oak Blvd")

    def test_boundary_cases(self):
        self.assertEqual(road_rd("123 Main Roadway"), "123 Main Rdway")
        self.assertEqual(road_rd("456 Elm Driveway"), "456 Elm Drivway")
        self.assertEqual(road_rd("789 Oak Boulevard"), "789 Oak Blvd")

    def test_special_cases(self):
        self.assertEqual(road_rd("123 Main Roadway"), "123 Main Rdway")
        self.assertEqual(road_rd("456 Elm Driveway"), "456 Elm Drivway")
        self.assertEqual(road_rd("789 Oak Boulevard"), "789 Oak Blvd")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            road_rd(123)
