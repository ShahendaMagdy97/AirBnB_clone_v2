#!/usr/bin/python3
"""test User Model"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """test User class"""

    def __init__(self, *args, **kwargs):
        """test User instance"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test first name id validation"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """test last name id validation"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test email id validation"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test password id validation"""
        new = self.value()
        self.assertEqual(type(new.password), str)
