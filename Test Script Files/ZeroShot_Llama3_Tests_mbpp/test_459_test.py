import unittest
from mbpp_459_code import remove_uppercase

class TestRemove_Uppercase(unittest.TestCase):

    def test_remove_uppercase(self):
        self.assertEqual(remove_uppercase("Hello World"), "ello world")
        self.assertEqual(remove_uppercase("HELLO WORLD"), "ello world")
        self.assertEqual(remove_uppercase("123 ABC"), "123 bc")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF"), "123 bc 456 def")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI"), "123 bc 456 def 789 ghi")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL"), "123 bc 456 def 789 ghi 890 jkl")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL 901 MNO"), "123 bc 456 def 789 ghi 890 jkl 901 mno")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL 901 MNO 912 PQR"), "123 bc 456 def 789 ghi 890 jkl 901 mno 912 pqr")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL 901 MNO 912 PQR 913 STU"), "123 bc 456 def 789 ghi 890 jkl 901 mno 912 pqr 913 stu")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL 901 MNO 912 PQR 913 STU 914 VWX"), "123 bc 456 def 789 ghi 890 jkl 901 mno 912 pqr 913 stu 914 vwx")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL 901 MNO 912 PQR 913 STU 914 VWX 915 YZ"), "123 bc 456 def 789 ghi 890 jkl 901 mno 912 pqr 913 stu 914 vwx 915 yz")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL 901 MNO 912 PQR 913 STU 914 VWX 915 YZ 916 ABC"), "123 bc 456 def 789 ghi 890 jkl 901 mno 912 pqr 913 stu 914 vwx 915 yz 916 abc")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL 901 MNO 912 PQR 913 STU 914 VWX 915 YZ 916 ABC 917 DEF"), "123 bc 456 def 789 ghi 890 jkl 901 mno 912 pqr 913 stu 914 vwx 915 yz 916 abc 917 def")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL 901 MNO 912 PQR 913 STU 914 VWX 915 YZ 916 ABC 917 DEF 918 GHI"), "123 bc 456 def 789 ghi 890 jkl 901 mno 912 pqr 913 stu 914 vwx 915 yz 916 abc 917 def 918 ghi")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL 901 MNO 912 PQR 913 STU 914 VWX 915 YZ 916 ABC 917 DEF 918 GHI 919 JKL"), "123 bc 456 def 789 ghi 890 jkl 901 mno 912 pqr 913 stu 914 vwx 915 yz 916 abc 917 def 918 ghi 919 jkl")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL 901 MNO 912 PQR 913 STU 914 VWX 915 YZ 916 ABC 917 DEF 918 GHI 919 JKL 920 MNO"), "123 bc 456 def 789 ghi 890 jkl 901 mno 912 pqr 913 stu 914 vwx 915 yz 916 abc 917 def 918 ghi 919 jkl 920 mno")
        self.assertEqual(remove_uppercase("123 ABC 456 DEF 789 GHI 890 JKL 901 MNO 912 PQR 913 STU 914 VWX 915 YZ 916 ABC 917 DEF 918 GHI 919 JKL 920 MNO 921 PQR"), "123 bc 456 def 789 ghi 890 jkl 901 mno 912 pqr 913 stu 914 vwx 915 yz 916 abc 917 def 918 ghi 919