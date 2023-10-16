from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy as sa

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []

db = sa()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new3-books.db"

db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    results = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = results.scalars()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('add.html')

@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get('id')
    if book_id:
        book_to_edit = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    
    if request.method == "POST":
        book_to_edit.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('edit.html', book=book_to_edit)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    if book_id:
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

