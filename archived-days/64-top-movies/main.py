from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy as sa
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from keys import key

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

tmdb_url = "https://api.themoviedb.org/3"
headers = {
    "accept": "application/json",
    "Authorization": key
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies2.db"
Bootstrap5(app)

db =sa()
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250))
    
class EditForm(FlaskForm):
    rating = StringField('Edit Your Rating', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class AddForm(FlaskForm):
    title = StringField('Enter Movie Title', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    results = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = results.scalars()
    # print(len(results.all()))
    rows = db.session.query(Movie).count()
    return render_template("index.html", movies=all_movies, num=rows)

@app.route('/add', methods=["GET", "POST"])
def add():
    add_form = AddForm()
    
    if add_form.validate_on_submit():
        q = request.form['title']
        return redirect(url_for('select', q=q))
    
    return render_template('add.html', form=add_form)

@app.route('/add/select')
def select():
    search_title = request.args.get('q')
    parameters = {
    'query': search_title,
    'include_adult': 'false',
    'language': 'en-US'
    }
    response = requests.get(tmdb_url + '/search/movie', headers=headers, params=parameters)
    response.raise_for_status()
    movie_data = response.json()['results']
    return render_template('select.html', query=search_title, movies=movie_data)

@app.route('/add/<id>')
def add_movie(id):
    response = requests.get(tmdb_url + '/movie/' + id, headers=headers)
    response.raise_for_status()
    movie = response.json()
    new_movie = Movie(
        title=movie['original_title'],
        year=movie['release_date'][:4],
        description=movie['overview'],
        rating=0.0,
        ranking=0,
        review='',
        img_url='https://image.tmdb.org/t/p/w500' + movie['poster_path']
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))

@app.route('/edit', methods=["GET", "POST"])
def edit():
    edit_form = EditForm()
    movie_id = request.args.get('id')
    if movie_id:
        movie_to_edit = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        
    if edit_form.validate_on_submit():
        print("True")
        movie_to_edit.rating = request.form['rating']
        movie_to_edit.review = request.form['review']
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print("False")
    return render_template('edit.html', form=edit_form, movie=movie_to_edit)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    if movie_id:
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
