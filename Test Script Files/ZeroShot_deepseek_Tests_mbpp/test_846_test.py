import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):

    def test_find_platform(self):
        self.assertEqual(find_platform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000], 6), 3)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 910, 1030, 1100, 1130, 1500, 1800], [930, 1200, 1120, 1130, 1900, 2000], 6), 3)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([900, 1100, 1235], [1000, 1200, 1230], 3), 1)
        self.assertEqual(find_platform([9