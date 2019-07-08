import unittest
from app.models import Post,User

class TestPost(unittest.TestCase):
    """
    This is the class I will use to test the posts
    """

    def setUp(self):
        """
        This will create a new post before each test
        """
        self.new_post = Post(title = "Haha")

    def tearDown(self):
        """
        This will clear the db after every test
        """
        Post.query.delete()
        User.query.delete()