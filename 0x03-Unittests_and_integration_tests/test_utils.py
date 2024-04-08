#!/usr/bin/env python3
""" 0. Parameterize a unit test"""

import unittest
from parameterized import parameterized
from utils import (access_nested_map)


class TestAccessNestedMap(unittest.TestCase):
    """ class that inherits from unittest.TestCase"""
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, exp):
        """to test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), exp)

    @parameterized.expand([({}, ("a",), KeyError),
                           ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, nested_map, path, exp):
        """ the assertRaises context manager to test that a KeyError"""
        with self.assertRaises(exp):
            access_nested_map(nested_map, path)
