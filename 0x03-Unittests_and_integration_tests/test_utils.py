#!/usr/bin/env python3
""" 0. Parameterize a unit test"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import (access_nested_map, get_json)


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


class TestGetJson(unittest.TestCase):
    """class and implement the TestGetJson.test_get_json method to test """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """method that returns test_payload"""
        dic = {'json.return_value': test_payload}
        with pitch('requests.get', return_value=Mock(**dic)) as f:
            self.assertEqual(get_json(test_url), test_payload)
            f.assert_called_once_with(test_url)
