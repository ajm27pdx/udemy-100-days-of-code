from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)

blog_endpoint = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(blog_endpoint)
all_blogs = response.json()


@app.route('/')
def home():
    return render_template('index.html', current_year=date.today().year)


@app.route('/guess/<string:n>')
def guess(n):
    agify_endpoint = 'https://api.agify.io'
    parameters = {
        'name': n,
    }
    response = requests.get(agify_endpoint, params=parameters)
    response.raise_for_status()
    age_response = response.json()['age']

    genderize_endpoint = 'https://api.genderize.io'
    parameters = {
        'name': n,
    }
    response = requests.get(genderize_endpoint, params=parameters)
    response.raise_for_status()
    gender_response = response.json()['gender']
    return render_template('guess.html', name=n, age=age_response, gender=gender_response)


@app.route('/blogs')
def blogs():
    return render_template('blogs.html', blogs=all_blogs)


@app.route('/blogs/<int:n>')
def show_blog(n):
    blog_rq = None
    for blog in all_blogs:
        if blog['id'] == n:
            blog_rq = blog
    return render_template('blog.html', blog=blog_rq)


if __name__ == "__main__":
    app.run(debug=True)
