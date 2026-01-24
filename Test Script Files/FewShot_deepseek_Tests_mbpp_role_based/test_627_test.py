import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):
    def test_typical_use_case(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        start = 0
        end = len(array) - 1
        self.assertEqual(find_First_Missing(array, start, end), 10)

    def test_edge_condition(self):
        array = [0]
        start = 0
        end = 0
        self.assertEqual(find_First_Missing(array, start, end), 1)

    def test_boundary_condition(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        start = 0
        end = len(array) - 1
        self.assertEqual(find_First_Missing(array, start, end), 11)

    def test_invalid_input(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        start = 0
        end = -1
        with self.assertRaises(ValueError):
            find_First_Missing(array, start, end)
