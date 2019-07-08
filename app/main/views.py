from . import main
from flask_login import current_user, login_required
from .forms import AddPostForm,SubscribeForm,AddComment,EditBio
from ..models import Post,User,Comment,Subscriber
from flask import redirect,url_for,render_template,flash,request
from .. import db,photos
from datetime import datetime
from app.email import create_mail

@main.route("/", methods = ["GET","POST"])
def index():
    form = SubscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        new_subscriber = Subscriber(email = email)
        db.session.add(new_subscriber)
        db.session.commit()
        flash("Thank You for subscribing!")
        return redirect(url_for("main.index"))
    posts = Post.query.order_by(Post.time.desc())
    title = "Home"
    return render_template("index.html",posts = posts,form = form,title = title)

