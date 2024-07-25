#!/usr/bin/env python3
""" Parameterize a unit test.
"""

import unittest

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Testing access nested map.
    """
    def test_access_nested_map(self):
        """ Tests access mested map with a path key.
        """
        self.assertEqual(
            access_nested_map({"a": {"b": 2}}, ("a", "b")), 2)
