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
   
      def tearDown(self):
        """
        THis will clear the db after each test
        """
        Post.query.delete()
        Comment.query.delete()

    def test_is_instance(self):
        """
        This will test whether the comment created is an instance of the Comment class
        """
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_init(self):
        """
        This willl test whether the new_commment is instantiated correctly
        """
        self.assertTrue(self.new_comment.title == "Haha")


    

