"""
Given a valid (IPv4) IP address, return a defanged version of that IP 
address.

A defanged IP address replaces every period "." with "[.]".
"""
import unittest
import re

def validIP(ipString):
    exp = "[0-255]\.[0-255]\.[0-255]\.[0-255]"
    return re.search(exp, ipString)

def defang(ipString):
    return "[.]".join(ipString.split("."))


class Test(unittest.TestCase):
    def setUp(self):
        self.input = [
            "1.1.1.1",
            "255.100.50.0",
            "123.123.123.123"
        ]
        self.expected = [
            "1[.]1[.]1[.]1",
            "255[.]100[.]50[.]0",
            "123[.]123[.]123[.]123"
        ]
    def test_validIP(self):
        for i, j in zip(self.input, self.expected):
            self.assertEqual(defang(i),j)

if __name__ == "__main__":
    unittest.main()