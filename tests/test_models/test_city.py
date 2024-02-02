#!/usr/bin/python3
"""test City Model"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """test City class"""

    def __init__(self, *args, **kwargs):
        """create a city instance"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """test state id validation"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """test name id validation"""
        new = self.value()
        self.assertEqual(type(new.name), str)
