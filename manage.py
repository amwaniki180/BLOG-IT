from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Post, Comment
from flask_migrate import Migrate, MigrateCommand

app = create_app("test")

manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(db = db, app = app, User = User, Post = Post, Comment = Comment)
