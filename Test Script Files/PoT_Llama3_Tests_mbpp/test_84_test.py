import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 3)
        self.assertEqual(sequence(5), 5)

    def test_edge(self):
        self.assertEqual(sequence(10), 34)

    def test_edge2(self):
        self.assertEqual(sequence(11), 89)

    def test_edge3(self):
        self.assertEqual(sequence(12), 144)

    def test_edge4(self):
        self.assertEqual(sequence(13), 233)

    def test_edge5(self):
        self.assertEqual(sequence(14), 377)

    def test_edge6(self):
        self.assertEqual(sequence(15), 610)

    def test_edge7(self):
        self.assertEqual(sequence(16), 985)

    def test_edge8(self):
        self.assertEqual(sequence(17), 1567)

    def test_edge9(self):
        self.assertEqual(sequence(18), 2584)

    def test_edge10(self):
        self.assertEqual(sequence(19), 4188)

    def test_edge11(self):
        self.assertEqual(sequence(20), 6765)

    def test_edge12(self):
        self.assertEqual(sequence(21), 10946)

    def test_edge13(self):
        self.assertEqual(sequence(22), 17711)

    def test_edge14(self):
        self.assertEqual(sequence(23), 28657)

    def test_edge15(self):
        self.assertEqual(sequence(24), 46368)

    def test_edge16(self):
        self.assertEqual(sequence(25), 75025)

    def test_edge17(self):
        self.assertEqual(sequence(26), 121393)

    def test_edge18(self):
        self.assertEqual(sequence(27), 196418)

    def test_edge19(self):
        self.assertEqual(sequence(28), 317811)

    def test_edge20(self):
        self.assertEqual(sequence(29), 514229)

    def test_edge21(self):
        self.assertEqual(sequence(30), 832040)

    def test_edge22(self):
        self.assertEqual(sequence(31), 1346269)

    def test_edge23(self):
        self.assertEqual(sequence(32), 2178309)

    def test_edge24(self):
        self.assertEqual(sequence(33), 3524578)

    def test_edge25(self):
        self.assertEqual(sequence(34), 5702887)

    def test_edge26(self):
        self.assertEqual(sequence(35), 9227465)

    def test_edge27(self):
        self.assertEqual(sequence(36), 14930352)

    def test_edge28(self):
        self.assertEqual(sequence(37), 24157817)

    def test_edge29(self):
        self.assertEqual(sequence(38), 39088169)

    def test_edge30(self):
        self.assertEqual(sequence(39), 63245986)

    def test_edge31(self):
        self.assertEqual(sequence(40), 102334155)

    def test_edge32(self):
        self.assertEqual(sequence(41), 165580141)

    def test_edge33(self):
        self.assertEqual(sequence(42), 267914296)

    def test_edge34(self):
        self.assertEqual(sequence(43), 433494437)

    def test_edge35(self):
        self.assertEqual(sequence(44), 701408733)

    def test_edge36(self):
        self.assertEqual(sequence(45), 1134903170)

    def test_edge37(self):
        self.assertEqual(sequence(46), 1836311903)

    def test_edge38(self):
        self.assertEqual(sequence(47), 2971215073)

    def test_edge39(self):
        self.assertEqual(sequence(48), 4807526976)

    def test_edge40(self):
        self.assertEqual(sequence(49), 7778742049)

    def test_edge41(self):
        self.assertEqual(sequence(50), 12586269025)
