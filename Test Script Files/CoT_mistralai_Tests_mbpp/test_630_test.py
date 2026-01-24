import unittest
from mbpp_630_code import Iterable
from itertools import chain, islice
from copy import deepcopy

from 630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):

    def test_empty_input(self):
        self.assertListEqual(get_coordinates([]), [])

    def test_single_element(self):
        for test_case in [(1,), ([1],), ([1, 1],), ([1, 1, 1],)]:
            self.assertListEqual(get_coordinates(test_case), [[]])

    def test_multiple_elements(self):
        for test_case in [
            ([1, 2], [0, 1, 2]),
            ([1, 2, 3], [0, 1, 2]),
            ([1, 2, 3, 4], [0, 1, 2, 3]),
            ([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]),
            ([1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5]),
        ]:
            self.assertListEqual(get_coordinates(test_case), list(chain(*[iter(range(i, i + 3)) for i in test_case])))

    def test_negative_elements(self):
        for test_case in [
            ([-1, 2], [-2, -1, 0, 1, 2]),
            ([-1, 2, 3], [-2, -1, 0, 1, 2]),
            ([-1, 2, 3, -4], [-2, -1, 0, 1, 2, -3, -2, -1]),
        ]:
            self.assertListEqual(get_coordinates(test_case), list(chain(*[iter(range(i, i + 3)) for i in test_case if i < 0])))

    def test_invalid_input(self):
        invalid_inputs = [
            (1.5,),
            ([], 1),
            ([1], 1),
            ([1, 2], "a"),
            ([1, 2], [1, "a"]),
            ([1, 2], [1, [1]]),
            ([1, 2], [1, [1, 2]]),
            ([1, 2], [1, [1, 2, 3]]),
        ]
        for invalid_input in invalid_inputs:
            with self.subTest(input=invalid_input):
                with self.assertRaises(TypeError):
                    get_coordinates(invalid_input)
