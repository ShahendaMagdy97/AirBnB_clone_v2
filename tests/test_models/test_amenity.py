#!/usr/bin/python3
"""test Amenity Model"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """test Amenity class"""

    def __init__(self, *args, **kwargs):
        """create a amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """test name id validation"""
        new = self.value()
        self.assertEqual(type(new.name), str)
