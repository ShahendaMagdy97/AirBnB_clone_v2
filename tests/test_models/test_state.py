#!/usr/bin/python3
"""test State Model"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """test State class"""

    def __init__(self, *args, **kwargs):
        """test State instance"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test name id validation"""
        new = self.value()
        self.assertEqual(type(new.name), str)
