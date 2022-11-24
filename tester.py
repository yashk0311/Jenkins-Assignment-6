#!/usr/bin/python3

import unittest
from prob1 import OddEven
from prob2 import pred

class Calculator(unittest.TestCase):

    def test_OddEven(self):
        x = 11
        res = OddEven(x)
        self.assertEqual(res, 12)

    def test_pred(self):
        x = 99
        res1 = pred(x)
        self.assertEqual(res1, 98)
    
    

if __name__ == '__main__':
    unittest.main()
