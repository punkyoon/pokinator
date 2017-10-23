# -*- coding: utf-8 -*-

import re
import unittest

from pokinator import Pokinator


class NameGenTest(unittest.TestCase):
    def test_generate(self):
        self.assertTrue(re.match(r'\w+-\w+-\d+', Pokinator.generate()))

    def test_generate_lowercase(self):
        self.assertTrue(re.match(r'[a-z]+-[a-z]+-\d+', Pokinator.generate(lowercase=True)))

    def test_generate_generation(self):
        for i in range(1, 7):
            self.assertTrue(re.match(r'\w+-\w+-\d+', Pokinator.generate(generation=i)))

    def test_not_equal_in_repeated_call(self):
        self.assertNotEqual(Pokinator.generate(), Pokinator.generate())

    def test_configurable_range(self):
        self.assertTrue(re.match(r'\w+-\w+-\d$', Pokinator.generate(9)))

    def test_wrong_generation(self):
        with self.assertRaises(RuntimeError):
            Pokinator.generate(generation=0)
        with self.assertRaises(RuntimeError):
            Pokinator.generate(generation=8)

    def test_wrong_range(self):
        with self.assertRaises(RuntimeError):
            Pokinator.generate('1')
        with self.assertRaises(RuntimeError):
            Pokinator.generate(-1)

    def test_wrong_delimiter(self):
        with self.assertRaises(RuntimeError):
            Pokinator.generate(delimiter=1)

    def test_wrong_digit(self):
        with self.assertRaises(RuntimeError):
            Pokinator.generate(digit=3)
            Pokinator.generate(token_range=999, digit=4)


def run_test():
    print('#1 value test : ' + Pokinator.generate())
    print('#2 value test : ' + Pokinator.generate(9))
    print('#3 value test : ' + Pokinator.generate(delimiter='*'))
    print('#4 value test : ' + Pokinator.generate(token_range=999, digit=3))
    print('#5 value test : ' + Pokinator.generate(generation=2))
    print('#6 value test : ' + Pokinator.generate(lowercase=True))

    ts = unittest.makeSuite(NameGenTest,  'test')
    runner = unittest.TextTestRunner()
    runner.run(ts)
