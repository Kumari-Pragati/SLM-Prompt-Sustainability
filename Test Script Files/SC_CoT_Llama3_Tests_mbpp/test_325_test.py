import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_Min_Squares(12), 3)

    def test_edge_case(self):
        self.assertEqual(get_Min_Squares(3), 3)
        self.assertEqual(get_Min_Squares(2), 1)
        self.assertEqual(get_Min_Squares(1), 1)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            get_Min_Squares(-1)

    def test_edge_case_zero(self):
        self.assertEqual(get_Min_Squares(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(get_Min_Squares(1), 1)

    def test_edge_case_two(self):
        self.assertEqual(get_Min_Squares(2), 1)

    def test_edge_case_three(self):
        self.assertEqual(get_Min_Squares(3), 3)

    def test_edge_case_four(self):
        self.assertEqual(get_Min_Squares(4), 2)

    def test_edge_case_five(self):
        self.assertEqual(get_Min_Squares(5), 3)

    def test_edge_case_six(self):
        self.assertEqual(get_Min_Squares(6), 3)

    def test_edge_case_seven(self):
        self.assertEqual(get_Min_Squares(7), 4)

    def test_edge_case_eight(self):
        self.assertEqual(get_Min_Squares(8), 4)

    def test_edge_case_nine(self):
        self.assertEqual(get_Min_Squares(9), 4)

    def test_edge_case_ten(self):
        self.assertEqual(get_Min_Squares(10), 4)

    def test_edge_case_eleven(self):
        self.assertEqual(get_Min_Squares(11), 4)

    def test_edge_case_twelve(self):
        self.assertEqual(get_Min_Squares(12), 3)

    def test_edge_case_thirteen(self):
        self.assertEqual(get_Min_Squares(13), 3)

    def test_edge_case_fourteen(self):
        self.assertEqual(get_Min_Squares(14), 3)

    def test_edge_case_fifteen(self):
        self.assertEqual(get_Min_Squares(15), 3)

    def test_edge_case_sixteen(self):
        self.assertEqual(get_Min_Squares(16), 4)

    def test_edge_case_seventeen(self):
        self.assertEqual(get_Min_Squares(17), 4)

    def test_edge_case_eighteen(self):
        self.assertEqual(get_Min_Squares(18), 4)

    def test_edge_case_nineteen(self):
        self.assertEqual(get_Min_Squares(19), 4)

    def test_edge_case_twenty(self):
        self.assertEqual(get_Min_Squares(20), 4)

    def test_edge_case_twenty_one(self):
        self.assertEqual(get_Min_Squares(21), 4)

    def test_edge_case_twenty_two(self):
        self.assertEqual(get_Min_Squares(22), 4)

    def test_edge_case_twenty_three(self):
        self.assertEqual(get_Min_Squares(23), 4)

    def test_edge_case_twenty_four(self):
        self.assertEqual(get_Min_Squares(24), 4)

    def test_edge_case_twenty_five(self):
        self.assertEqual(get_Min_Squares(25), 5)

    def test_edge_case_twenty_six(self):
        self.assertEqual(get_Min_Squares(26), 5)

    def test_edge_case_twenty_seven(self):
        self.assertEqual(get_Min_Squares(27), 5)

    def test_edge_case_twenty_eight(self):
        self.assertEqual(get_Min_Squares(28), 5)

    def test_edge_case_twenty_nine(self):
        self.assertEqual(get_Min_Squares(29), 5)

    def test_edge_case_thirty(self):
        self.assertEqual(get_Min_Squares(30), 5)

    def test_edge_case_thirty_one(self):
        self.assertEqual(get_Min_Squares(31), 5)

    def test_edge_case_thirty_two(self):
        self.assertEqual(get_Min_Squares(32), 5)

    def test_edge_case_thirty_three(self):
        self.assertEqual(get_Min_Squares(33), 5)

    def test_edge_case_thirty_four(self):
        self.assertEqual(get_Min_Squares(34), 5)

    def test_edge_case_thirty_five(self):
        self.assertEqual(get_Min_Squares(35), 5)

    def test_edge_case_thirty_six(self):
        self.assertEqual(get_Min_Squares(36), 5)

    def test_edge_case_thirty_seven(self):
        self.assertEqual(get_Min_Squares(37), 5)

    def test_edge_case_thirty_eight(self):
        self.assertEqual(get_Min_Squares(38), 5)

    def test_edge_case_thirty_nine(self):
        self.assertEqual(get_Min_Squares(39), 5)

    def test_edge_case_forty