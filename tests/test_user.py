import unittest
from app.models import User,Post
from app import db
class TestUSer(unittest.TestCase):
    """
    This is the class we will be using to test the users
    """

    def setUp(self):
        """
        This will create a new user before each test
        """
        self.new_user = User(username = "antony",bio = "haha",password ="antony")

    def tearDown(self):
        """
        This will clear the db after each test
        """
        User.query.delete()
        Post.query.delete()