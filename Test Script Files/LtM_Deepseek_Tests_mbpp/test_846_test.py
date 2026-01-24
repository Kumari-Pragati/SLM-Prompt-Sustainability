import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_platform([900, 940], [910, 1000], 2), 1)

    def test_typical_case(self):
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1130, 1240], 3), 1)

    def test_edge_case_single_train(self):
        self.assertEqual(find_platform([900], [1000], 1), 1)

    def test_boundary_case_max_values(self):
        self.assertEqual(find_platform([2359], [2360], 1), 1)

    def test_complex_case_multiple_trains(self):
        self.assertEqual(find_platform([900, 1100, 1235, 1245], [1000, 1130, 1240, 1255], 4), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_platform("900", [1000], 1)
