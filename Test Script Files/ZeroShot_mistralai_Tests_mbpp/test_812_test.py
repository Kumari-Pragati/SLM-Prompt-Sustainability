import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(road_rd(''), '')

    def test_no_road(self):
        self.assertEqual(road_rd('Main Street'), 'Main Street')

    def test_single_road(self):
        self.assertEqual(road_rd('Road'), 'Rd.')

    def test_multiple_road(self):
        self.assertEqual(road_rd('First Road Second Road'), 'First Rd. Second Road')

    def test_multiple_road_with_spaces(self):
        self.assertEqual(road_rd('First Road   Second Road'), 'First Rd.   Second Road')

    def test_multiple_road_with_punctuation(self):
        self.assertEqual(road_rd('First Road, Second Road'), 'First Rd., Second Road')

    def test_multiple_road_with_numbers(self):
        self.assertEqual(road_rd('1st Road, 2nd Road'), '1st Rd., 2nd Rd.')

    def test_multiple_road_with_numbers_and_punctuation(self):
        self.assertEqual(road_rd('1st Road, 2nd Road, 3rd Road'), '1st Rd., 2nd Rd., 3rd Rd.')
