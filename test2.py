import unittest
from long_palin_sub_seq import lps

class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(lps("abcd",0,len("abcd")-1), 0)

    def testCase2(self):
        self.assertEqual(lps("abaaba",0,len("abaaba")-1), 4)

    

if __name__ == '__main__':
    unittest.main()