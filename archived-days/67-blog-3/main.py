from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

# Init CKEditor
ckeditor = CKEditor(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message="Bad Name")])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    img_url = StringField('Background Image (URL)', validators=[DataRequired(), URL()])
    body = CKEditorField('Body', validators=[DataRequired()])

    submit = SubmitField('Submit Post')


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars().all()

    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/post/new', methods=["GET", "POST"])
def new_post():
    add_form = NewPostForm()
    if add_form.validate_on_submit():
        print(request.form['title'])
        new_post = BlogPost(
            title=request.form['title'],
            subtitle=request.form['subtitle'],
            author='Adam',
            date=str(date.today()),
            img_url=request.form['img_url'],
            body=request.form['body'])
        db.session.add(new_post)
        db.session.commit()
        
        return redirect(url_for('show_post', post_id=new_post.id))
    
    return render_template('make-post.html', form=add_form)

# TODO: edit_post() to change an existing blog post
@app.route('/post/<int:post_id>/edit', methods=["GET", "POST"])
def edit_post(post_id):
    if post_id:
        post_to_edit = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()

    edit_form = NewPostForm(
        title=post_to_edit.title,
        subtitle=post_to_edit.subtitle,
        img_url=post_to_edit.img_url,
        body=post_to_edit.body
    )
    
    if edit_form.validate_on_submit():
        post_to_edit.title = request.form['title']
        post_to_edit.subtitle=request.form['subtitle']
        post_to_edit.img_url=request.form['img_url']
        post_to_edit.body=request.form['body']
        db.session.commit()
        
        return redirect(url_for('show_post', post_id=post_to_edit.id))
    return render_template('make-post.html', form=edit_form)

# TODO: delete_post() to remove a blog post from the database

@app.route('/post/<int:post_id>/delete')
def delete_post(post_id):
    if post_id:
        post_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
        db.session.delete(post_to_delete)
        db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
