import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):

    def test_simple(self):
        students = {
            "Alice": (18, 170),
            "Bob": (20, 180),
            "Charlie": (19, 175),
        }
        result = filter_data(students, 18, 170)
        self.assertDictEqual(result, {})

        result = filter_data(students, 18, 180)
        self.assertDictEqual(result, {"Alice": (18, 170)})

        result = filter_data(students, 19, 175)
        self.assertDictEqual(result, {"Charlie": (19, 175)})

    def test_edge_and_boundary(self):
        students = {
            "Dave": (0, 0),
            "Eve": (minint, minint),
            "Frank": (maxint, maxint),
        }
        result = filter_data(students, 0, 0)
        self.assertDictEqual(result, {"Dave": (0, 0)})

        result = filter_data(students, minint, minint)
        self.assertDictEqual(result, {"Eve": (minint, minint)})

        result = filter_data(students, maxint, maxint)
        self.assertDictEqual(result, {"Frank": (maxint, maxint)})

    def test_complex(self):
        students = {
            "George": (17, 160),
            "Henry": (18, 150),
            "Irene": (19, 175),
            "James": (20, 180),
            "Karen": (21, 190),
        }
        result = filter_data(students, 18, 170)
        self.assertDictEqual(result, {"Irene": (19, 175)})

        result = filter_data(students, 19, 169)
        self.assertDictEqual(result, {"Irene": (19, 175)})

        result = filter_data(students, 20, 181)
        self.assertDictEqual(result, {"James": (20, 180), "Karen": (21, 190)})
