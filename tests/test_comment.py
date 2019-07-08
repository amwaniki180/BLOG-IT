import unittest
from app.models import Post,Comment

class TestComment(unittest.TestCase):
    """
    This is the class I will use to test the comments
    """

    def setUp(self):
        """
        This will create a new comment before each test
        """
        self.new_comment = Comment(title = "Haha")
