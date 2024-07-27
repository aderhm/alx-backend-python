#!/usr/bin/env python3
""" Parameterize a unit test.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Testing access nested map.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Tests access nested map with a path key.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Testing KeyError Exception raising.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Mocks HTTP calls.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Tests that utils.get_json returns the expected result.
        """
        return_value = {'return_value.json.return_value': test_payload}
        p = patch('requests.get', **return_value)
        mock = p.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        p.stop()
