import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_typical_case(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        start = 0
        end = len(array) - 1
        self.assertEqual(find_First_Missing(array, start, end), 10)

    def test_empty_array(self):
        array = []
        start = 0
        end = len(array) - 1
        self.assertEqual(find_First_Missing(array, start, end), 1)

    def test_array_with_missing_first_element(self):
        array = [1, 2, 3, 4, 5]
        start = 0
        end = len(array) - 1
        self.assertEqual(find_First_Missing(array, start, end), 0)

    def test_array_with_missing_last_element(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        start = 0
        end = len(array) - 1
        self.assertEqual(find_First_Missing(array, start, end), 9)

    def test_array_with_missing_middle_element(self):
        array = [0, 1, 2, 3, 5, 6, 7, 8, 9]
        start = 0
        end = len(array) - 1
        self.assertEqual(find_First_Missing(array, start, end), 4)

    def test_array_with_duplicates(self):
        array = [0, 1, 2, 2, 4, 5, 6, 7, 8, 9]
        start = 0
        end = len(array) - 1
        self.assertEqual(find_First_Missing(array, start, end), 3)
