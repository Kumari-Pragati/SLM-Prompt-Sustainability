import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_div_of_nums(self):
        self.assertEqual(div_of_nums([1,2,3,4,5,6,7,8,9,10],2,3), [2,3,4,6,8,9,10])
        self.assertEqual(div_of_nums([1,2,3,4,5,6,7,8,9,10],3,4), [3,6,9])
        self.assertEqual(div_of_nums([1,2,3,4,5,6,7,8,9,10],5,6), [5,6,10])
        self.assertEqual(div_of_nums([1,2,3,4,5,6,7,8,9,10],7,8), [7,8,14])
        self.assertEqual(div_of_nums([1,2,3,4,5,6,7,8,9,10],9,10), [9,10])
        self.assertEqual(div_of_nums([1,2,3,4,5,6,7,8,9,10],11,12), [])
        self.assertEqual(div_of_nums([1,2,3,4,5,6,7,8,9,10],10,11), [10])
        self.assertEqual(div_of_nums([1,2,3,4,5,6,7,8,9,10],12,13), [12])
        self.assertEqual(div_of_nums([1,2,3,4,5,6,7,8,9,10],15,16), [15,16])
