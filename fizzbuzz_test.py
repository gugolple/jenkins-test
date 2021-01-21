#!/usr/bin/env python3

import sys
import unittest
import random
import string
from fizzbuzz import fizzbuzz

def RandomString(letters, length):
    return ''.join(random.choices(letters, k=length))

class TestFizzBuzz(unittest.TestCase):
    #Main class for testing, required for use with unittest to inherit it

    def TestCheck(self,start,end,multiples,answers):
        #Check of the fizzbuzz result against a known and proven algorithm
        result = fizzbuzz(start,end,multiples,answers)
        for position,number in enumerate(range(start,end+1)):
            calculated = []
            for position_multiple,multiple in enumerate(multiples):
                if number % multiple == 0:
                    calculated.append(answers[position_multiple])

            if len(calculated) == 0:
                calculated.append(number)

            self.assertEqual(result[position],calculated)

    def TestGenerator(self):
        #Create variable input to test the fizzbuzz algorithm
        for iteration in range(10):
            start = random.randint(0,100)
            end = start + random.randint(0,100)
            count = random.randint(1,10)
            multiples = [random.randint(1,100) for i in range(count)]
            answers = [RandomString(string.ascii_uppercase,random.randint(1,7)) for i in range(count)]
            print("Start test {:03d}".format(iteration))
            print(start,end,count,multiples,answers)
            self.TestCheck(start,end,multiples,answers)


if __name__ == "__main__":
    TestFizzBuzz().TestGenerator()

