from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)
blog_endpoint = 'https://api.npoint.io/eb6cd8a5d783f501ee7d'
response = requests.get(blog_endpoint)
all_blogs = response.json()


@app.route('/')
def home():
    header = {'tag': 'home',
              'title': 'Clean Blog',
              'subtitle': 'A Blog Theme by Start Bootstrap'}
    return render_template('index.html', info=header, blogs=all_blogs)

@app.route('/about')
def about():
    header = {'tag': 'about',
            'title': 'About Me',
            'subtitle': 'This is what I do'}
    return render_template('about.html', info=header)

@app.route('/contact')
def contact():
    header = {'tag': 'contact',
            'title': 'Contact Me',
            'subtitle': 'Have questions? I have answers'}
    return render_template('contact.html', info=header)

@app.route('/post/<int:id>')
def show_post(id):
    
    for blog in all_blogs:
        if blog['id'] == id:
            data = blog
    header = {'tag': 'post',
            'title': data['title'],
            'subtitle': data['subtitle']}
    
    return render_template('post.html', post=data, info=header)


if __name__ == "__main__":
    app.run(debug=True)