import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(prod_Square(36))

    def test_edge_case(self):
        self.assertFalse(prod_Square(1))
        self.assertFalse(prod_Square(2))
        self.assertFalse(prod_Square(3))
        self.assertFalse(prod_Square(4))
        self.assertFalse(prod_Square(5))
        self.assertFalse(prod_Square(6))
        self.assertFalse(prod_Square(7))
        self.assertFalse(prod_Square(8))
        self.assertFalse(prod_Square(9))
        self.assertFalse(prod_Square(10))

    def test_edge_case2(self):
        self.assertTrue(prod_Square(16))
        self.assertTrue(prod_Square(25))
        self.assertTrue(prod_Square(36))
        self.assertTrue(prod_Square(49))
        self.assertTrue(prod_Square(64))
        self.assertTrue(prod_Square(81))
        self.assertTrue(prod_Square(100))

    def test_edge_case3(self):
        self.assertFalse(prod_Square(11))
        self.assertFalse(prod_Square(12))
        self.assertFalse(prod_Square(13))
        self.assertFalse(prod_Square(14))
        self.assertFalse(prod_Square(15))
        self.assertFalse(prod_Square(16))
        self.assertFalse(prod_Square(17))
        self.assertFalse(prod_Square(18))
        self.assertFalse(prod_Square(19))
        self.assertFalse(prod_Square(20))

    def test_edge_case4(self):
        self.assertFalse(prod_Square(21))
        self.assertFalse(prod_Square(22))
        self.assertFalse(prod_Square(23))
        self.assertFalse(prod_Square(24))
        self.assertFalse(prod_Square(25))
        self.assertFalse(prod_Square(26))
        self.assertFalse(prod_Square(27))
        self.assertFalse(prod_Square(28))
        self.assertFalse(prod_Square(29))
        self.assertFalse(prod_Square(30))

    def test_edge_case5(self):
        self.assertFalse(prod_Square(31))
        self.assertFalse(prod_Square(32))
        self.assertFalse(prod_Square(33))
        self.assertFalse(prod_Square(34))
        self.assertFalse(prod_Square(35))
        self.assertFalse(prod_Square(36))
        self.assertFalse(prod_Square(37))
        self.assertFalse(prod_Square(38))
        self.assertFalse(prod_Square(39))
        self.assertFalse(prod_Square(40))

    def test_edge_case6(self):
        self.assertFalse(prod_Square(41))
        self.assertFalse(prod_Square(42))
        self.assertFalse(prod_Square(43))
        self.assertFalse(prod_Square(44))
        self.assertFalse(prod_Square(45))
        self.assertFalse(prod_Square(46))
        self.assertFalse(prod_Square(47))
        self.assertFalse(prod_Square(48))
        self.assertFalse(prod_Square(49))
        self.assertFalse(prod_Square(50))

    def test_edge_case7(self):
        self.assertFalse(prod_Square(51))
        self.assertFalse(prod_Square(52))
        self.assertFalse(prod_Square(53))
        self.assertFalse(prod_Square(54))
        self.assertFalse(prod_Square(55))
        self.assertFalse(prod_Square(56))
        self.assertFalse(prod_Square(57))
        self.assertFalse(prod_Square(58))
        self.assertFalse(prod_Square(59))
        self.assertFalse(prod_Square(60))

    def test_edge_case8(self):
        self.assertFalse(prod_Square(61))
        self.assertFalse(prod_Square(62))
        self.assertFalse(prod_Square(63))
        self.assertFalse(prod_Square(64))
        self.assertFalse(prod_Square(65))
        self.assertFalse(prod_Square(66))
        self.assertFalse(prod_Square(67))
        self.assertFalse(prod_Square(68))
        self.assertFalse(prod_Square(69))
        self.assertFalse(prod_Square(70))

    def test_edge_case9(self):
        self.assertFalse(prod_Square(71))
        self.assertFalse(prod_Square(72))
        self.assertFalse(prod_Square(73))
        self.assertFalse(prod_Square(74))
        self.assertFalse(prod_Square(75))
        self.assertFalse(prod_Square(76))
        self.assertFalse(prod_Square(77))
        self.assertFalse(prod_Square(78))
        self.assertFalse(prod_Square(79))
        self.assertFalse(prod_Square(80))

    def test_edge_case10(self):
        self.assertFalse(prod_Square(81))
        self.assertFalse(prod_Square(82))
        self.assertFalse(prod_Square(83))
        self.assertFalse(prod_Square(84))
        self.assertFalse(prod_Square(85))
        self.assertFalse(prod_Square(86))
        self.assertFalse(prod_Square(87))
        self.assertFalse(prod_Square(88))
        self.assertFalse(prod_Square(89))
        self.assertFalse(prod_Square(90))

    def test_edge_case11(self):
        self.assertFalse(prod_Square(91))
        self.assertFalse(prod_Square(92))
        self.assertFalse(prod_Square(93))