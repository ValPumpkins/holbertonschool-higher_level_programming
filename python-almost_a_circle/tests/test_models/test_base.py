#!/usr/bin/python3
""" Unittest for Base class """

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """ Testing instantiation of Base class """

    def test_no_instance_creation(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_instance_creation_with_id(self):
        base1 = Base(10)
        self.assertEqual(base1.id, 10)

    def test_more_creation(self):
        base1 = Base(11)
        base2 = Base(42)
        base3 = Base(1337)
        self.assertEqual(base1.id, 11)
        self.assertEqual(base2.id, 42)
        self.assertEqual(base3.id, 1337)

    def test_None_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_negative_id(self):
        self.assertEqual(-5, Base(-5).id)

    def test_float_id(self):
        self.assertEqual(3.14, Base(3.14).id)

    def test_zero_id(self):
        self.assertEqual(0, Base(0).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    # JSON
    def test_empty_list(self):
        """ Testing with empyt list """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_non_empty_list(self):
        """ Testing with non-empty list"""
        list_of_dicts = [{"key1": "value1", "key2": "value2"}, {"key3": "value3"}]
        result = Base.to_json_string(list_of_dicts)
        expected_json = '[{"key1": "value1", "key2": "value2"}, {"key3": "value3"}]'
        self.assertEqual(result, expected_json)

    def test_none_list(self):
        """ Test with None list """
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_non_empty_dict(self):
        """ Test with non-empty dict """
        dict_of_dicts = {"key1": "value1", "key2": "value2"}
        result = Base.to_json_string(dict_of_dicts)
        expected_json = '{"key1": "value1", "key2": "value2"}'
        self.assertEqual(result, expected_json)

    def test_non_empty_string(self):
        """ Test with non-empty string """
        string_of_dicts = "key1:value1,key2:value2"
        result = Base.to_json_string(string_of_dicts)
        expected_json = '"key1:value1,key2:value2"'
        self.assertEqual(result, expected_json)

    def test_list_of_dicts(self):
        """ Test with non-empty list of dicts """
        list_of_dicts = [{"key1": "value1", "key2": "value2"}, {"key3": "value3"}]
        result = Base.to_json_string(list_of_dicts)
        expected_json = '[{"key1": "value1", "key2": "value2"}, {"key3": "value3"}]'
        self.assertEqual(result, expected_json)

    def test_list_of_strings(self):
        """ Test with list of strings """
        list_of_strings = ["key1:value1", "key2:value2"]
        result = Base.to_json_string(list_of_strings)
        expected_json = '["key1:value1", "key2:value2"]'
        self.assertEqual(result, expected_json)

    def test_list_of_ints(self):
        """ Test with non-empty list of ints """
        list_of_ints = [1, 2, 3]
        result = Base.to_json_string(list_of_ints)
        expected_json = '[1, 2, 3]'
        self.assertEqual(result, expected_json)

    def test_list_of_floats(self):
        """ Test with non-empty list of floats """
        list_of_floats = [1.1, 2.2, 3.3]
        result = Base.to_json_string(list_of_floats)
        expected_json = '[1.1, 2.2, 3.3]'
        self.assertEqual(result, expected_json)

if __name__ == '__main__':
    unittest.main()
