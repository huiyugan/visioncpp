from __future__ import print_function

from unittest import TestCase

import visioncpp as vp
from visioncpp import util


class TestClass(object):
    x = 5
    def __init__(self, y):
        self.y = y

    def gety(self):
        return self.y

    def getxplus(self, z):
        return self.x + z


class test_util(TestCase):
    def test_foreach(self):
        res = []
        def f(x):
            res.append(x)

        util.foreach(f,  [1, 2, 3, 4, 5])
        self.assertEqual([1, 2, 3, 4, 5], res)

    def test_call_if_attribute(self):
        x = TestClass(10)
        self.assertEqual(util.call_if_attribute(x, "gety"), 10)
        self.assertEqual(util.call_if_attribute(x, "getxplus", 2), 7)
        self.assertEqual(util.call_if_attribute(x, "nope"), None)

    def test_get_attribute(self):
        x = TestClass(10)
        self.assertEqual(util.get_attribute(x, "x"), 5)
        self.assertEqual(util.get_attribute(x, "nope"), None)
