import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(octal_To_Decimal(0), 0)

    def test_single_digit(self):
        for num, expected in [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]:
            self.assertEqual(octal_To_Decimal(num), expected)

    def test_multiple_digits(self):
        for num, expected in [(10, 8), (11, 9), (12, 10), (13, 11), (14, 12), (15, 13), (16, 14), (17, 15), (20, 16), (21, 17), (22, 18), (23, 19), (24, 20), (25, 21), (26, 22), (27, 23), (30, 24), (31, 25), (32, 26), (33, 27), (34, 28), (35, 29), (36, 30), (37, 31), (40, 32), (41, 33), (42, 34), (43, 35), (44, 36), (45, 37), (46, 38), (47, 39), (50, 40), (51, 41), (52, 42), (53, 43), (54, 44), (55, 45), (56, 46), (57, 47), (60, 48), (61, 49), (62, 50), (63, 51), (70, 52), (71, 53), (72, 54), (73, 55), (74, 56), (75, 57), (76, 58), (77, 59), (80, 60), (81, 61), (82, 62), (83, 63), (90, 64), (91, 65), (92, 66), (93, 67), (100, 68), (101, 69), (102, 70), (103, 71), (110, 72), (111, 73), (112, 74), (113, 75), (114, 76), (115, 77), (116, 78), (117, 79), (120, 80), (121, 81), (122, 82), (123, 83), (130, 84), (131, 85), (132, 86), (133, 87), (140, 88), (141, 89), (142, 90), (143, 91), (150, 92), (151, 93), (152, 94), (153, 95), (154, 96), (155, 97), (156, 98), (157, 99)]:
            self.assertEqual(octal_To_Decimal(num), expected)

    def test_negative_input(self):
        self.assertRaises(ValueError, octal_To_Decimal, -1)

    def test_non_integer_input(self):
        self.assertRaises(TypeError, octal_